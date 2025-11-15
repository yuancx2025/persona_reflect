"""
Cognitive Behavioral Therapy (CBT) Tools

Provides structured CBT techniques for identifying cognitive distortions,
behavioral activation, and thought records using the ABC model.
"""

from typing import List, Dict, Any
import re


def identify_distortions(text: str) -> List[Dict[str, Any]]:
    """
    Identify cognitive distortions in user's thoughts or statements.

    Detects common thinking patterns that may contribute to emotional distress:
    - All-or-nothing thinking
    - Catastrophizing
    - Overgeneralization
    - Mental filtering
    - Jumping to conclusions
    - Emotional reasoning
    - Should/must statements
    - Labeling
    - Personalization

    Args:
        text: User's thoughts, self-talk, or description of their thinking

    Returns:
        List of detected distortions with explanation and reframe suggestions

    Example:
        >>> identify_distortions("I always fail at everything")
        [
            {
                "distortion": "all-or-nothing",
                "evidence": "always fail at everything",
                "explanation": "Using absolute terms like 'always' and 'everything'",
                "reframe": "I've struggled with some things, but I've also succeeded at others"
            },
            {
                "distortion": "overgeneralization",
                "evidence": "always fail",
                "explanation": "One experience applied to all situations",
                "reframe": "This specific situation didn't go as planned"
            }
        ]
    """
    text_lower = text.lower()
    distortions = []

    # All-or-nothing thinking patterns
    absolute_words = ['always', 'never', 'every', 'everyone', 'no one', 'everything', 'nothing', 'completely', 'totally']
    found_absolutes = [word for word in absolute_words if word in text_lower]
    if found_absolutes:
        distortions.append({
            "distortion": "all-or-nothing",
            "evidence": ", ".join(found_absolutes),
            "explanation": "Using absolute or extreme language suggests black-and-white thinking. Reality often exists in shades of gray.",
            "reframe": "Consider: Are there exceptions? Degrees? Nuances in this situation?",
            "severity": "moderate"
        })

    # Catastrophizing patterns
    catastrophe_words = ['disaster', 'terrible', 'awful', 'horrible', 'worst', 'ruined', 'catastrophe', 'end of the world']
    found_catastrophe = [word for word in catastrophe_words if word in text_lower]
    if found_catastrophe:
        distortions.append({
            "distortion": "catastrophizing",
            "evidence": ", ".join(found_catastrophe),
            "explanation": "Imagining the worst possible outcome or magnifying negative aspects.",
            "reframe": "What's the most realistic outcome? What would you tell a friend in this situation?",
            "severity": "high"
        })

    # Overgeneralization (single event → always)
    overgeneralization_patterns = [
        (r'(failed|messed up|didn\'t work).*(always|never)', 'One setback doesn\'t define all future outcomes'),
        (r'(can\'t|cannot).*(anything|everything)', 'Struggling with one thing doesn\'t mean inability in all areas')
    ]
    for pattern, reframe in overgeneralization_patterns:
        if re.search(pattern, text_lower):
            distortions.append({
                "distortion": "overgeneralization",
                "evidence": re.search(pattern, text_lower).group(0),
                "explanation": "Drawing broad conclusions from a single incident.",
                "reframe": reframe,
                "severity": "moderate"
            })
            break

    # Should/must statements
    should_words = ['should', 'must', 'ought to', 'have to', 'need to']
    found_shoulds = [word for word in should_words if word in text_lower]
    if found_shoulds and any(word in text_lower for word in ['but', "can't", "don't", "not"]):
        distortions.append({
            "distortion": "should-statements",
            "evidence": ", ".join(found_shoulds),
            "explanation": "Rigid rules about how you 'should' be can create unnecessary guilt and pressure.",
            "reframe": "Replace 'should' with 'I would prefer to' or 'It would be nice if'. This reduces shame.",
            "severity": "moderate"
        })

    # Labeling
    labeling_patterns = [
        r'i am (a|an)?\s*(failure|loser|idiot|stupid|worthless|useless)',
        r'i\'m (such a|just a|a total|a complete)?\s*(failure|loser|idiot|stupid|mess)'
    ]
    for pattern in labeling_patterns:
        match = re.search(pattern, text_lower)
        if match:
            distortions.append({
                "distortion": "labeling",
                "evidence": match.group(0),
                "explanation": "Defining yourself by a single characteristic or mistake is inaccurate and harmful.",
                "reframe": "You had a human experience. You are not defined by one moment, thought, or outcome.",
                "severity": "high"
            })
            break

    # Emotional reasoning
    emotion_reasoning_patterns = [
        r'i feel (like)?\s*(a failure|worthless|stupid)',
        r'(feel|feeling).*(so|therefore|means).*(i am|i\'m)'
    ]
    for pattern in emotion_reasoning_patterns:
        if re.search(pattern, text_lower):
            distortions.append({
                "distortion": "emotional-reasoning",
                "evidence": re.search(pattern, text_lower).group(0),
                "explanation": "Feelings are real, but they aren't facts. Feeling like a failure doesn't make it true.",
                "reframe": "Separate the feeling from the fact. Ask: What's the objective evidence?",
                "severity": "moderate"
            })
            break

    # Personalization
    personalization_patterns = ['my fault', 'because of me', 'i caused', 'i ruined', 'i\'m responsible for']
    found_personalization = [phrase for phrase in personalization_patterns if phrase in text_lower]
    if found_personalization:
        distortions.append({
            "distortion": "personalization",
            "evidence": ", ".join(found_personalization),
            "explanation": "Taking excessive responsibility for events outside your complete control.",
            "reframe": "What factors were truly within your control? What role did circumstances play?",
            "severity": "moderate"
        })

    # Mental filtering (focus on negative)
    negative_focus_words = ['only', 'just', 'nothing but', 'except']
    if any(word in text_lower for word in negative_focus_words) and any(word in text_lower for word in ['bad', 'wrong', 'negative', 'failed', 'problem']):
        distortions.append({
            "distortion": "mental-filtering",
            "evidence": "Focus appears exclusively on negative aspects",
            "explanation": "Filtering out positive aspects while magnifying the negative creates distorted view.",
            "reframe": "What's being overlooked? What went right or neutral, even in a small way?",
            "severity": "moderate"
        })

    # If no distortions detected, return helpful message
    if not distortions:
        return [{
            "distortion": "none-detected",
            "evidence": "",
            "explanation": "No obvious cognitive distortions detected in this statement. The thinking appears balanced.",
            "reframe": "This thought seems grounded in reality. Continue examining evidence objectively.",
            "severity": "none"
        }]

    return distortions


def behavioral_activation(task: str, minutes: int = 5) -> Dict[str, Any]:
    """
    Create a behavioral activation plan using the 5-minute rule.

    Behavioral activation combats avoidance and procrastination by breaking
    tasks into tiny, achievable first steps. The 5-minute commitment reduces
    the activation energy needed to start.

    Args:
        task: The task or activity the user is avoiding or struggling to start
        minutes: Duration of micro-action (default: 5 minutes)

    Returns:
        Structured action plan with micro-step, rationale, and success criteria

    Example:
        >>> behavioral_activation("start my research paper", minutes=5)
        {
            "original_task": "start my research paper",
            "micro_action": "Open a blank document and write the paper title and your name",
            "duration_minutes": 5,
            "rationale": "Starting is often the hardest part...",
            "success_criteria": "Document exists with title",
            "next_step_suggestion": "Spend 5 minutes writing 3 questions your paper will answer"
        }
    """
    # Generate specific micro-action based on task type
    task_lower = task.lower()

    # Detect task category
    if any(word in task_lower for word in ['write', 'paper', 'essay', 'report', 'email', 'document']):
        category = "writing"
        micro_action = f"Open a blank document and write just the title or first sentence. Nothing more for {minutes} minutes."
        success = "A document exists with at least one sentence written"
        next_step = "Spend 5 minutes brainstorming 3 key points you want to make"

    elif any(word in task_lower for word in ['study', 'read', 'learn', 'review', 'research']):
        category = "studying"
        micro_action = f"Gather materials (book, notes, laptop) and read just the first paragraph or section heading for {minutes} minutes."
        success = "Materials are in front of you and you've read something—even just a title"
        next_step = "Spend 5 minutes highlighting or noting one interesting thing you learned"

    elif any(word in task_lower for word in ['exercise', 'workout', 'run', 'gym', 'walk']):
        category = "exercise"
        micro_action = f"Put on workout clothes or shoes. That's it. You have permission to stop after {minutes} minutes."
        success = "You're wearing appropriate clothing for the activity"
        next_step = "Step outside or do 5 minutes of gentle movement (stretching, short walk)"

    elif any(word in task_lower for word in ['clean', 'organize', 'tidy', 'declutter']):
        category = "organizing"
        micro_action = f"Set a timer for {minutes} minutes and clear just one small surface (desk corner, nightstand, counter)."
        success = "One visible area is clearer than before"
        next_step = "Take a 2-minute break, then tackle one drawer or shelf for 5 minutes"

    elif any(word in task_lower for word in ['call', 'email', 'message', 'reach out', 'contact']):
        category = "communication"
        micro_action = f"Write or speak the first sentence of what you need to say. Don't send yet—just draft it for {minutes} minutes."
        success = "First sentence exists in draft form"
        next_step = "Add 1-2 more sentences to complete your main point"

    elif any(word in task_lower for word in ['apply', 'application', 'form', 'submit']):
        category = "application"
        micro_action = f"Open the application and read the first question. Fill in just your name and contact info for {minutes} minutes."
        success = "Basic information fields are completed"
        next_step = "Answer just the first substantive question in rough draft form"

    elif any(word in task_lower for word in ['project', 'assignment', 'work on']):
        category = "project"
        micro_action = f"Create a list of 3-5 tiny steps this project requires. Don't do them—just list them for {minutes} minutes."
        success = "A simple list exists breaking down the project"
        next_step = "Pick the smallest item on the list and spend 5 minutes on it"

    else:
        category = "general"
        micro_action = f"Spend exactly {minutes} minutes on the absolute smallest first step of '{task}'. Set a timer and give yourself permission to stop when it rings."
        success = f"You engaged with the task for {minutes} minutes, regardless of outcome"
        next_step = "Notice how you feel. If momentum built, continue. If not, take a break and try another 5 minutes later."

    return {
        "original_task": task,
        "category": category,
        "micro_action": micro_action,
        "duration_minutes": minutes,
        "rationale": f"Starting is often the hardest part. Committing to just {minutes} minutes removes the overwhelming feeling of tackling the entire task. Once you start, momentum often builds naturally. And if it doesn't? You still succeeded by taking action.",
        "success_criteria": success,
        "next_step_suggestion": next_step,
        "permission_to_stop": f"You have full permission to stop after {minutes} minutes. This isn't about finishing—it's about starting and building positive momentum.",
        "tip": "Set a visible timer. When it goes off, check in: Do you want to continue, or is this a good stopping point? Either choice is valid."
    }


def thought_record(situation: str, thoughts: List[str], emotions: List[str]) -> Dict[str, Any]:
    """
    Create a structured thought record using the ABC model (Cognitive Behavioral Therapy).

    The ABC Model:
    - A: Activating Event (situation that triggered thoughts/emotions)
    - B: Beliefs/Thoughts (what went through your mind)
    - C: Consequences (emotional and behavioral responses)

    This tool helps identify connections between thoughts and emotions, and
    prompts examination of evidence for/against automatic thoughts.

    Args:
        situation: Description of the activating event or situation
        thoughts: List of automatic thoughts or beliefs that arose
        emotions: List of emotions experienced (and optionally intensity 0-100)

    Returns:
        Structured thought record with ABC analysis and cognitive restructuring prompts

    Example:
        >>> thought_record(
        ...     situation="Didn't get a response to my job application",
        ...     thoughts=["I'm not qualified", "They rejected me", "I'll never get a job"],
        ...     emotions=["anxious (80%)", "hopeless (70%)", "disappointed (60%)"]
        ... )
    """
    # Parse emotions to separate emotion from intensity
    parsed_emotions = []
    for emotion in emotions:
        # Try to extract intensity if provided (e.g., "anxious (80%)" or "sad - 70")
        intensity_match = re.search(r'(\d+)\s*%?', emotion)
        if intensity_match:
            intensity = int(intensity_match.group(1))
            emotion_name = re.sub(r'[\(\)\-\d%\s]+$', '', emotion).strip()
        else:
            intensity = None
            emotion_name = emotion.strip()

        parsed_emotions.append({
            "emotion": emotion_name,
            "intensity": intensity,
            "intensity_description": _get_intensity_description(intensity) if intensity else "not specified"
        })

    # Analyze thoughts for potential distortions
    thought_analysis = []
    for thought in thoughts:
        distortions = identify_distortions(thought)
        thought_analysis.append({
            "thought": thought,
            "potential_distortions": [d["distortion"] for d in distortions if d["distortion"] != "none-detected"],
            "evidence_questions": _generate_evidence_questions(thought)
        })

    # Generate cognitive restructuring prompts
    restructuring_prompts = {
        "evidence_for": f"What evidence supports these thoughts? List specific, objective facts.",
        "evidence_against": f"What evidence contradicts these thoughts? What am I overlooking?",
        "alternative_thoughts": f"What are 2-3 alternative ways to interpret this situation?",
        "friend_perspective": f"What would you tell a close friend who had these exact thoughts?",
        "worst_best_realistic": f"What's the worst outcome? Best outcome? Most realistic outcome?",
        "action_steps": f"If the thoughts were 100% true, what could you do? If they're not true, what then?"
    }

    return {
        "abc_model": {
            "A_activating_event": {
                "situation": situation,
                "objective_facts": "What happened, stripped of interpretation?",
                "trigger_identified": bool(situation)
            },
            "B_beliefs_thoughts": {
                "automatic_thoughts": thoughts,
                "thought_analysis": thought_analysis,
                "core_belief_hint": "Do these thoughts reveal a deeper belief about yourself, others, or the world?"
            },
            "C_consequences": {
                "emotions": parsed_emotions,
                "emotional_summary": f"{len(parsed_emotions)} emotions identified",
                "behavioral_consequences": "How did these thoughts affect your actions or urges to act?",
                "physical_sensations": "What did you notice in your body? (tension, heart rate, etc.)"
            }
        },
        "cognitive_restructuring": restructuring_prompts,
        "balanced_thought_exercise": {
            "instruction": "After examining evidence, write a more balanced thought that:",
            "criteria": [
                "Acknowledges your feelings as valid",
                "Incorporates evidence from both sides",
                "Is more flexible (less absolute)",
                "Is compassionate toward yourself",
                "Focuses on what you can control"
            ],
            "example_structure": "'While I feel [emotion] about [situation], I recognize that [evidence]. A more balanced perspective is [alternative thought].'"
        },
        "re_rate_emotions": {
            "instruction": "After restructuring, re-rate emotion intensity (0-100)",
            "goal": "Notice if intensity decreased even slightly—this shows thoughts influence feelings"
        },
        "summary": f"Thought record captured: 1 situation, {len(thoughts)} thoughts, {len(emotions)} emotions. Use restructuring prompts to examine evidence and develop balanced perspectives."
    }


def _get_intensity_description(intensity: int) -> str:
    """Convert numerical intensity to descriptive label"""
    if intensity is None:
        return "not specified"
    elif intensity >= 80:
        return "very high"
    elif intensity >= 60:
        return "high"
    elif intensity >= 40:
        return "moderate"
    elif intensity >= 20:
        return "mild"
    else:
        return "minimal"


def _generate_evidence_questions(thought: str) -> List[str]:
    """Generate specific evidence-examination questions for a thought"""
    questions = [
        f"What concrete facts support the thought: '{thought}'?",
        f"What facts contradict or don't fit with: '{thought}'?",
        "Am I confusing a thought with a fact?",
        "Am I jumping to conclusions without all the information?"
    ]

    # Add thought-specific questions
    thought_lower = thought.lower()
    if any(word in thought_lower for word in ['always', 'never', 'every']):
        questions.append("Are there any exceptions to this absolute statement?")
    if any(word in thought_lower for word in ['should', 'must', 'have to']):
        questions.append("Who made this rule? Is it flexible? What happens if it's not followed?")
    if 'i am' in thought_lower or "i'm" in thought_lower:
        questions.append("Am I defining myself by a single characteristic or moment?")

    return questions
