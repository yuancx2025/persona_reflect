"""
Emotional Support and Resource Tools

Provides compassionate reframing, grounding techniques, mental health resources,
and self-compassion practices for emotional support.
"""

from typing import List, Dict, Any


def reframe(negative_self_talk: str) -> str:
    """
    Offer compassionate reframing of harsh self-talk.

    Uses principles from self-compassion research (Kristin Neff) and
    cognitive reframing to transform self-criticism into self-kindness
    while maintaining accountability and growth.

    Args:
        negative_self_talk: The critical or harsh statement about oneself

    Returns:
        Compassionate reframe with validation and perspective shift

    Example:
        >>> reframe("I'm such an idiot for making that mistake")
        "Making a mistake doesn't make you an idiot—it makes you human..."
    """
    # Detect patterns in the self-talk
    statement_lower = negative_self_talk.lower()

    # Initialize reframe components
    validation = ""
    perspective = ""
    reframe_statement = ""

    # Pattern: "I'm a [negative label]" or "I'm [negative adjective]"
    if any(phrase in statement_lower for phrase in ["i'm a failure", "i'm an idiot", "i'm stupid", "i'm worthless", "i'm a mess", "i'm useless"]):
        validation = "I hear that you're being really hard on yourself right now. That pain is real."
        perspective = "And... having a difficult moment—or even many difficult moments—doesn't define who you are as a person."
        reframe_statement = "What if we separated the behavior from your identity? Instead of 'I am a failure,' what about 'I'm struggling with something challenging right now, and that's okay. I'm learning.'"

    # Pattern: "I always [negative behavior]" or "I never [positive behavior]"
    elif any(word in statement_lower for word in ["always", "never"]) and any(word in statement_lower for word in ["fail", "mess up", "screw up", "wrong"]):
        validation = "It feels like this pattern keeps happening, and that's incredibly frustrating."
        perspective = "Words like 'always' and 'never' are heavy. They erase all the times things went differently."
        reframe_statement = "What if we got specific? Instead of 'I always fail,' try 'This particular situation didn't go as I hoped. What can I learn from it?' That opens possibilities instead of closing them."

    # Pattern: "I should have [done something]" or "I shouldn't have [done something]"
    elif any(phrase in statement_lower for phrase in ["should have", "shouldn't have", "should've", "shouldn't've"]):
        validation = "Hindsight can be painful. It's hard when we wish we'd done something differently."
        perspective = "But you made the best decision you could with the information, resources, and emotional state you had in that moment."
        reframe_statement = "Instead of 'I should have...', what if you said: 'Next time, I'd like to try...' or 'I'm learning that...' This shifts from shame to growth."

    # Pattern: "I can't [do something]"
    elif "can't" in statement_lower or "cannot" in statement_lower:
        validation = "Feeling stuck or incapable is a heavy feeling to carry."
        perspective = "Often 'I can't' actually means 'I don't know how yet' or 'This feels too hard right now with the resources I have.'"
        reframe_statement = "What if we changed 'I can't' to 'I haven't figured out how yet' or 'This is challenging, and I might need support'? That leaves room for possibility."

    # Pattern: Catastrophizing
    elif any(word in statement_lower for word in ["ruined", "disaster", "terrible", "worst", "horrible"]):
        validation = "When things feel catastrophic, it's because they really matter to you. That's not nothing."
        perspective = "And when we're overwhelmed, our brain sometimes exaggerates the danger. It's trying to protect you, but it might be overestimating the threat."
        reframe_statement = "Ask yourself: What's the actual impact? In a week, a month, a year—how will this look? And even if it's genuinely difficult, does that mean it's *permanently* ruined, or just hard right now?"

    # Pattern: Comparison to others
    elif any(phrase in statement_lower for phrase in ["everyone else", "other people", "others can", "they can"]):
        validation = "Comparison is so painful, especially when it feels like everyone else has it figured out."
        perspective = "But you're comparing your messy inside to everyone else's curated outside. You don't see their struggles."
        reframe_statement = "What if instead of comparing, you asked: 'Am I making progress compared to where *I* was last month, last year?' That's the only comparison that truly matters."

    # Pattern: Perfectionism
    elif any(phrase in statement_lower for phrase in ["not good enough", "not enough", "should be better", "have to be perfect"]):
        validation = "The drive to be 'good enough' often comes from wanting to be loved, safe, valued. That's deeply human."
        perspective = "But perfectionism is an impossible standard that steals your joy and keeps you perpetually dissatisfied."
        reframe_statement = "What if 'good enough' was actually enough? What if progress, effort, and showing up imperfectly counted? Because they do."

    # Generic fallback
    else:
        validation = "The way you're talking to yourself sounds painful. You deserve kindness, especially from yourself."
        perspective = "Self-criticism might feel like it's motivating you, but research shows it usually does the opposite—it increases shame, anxiety, and paralysis."
        reframe_statement = "What would you say to a dear friend who came to you with this exact struggle? Try offering yourself that same warmth and understanding."

    # Construct the full reframe
    full_reframe = f"""**Reframing: "{negative_self_talk}"**

💙 **Validation:** {validation}

🔄 **Perspective Shift:** {perspective}

🌱 **Compassionate Reframe:** {reframe_statement}

---

**Remember:** Self-compassion isn't about lowering standards or making excuses. It's about treating yourself with the same kindness you'd offer someone you care about, while still encouraging growth.

**Try this:** Place your hand on your heart. Take a breath. Say out loud or in your mind:
*"I'm struggling right now, and that's okay. I'm doing my best. I deserve kindness, especially from myself."*
"""

    return full_reframe


def grounding_exercise(duration: int = 3) -> Dict[str, Any]:
    """
    Quick centering practice using breath and body awareness.

    Note: This is a simplified version optimized for the empathetic friend persona.
    For full 5-4-3-2-1 sensory grounding, see mindfulness_tools.grounding_exercise().

    Args:
        duration: Duration in minutes (1-5 recommended)

    Returns:
        Simple grounding exercise instructions

    Example:
        >>> grounding_exercise(duration=2)
        {
            "duration_minutes": 2,
            "technique": "Breath & Body Anchor",
            ...
        }
    """
    return {
        "duration_minutes": duration,
        "technique": "Breath & Body Anchor",
        "purpose": "Come back to the present moment when you're overwhelmed, anxious, or feeling disconnected.",
        "instructions": {
            "step_1": {
                "action": "Find your breath",
                "details": "Place one hand on your chest or belly. Feel it rise and fall. You don't have to change your breathing—just notice it.",
                "duration": f"{duration * 0.3:.0f} seconds"
            },
            "step_2": {
                "action": "Feel your body",
                "details": "Notice where your body touches the ground, chair, or surface. Press your feet into the floor. Feel the support beneath you.",
                "duration": f"{duration * 0.3:.0f} seconds"
            },
            "step_3": {
                "action": "Soften one thing",
                "details": "Check: Is your jaw clenched? Shoulders tight? Fists closed? Consciously soften just one place of tension.",
                "duration": f"{duration * 0.2:.0f} seconds"
            },
            "step_4": {
                "action": "Say something kind",
                "details": "Silently or aloud, say: 'I'm here. I'm okay. This moment is manageable.' Repeat as needed.",
                "duration": f"{duration * 0.2:.0f} seconds"
            }
        },
        "simple_version": f"""**{duration}-Minute Grounding**

1. **Breathe**: Hand on chest. Feel your breath.
2. **Ground**: Feet on floor. Feel the support.
3. **Soften**: Relax your jaw, shoulders, or hands.
4. **Affirm**: "I'm here. I'm okay. This will pass."

You can do this anywhere, anytime.""",
        "when_to_use": [
            "Before or during a panic attack",
            "When emotions feel too big",
            "When thoughts are racing",
            "When you feel disconnected or numb",
            "Before a difficult conversation or event"
        ],
        "tip": f"Set a gentle timer for {duration} minute(s). Give yourself permission to just *be* for this time—no fixing, no solving, just grounding."
    }


def resources(topic: str = "general") -> List[Dict[str, Any]]:
    """
    Provide curated mental health resources based on topic.

    Offers crisis lines, therapy directories, support groups, educational
    resources, and apps for various mental health concerns.

    Args:
        topic: Resource category (e.g., "crisis", "therapy", "anxiety", "depression", "general")

    Returns:
        List of relevant resources with descriptions and contact info

    Example:
        >>> resources(topic="crisis")
        [{"name": "988 Suicide & Crisis Lifeline", ...}, ...]
    """
    topic_lower = topic.lower()

    # Crisis resources (always included if topic is crisis or high-risk keywords)
    crisis_resources = [
        {
            "name": "988 Suicide & Crisis Lifeline",
            "type": "crisis_line",
            "contact": "Call or text 988",
            "availability": "24/7",
            "description": "Free, confidential support for people in distress, prevention and crisis resources. Available in English and Spanish.",
            "url": "https://988lifeline.org"
        },
        {
            "name": "Crisis Text Line",
            "type": "crisis_line",
            "contact": "Text HOME to 741741",
            "availability": "24/7",
            "description": "Free, 24/7 crisis support via text. Trained crisis counselors respond to help you move from a hot moment to a cool calm.",
            "url": "https://www.crisistextline.org"
        },
        {
            "name": "Trevor Project (LGBTQ Youth)",
            "type": "crisis_line",
            "contact": "Call 1-866-488-7386 or text START to 678678",
            "availability": "24/7",
            "description": "Crisis intervention and suicide prevention for LGBTQ young people under 25.",
            "url": "https://www.thetrevorproject.org"
        },
        {
            "name": "SAMHSA National Helpline",
            "type": "crisis_line",
            "contact": "1-800-662-4357",
            "availability": "24/7",
            "description": "Free, confidential treatment referral and information service for substance use and mental health issues.",
            "url": "https://www.samhsa.gov/find-help/national-helpline"
        }
    ]

    # Therapy and professional help
    therapy_resources = [
        {
            "name": "Psychology Today Therapist Directory",
            "type": "therapy_finder",
            "description": "Search for therapists by location, insurance, specialty, and therapy type. Includes profiles and contact info.",
            "url": "https://www.psychologytoday.com/us/therapists"
        },
        {
            "name": "Open Path Collective",
            "type": "affordable_therapy",
            "description": "Network of therapists offering sessions for $30-$80 for those without insurance or with high deductibles.",
            "url": "https://openpathcollective.org"
        },
        {
            "name": "BetterHelp / Talkspace",
            "type": "online_therapy",
            "description": "Online therapy platforms with licensed therapists. Subscription-based, often more affordable than traditional therapy.",
            "note": "Research each platform's reviews and policies before committing."
        },
        {
            "name": "NAMI (National Alliance on Mental Illness)",
            "type": "support_advocacy",
            "description": "Free education programs, support groups, and advocacy. Helpline: 1-800-950-NAMI (6264)",
            "url": "https://www.nami.org"
        }
    ]

    # Anxiety-specific resources
    anxiety_resources = [
        {
            "name": "Anxiety and Depression Association of America (ADAA)",
            "type": "educational",
            "description": "Evidence-based information, therapist finder, free webinars, and peer-to-peer support community.",
            "url": "https://adaa.org"
        },
        {
            "name": "DARE App",
            "type": "app",
            "description": "App for panic attacks, anxiety, and phobias. Based on exposure therapy and CBT principles.",
            "platform": "iOS/Android"
        },
        {
            "name": "Headspace / Calm",
            "type": "app",
            "description": "Meditation and mindfulness apps with anxiety-specific programs, sleep stories, and breathing exercises.",
            "platform": "iOS/Android"
        }
    ]

    # Depression-specific resources
    depression_resources = [
        {
            "name": "Depression and Bipolar Support Alliance (DBSA)",
            "type": "support_groups",
            "description": "Peer-led support groups (in-person and online) for depression and bipolar disorder.",
            "url": "https://www.dbsalliance.org"
        },
        {
            "name": "7 Cups",
            "type": "peer_support",
            "description": "Free emotional support through trained listeners. Also offers affordable online therapy.",
            "url": "https://www.7cups.com"
        }
    ]

    # Self-help and educational resources
    general_resources = [
        {
            "name": "MindTools",
            "type": "self_help",
            "description": "Free tools for stress management, resilience, productivity, and emotional intelligence.",
            "url": "https://www.mindtools.com"
        },
        {
            "name": "Therapist Aid Worksheets",
            "type": "worksheets",
            "description": "Free, printable therapy worksheets for CBT, DBT, mindfulness, and more.",
            "url": "https://www.therapistaid.com"
        },
        {
            "name": "Self-Compassion.org",
            "type": "educational",
            "description": "Dr. Kristin Neff's research-based self-compassion exercises, meditations, and resources.",
            "url": "https://self-compassion.org"
        }
    ]

    # Student-specific resources
    student_resources = [
        {
            "name": "University Counseling Center",
            "type": "campus_resource",
            "description": "Most colleges offer free or low-cost counseling. Check your school's student health services.",
            "note": "Often includes group therapy, workshops, and crisis support."
        },
        {
            "name": "JED Foundation",
            "type": "student_mental_health",
            "description": "Mental health resources specifically for teens and young adults, including campus programs.",
            "url": "https://jedfoundation.org"
        }
    ]

    # Build response based on topic
    response = []

    if any(keyword in topic_lower for keyword in ["crisis", "suicide", "emergency", "urgent", "help now"]):
        response.extend(crisis_resources)
        response.append({
            "name": "Emergency Services",
            "type": "emergency",
            "contact": "Call 911",
            "description": "For immediate medical or psychiatric emergencies, call 911 or go to your nearest emergency room.",
            "note": "If you're in immediate danger or having a medical emergency, call 911."
        })

    if "therapy" in topic_lower or "therapist" in topic_lower or "counseling" in topic_lower:
        response.extend(therapy_resources)

    if "anxiety" in topic_lower or "panic" in topic_lower:
        response.extend(anxiety_resources)

    if "depression" in topic_lower or "depressed" in topic_lower:
        response.extend(depression_resources)

    if "student" in topic_lower or "college" in topic_lower or "school" in topic_lower:
        response.extend(student_resources)

    # If general or no specific matches, provide a well-rounded selection
    if not response or topic_lower == "general":
        response = [
            crisis_resources[0],  # 988 Lifeline
            crisis_resources[1],  # Crisis Text Line
            therapy_resources[0],  # Psychology Today
            therapy_resources[1],  # Open Path
            therapy_resources[3],  # NAMI
            general_resources[2],  # Self-compassion.org
        ]

    # Add important disclaimer
    disclaimer = {
        "type": "disclaimer",
        "important": "⚠️ Important Notes",
        "notes": [
            "These resources are for informational purposes and do not replace professional medical advice.",
            "If you're in immediate danger, call 911 or go to your nearest emergency room.",
            "Many resources offer sliding scale fees or free services—don't let cost prevent you from reaching out.",
            "Finding the right therapist or resource may take time. It's okay to try a few before finding the right fit."
        ]
    }

    return response + [disclaimer]


def self_compassion_prompt() -> str:
    """
    Provide a self-compassion template based on Dr. Kristin Neff's research.

    Self-compassion has three core components:
    1. Self-kindness (vs. self-judgment)
    2. Common humanity (vs. isolation)
    3. Mindfulness (vs. over-identification)

    Returns:
        Guided self-compassion exercise

    Example:
        >>> print(self_compassion_prompt())
        "**Self-Compassion Practice**..."
    """
    return """**Self-Compassion Practice** 💙

Based on Dr. Kristin Neff's research, self-compassion involves treating yourself with the same kindness you'd offer a good friend.

---

**Right now, take a moment to acknowledge:**

**1️⃣ Mindfulness: Name What's Hard**
"Right now, I'm struggling with _______________."

(Just name it. Don't judge it or fix it yet. Just acknowledge: This is difficult.)

---

**2️⃣ Common Humanity: You're Not Alone**
"This is a moment of suffering. Suffering is a part of life. I'm not alone in this—many people have felt this way."

(Your struggle doesn't mean you're broken or uniquely flawed. It means you're human.)

---

**3️⃣ Self-Kindness: Offer Yourself Warmth**
Place your hand on your heart (or another soothing place—your cheek, your belly). Feel the warmth of your own touch.

Now, say to yourself:
- "May I be kind to myself in this moment."
- "May I give myself the compassion I need."
- "May I accept myself as I am right now."

Or, use your own words. What would you say to a dear friend going through this exact thing? Say that to yourself.

---

**Alternative Phrases (choose what resonates):**
- "I'm doing the best I can with what I have right now."
- "It's okay to struggle. I don't have to be perfect."
- "I deserve kindness, especially from myself."
- "This is hard, and I'm allowed to feel this way."
- "I'm learning. I'm growing. I'm enough."

---

**Why This Matters:**
Research shows self-compassion is linked to:
- Greater emotional resilience
- Lower anxiety and depression
- More motivation to change and grow (not less!)
- Better ability to cope with failure and setbacks

Self-criticism might *feel* motivating, but it actually undermines you. Self-compassion is the foundation for real, sustainable growth.

---

**Practice:** Try using this script once a day for a week, especially in difficult moments. Notice how it feels different from self-criticism or self-pity. You're not lowering standards—you're meeting yourself with humanity.

**Further exploration:** Visit https://self-compassion.org for guided meditations, exercises, and research."""
