"""
Orchestrator Agent - Coordinates the four persona agents
"""
import asyncio
from typing import List, Dict, Any
from datetime import datetime
import os
import uuid

from google.adk import Runner
from google.adk.agents import Agent, ParallelAgent
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types as genai_types

from .cognitive_behavioral import CognitiveBehavioralAgent
from .empathetic_friend import EmpatheticFriendAgent
from .rational_analyst import RationalAnalystAgent
from .mindfulness_mentor import MindfulnessMentorAgent

class PersonaReflectOrchestrator:
    """
    Main orchestrator that coordinates all persona agents
    """
    
    def __init__(self):
        """Initialize the orchestrator with all persona agents"""
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        
        # Initialize persona agents
        self.cognitive_agent = CognitiveBehavioralAgent()
        self.empathetic_agent = EmpatheticFriendAgent()
        self.rational_agent = RationalAnalystAgent()
        self.mindfulness_agent = MindfulnessMentorAgent()
        
        # Create parallel agent for concurrent persona processing
        self.parallel_processor = ParallelAgent(
            name="persona_parallel_processor",
            sub_agents=[
                self.cognitive_agent.agent,
                self.empathetic_agent.agent,
                self.rational_agent.agent,
                self.mindfulness_agent.agent,
            ]
        )
        
        # Create main orchestrator agent
        self.orchestrator = Agent(
            name="persona_reflect_orchestrator",
            model=self.model,
            instruction="""You are the PersonaReflect Orchestrator.
            
            Your role is to:
            1. Receive user dilemmas and coordinate responses from four specialized AI coaches
            2. Ensure each persona provides unique, valuable insights
            3. Synthesize insights into coherent action plans when requested
            4. Maintain conversation context and user history
            
            Remember:
            - Each persona should maintain their distinct voice and approach
            - Responses should be empathetic, actionable, and non-judgmental
            - Focus on empowering users to find their own solutions
            """,
            description="Orchestrates multi-persona self-reflection coaching"
        )
    
    async def process_dilemma(
        self,
        user_id: str,
        dilemma: str,
        context: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """
        Process a user's dilemma through all persona agents
        With lightweight context: if recent_dilemmas provided, personas see reflection journey
        Now includes intent detection for context-aware routing
        """
        print(f"🎭 Orchestrator processing dilemma for user: {user_id}")

        # Detect user intent from dilemma
        intent_info = self._detect_intent(dilemma)

        # Enrich context based on detected intent
        if intent_info["primary"]:
            context["detected_intent"] = intent_info["primary"]

            # For scheduling intents, add routing hint
            if "schedule" in intent_info["intents"]:
                context["routing_hint"] = "User wants to schedule time. Alex (Rational Analyst) should use calendar tools to find and book time slots."
                print("📅 Schedule intent detected - routing hint added for calendar tools")

            # For CBT intents, add thought pattern focus
            elif "cbt" in intent_info["intents"]:
                context["routing_hint"] = "Focus on identifying thought patterns and cognitive distortions. Dr. Chen should use CBT tools."
                print("🧠 CBT intent detected - routing hint added for thought pattern analysis")

            # For mindfulness intents, suggest breath-first approach
            elif "mindfulness" in intent_info["intents"]:
                context["routing_hint"] = "User needs grounding and present-moment awareness. Sage should offer mindfulness practices."
                print("🧘 Mindfulness intent detected - routing hint added for grounding practices")

            # For support intents, flag for resource offering
            elif "support" in intent_info["intents"]:
                context["routing_hint"] = "User may need professional resources or crisis support. Maya should assess and offer appropriate resources."
                print("💙 Support intent detected - routing hint added for resource offering")

        # Build context hint from user's reflection journey (lightweight memory)
        context_hint = self._build_context_hint(context)

        # Prepare the message for all personas with journey context
        journey_instruction = "Consider the user's ongoing reflection journey when forming your response." if context_hint else ""

        prompt = f"""
        User Dilemma: {dilemma}

        Context: {context if context else 'No additional context provided'}
        {context_hint}

        Please provide your unique perspective and guidance for this dilemma.
        {journey_instruction}
        """

        # Process through all personas in parallel
        tasks = [
            self._get_persona_response(self.cognitive_agent, prompt),
            self._get_persona_response(self.empathetic_agent, prompt),
            self._get_persona_response(self.rational_agent, prompt),
            self._get_persona_response(self.mindfulness_agent, prompt)
        ]

        responses = await asyncio.gather(*tasks)

        # Extract suggested actions from responses
        suggested_actions = await self._synthesize_actions(responses, dilemma)

        return {
            "id": f"entry-{datetime.now().timestamp()}",
            "responses": responses,
            "suggested_actions": suggested_actions,
            "detected_intent": intent_info["primary"]  # Include in response for frontend
        }

    async def _invoke_agent(
        self,
        agent: Agent,
        session_prefix: str,
        prompt: str,
        user_id: str = "persona_reflect",
    ) -> str:
        """Execute an ADK agent with a single-turn prompt."""
        runner = Runner(
            agent=agent,
            app_name="persona_reflect",
            session_service=InMemorySessionService(),
        )
        session_id = f"{session_prefix}-{uuid.uuid4()}"
        message = genai_types.Content(
            role="user",
            parts=[genai_types.Part(text=prompt)]
        )
        response_text = ""

        try:
            await runner.session_service.create_session(
                app_name="persona_reflect",
                user_id=user_id,
                session_id=session_id,
            )

            async for event in runner.run_async(
                user_id=user_id,
                session_id=session_id,
                new_message=message,
            ):
                if event.author == "user":
                    continue
                if event.content and event.content.parts:
                    text_fragments = [
                        part.text or ""
                        for part in event.content.parts
                        if getattr(part, "text", None)
                    ]
                    if text_fragments:
                        response_text = "".join(text_fragments).strip()

                if getattr(event, "is_final_response", None) and event.is_final_response():
                    break
        finally:
            await runner.close()

        return response_text
    
    async def _get_persona_response(
        self,
        persona_agent,
        prompt: str
    ) -> Dict[str, str]:
        """
        Get response from a specific persona agent
        """
        try:
            response_text = await self._invoke_agent(
                persona_agent.agent,
                session_prefix=persona_agent.persona_id,
                prompt=prompt,
                user_id="demo_user",
            )
        except Exception as e:
            print(f"❌ Error getting response from {persona_agent.name}: {str(e)}")
            response_text = ""

        if not response_text:
            response_text = "I'm having trouble processing this right now. Please try again."

        return {
            "persona": persona_agent.persona_id,
            "name": persona_agent.name,
            "icon": persona_agent.icon,
            "response": response_text
        }
    
    async def _synthesize_actions(
        self,
        responses: List[Dict[str, str]],
        dilemma: str
    ) -> List[str]:
        """
        Synthesize responses into suggested action steps
        """
        synthesis_prompt = f"""
        Based on the following diverse perspectives on this dilemma:
        
        Dilemma: {dilemma}
        
        Perspectives:
        {self._format_responses(responses)}
        
        Please synthesize these insights into 3-5 concrete, actionable steps.
        Focus on practical actions the user can take immediately.
        Return only the action steps as a numbered list.
        """
        
        try:
            result_text = await self._invoke_agent(
                self.orchestrator,
                session_prefix="orchestrator-synthesis",
                prompt=synthesis_prompt,
            )
            actions = result_text.strip().split("\n")
            # Clean up the actions
            actions = [
                action.strip().lstrip("0123456789. ")
                for action in actions
                if action.strip()
            ]
            return actions[:5]  # Limit to 5 actions
        except Exception as e:
            print(f"❌ Error synthesizing actions: {str(e)}")
            return []
    
    def _format_responses(self, responses: List[Dict[str, str]]) -> str:
        """Format responses for synthesis"""
        formatted = []
        for resp in responses:
            formatted.append(f"{resp['name']} ({resp['persona']}): {resp['response']}")
        return "\n\n".join(formatted)
    
    def _detect_intent(self, dilemma: str) -> Dict[str, Any]:
        """
        Detect user intent from dilemma text using keyword matching.

        Returns:
            Dictionary with detected intents and primary intent
        """
        dilemma_lower = dilemma.lower()

        # Define intent keywords
        intents = {
            "schedule": [
                "schedule", "calendar", "time block", "plan time", "book",
                "set aside", "when can i", "find time", "block out", "allocate time"
            ],
            "cbt": [
                "stuck", "negative thought", "anxious", "procrastinating",
                "distortion", "thinking", "worry", "ruminating", "overthinking",
                "can't stop thinking", "spiraling", "anxious about"
            ],
            "mindfulness": [
                "overwhelmed", "breathe", "grounding", "present", "anxious",
                "calm down", "center", "focus", "racing thoughts", "can't focus",
                "stressed", "tense", "tight", "body", "relax"
            ],
            "support": [
                "help", "resources", "crisis", "don't know what to do",
                "need support", "feeling lost", "don't know where to turn",
                "therapy", "counseling", "professional help", "suicide", "self-harm"
            ]
        }

        detected = []
        for intent, keywords in intents.items():
            if any(keyword in dilemma_lower for keyword in keywords):
                detected.append(intent)

        # Determine primary intent (first detected)
        primary = detected[0] if detected else None

        if detected:
            print(f"🎯 Intent Detection: {detected} (primary: {primary})")

        return {
            "intents": detected,
            "primary": primary
        }

    def _build_context_hint(self, context: Dict[str, Any]) -> str:
        """
        Build lightweight context hint from user's reflection journey
        NO DATABASE - just uses context dict passed from frontend

        Example frontend usage:
        {
            "recent_dilemmas": ["Stressed about work", "Feeling overwhelmed"],
            "growth_area": "work-life-balance",  # optional
            "detected_intent": "schedule"  # added by orchestrator
        }
        """
        hints = []

        # Add recent reflection topics if provided
        recent = context.get("recent_dilemmas", [])
        if recent and isinstance(recent, list) and len(recent) > 0:
            # Take last 2-3 for brevity
            recent_topics = recent[-3:] if len(recent) > 3 else recent
            topics_str = ", ".join([f'"{topic}"' for topic in recent_topics])
            hints.append(f"User has been reflecting on: {topics_str}")
            print(f"💭 Context: User reflecting on {len(recent_topics)} recent topics")

        # Add growth area focus if provided
        growth_area = context.get("growth_area")
        if growth_area and isinstance(growth_area, str):
            hints.append(f"Focus area: {growth_area}")
            print(f"🎯 Context: Focus area = {growth_area}")

        # Add detected intent hint if provided
        detected_intent = context.get("detected_intent")
        if detected_intent and isinstance(detected_intent, str):
            hints.append(f"Detected user intent: {detected_intent}")

        # Add routing hints if provided
        routing_hint = context.get("routing_hint")
        if routing_hint and isinstance(routing_hint, str):
            hints.append(f"💡 {routing_hint}")

        # Format as hint block or return empty
        if hints:
            hint_text = "\n".join(hints)
            return f"\n**Reflection Journey Context:**\n{hint_text}\n"

        return ""
    
    async def create_action_plan(
        self,
        entry_id: str,
        responses: List[Dict[str, Any]],
        preferences: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """
        Create a comprehensive action plan from persona responses
        """
        plan_prompt = f"""
        Create a detailed action plan based on these coaching perspectives:
        
        {self._format_responses(responses)}
        
        User preferences: {preferences if preferences else 'None specified'}
        
        Generate 5-7 specific, measurable action steps that:
        1. Are immediately actionable
        2. Build on each other progressively
        3. Address the core issues identified
        4. Can be tracked and measured
        
        Return only the action steps as a numbered list.
        """
        
        try:
            result_text = await self._invoke_agent(
                self.orchestrator,
                session_prefix="orchestrator-action-plan",
                prompt=plan_prompt,
            )
            steps = result_text.strip().split("\n")
            # Clean up the steps
            steps = [
                step.strip().lstrip("0123456789. ")
                for step in steps
                if step.strip()
            ]
            if not steps:
                return {"steps": ["Please try creating your action plan again"]}
            return {"steps": steps[:7]}  # Limit to 7 steps
        except Exception as e:
            print(f"❌ Error creating action plan: {str(e)}")
            return {"steps": ["Please try creating your action plan again"]}