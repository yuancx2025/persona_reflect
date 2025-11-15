"""
Mindfulness and Grounding Tools

Provides evidence-based mindfulness techniques including breathwork,
body scans, values clarification, and grounding exercises.
"""

from typing import Dict, Any, List


def one_breath_instruction() -> str:
    """
    Provide immediate, simple breathing instruction for moments of overwhelm.

    This is the fastest intervention—one conscious breath can activate
    the parasympathetic nervous system and create a pause before reacting.

    Returns:
        Clear, calm breathing instruction

    Example:
        >>> print(one_breath_instruction())
        "Right now, take one slow breath with me..."
    """
    return """**One Breath Practice** 🌬️

Right now, wherever you are:

1. **Pause** what you're doing
2. **Inhale** slowly through your nose for 4 counts (1...2...3...4)
3. **Hold** gently for 2 counts (1...2)
4. **Exhale** slowly through your mouth for 6 counts (1...2...3...4...5...6)

That's it. One breath.

Notice: Did anything shift, even slightly? Your shoulders? Your jaw? Your racing thoughts?

You can return to this breath any time—in a meeting, before a difficult conversation, when emotions spike. One breath is always available.

**If you'd like to continue:** Repeat this pattern 3-5 more times, letting each exhale be a little longer and softer than the last."""


def body_scan(duration: int = 5) -> Dict[str, Any]:
    """
    Generate a guided body scan meditation script.

    Body scans help reconnect with physical sensations, interrupt rumination,
    and release held tension. Duration is flexible based on available time.

    Args:
        duration: Length of practice in minutes (3, 5, or 10 recommended)

    Returns:
        Structured script with timed sections and guidance

    Example:
        >>> body_scan(duration=5)
        {
            "duration_minutes": 5,
            "preparation": "Find a comfortable position...",
            "script": [...],
            ...
        }
    """
    # Adjust detail based on duration
    if duration <= 3:
        body_parts = ["feet", "belly", "chest", "shoulders", "face"]
        seconds_per_part = 30
        detail_level = "brief"
    elif duration <= 7:
        body_parts = ["feet and legs", "pelvis and lower back", "belly and chest", "arms and hands", "shoulders and neck", "face and head"]
        seconds_per_part = 45
        detail_level = "moderate"
    else:
        body_parts = ["toes and feet", "ankles and calves", "knees and thighs", "pelvis and hips", "lower back and belly", "chest and upper back", "shoulders", "arms and hands", "neck and throat", "jaw and face", "head and scalp"]
        seconds_per_part = 50
        detail_level = "detailed"

    script_sections = []
    for i, body_part in enumerate(body_parts):
        script_sections.append({
            "body_area": body_part,
            "approximate_time": f"{i * seconds_per_part // 60}:{(i * seconds_per_part) % 60:02d}",
            "guidance": f"Bring gentle awareness to your {body_part}. Notice any sensations—warmth, coolness, tingling, tension, or maybe nothing at all. No need to change anything. Just notice, and breathe.",
            "duration_seconds": seconds_per_part
        })

    return {
        "practice_name": "Body Scan Meditation",
        "duration_minutes": duration,
        "detail_level": detail_level,
        "preparation": {
            "instruction": "Find a comfortable position—sitting or lying down. You can close your eyes or soften your gaze downward.",
            "initial_breaths": "Take 3 deep breaths to arrive in this moment. Let each exhale release a little tension.",
            "intention": "The intention is not to relax (though that may happen). It's simply to notice what's present in your body without judgment."
        },
        "script": script_sections,
        "closing": {
            "instruction": "Gradually expand your awareness to your whole body. Notice your body as one complete system, breathing and alive.",
            "integration": "Take 3 more deep breaths. When you're ready, gently wiggle fingers and toes, and slowly open your eyes.",
            "reflection": "Notice: How do you feel now compared to when you started? Any areas of tension released? Any insights?"
        },
        "tips": [
            "If your mind wanders (it will), gently guide it back to the body area you're focusing on",
            "There's no 'perfect' way to feel. Boredom, restlessness, sleepiness—all are welcome",
            "You can speed up or slow down as needed. This is your practice",
            f"Consider setting a gentle timer for {duration} minutes"
        ],
        "adaptations": {
            "if_overwhelmed": "If scanning feels overwhelming, just focus on your feet or hands—one small area of grounding.",
            "if_sleepy": "Try this sitting up with eyes open if you notice yourself getting drowsy.",
            "if_restless": "It's okay to adjust your position. Mindfulness includes noticing the urge to move."
        }
    }


def values_checkin() -> str:
    """
    Provide reflective questions to help clarify personal values.

    Values clarification helps ground decisions in what truly matters,
    especially useful when feeling lost, stuck, or facing difficult choices.

    Based on Acceptance and Commitment Therapy (ACT) values work.

    Returns:
        Structured values reflection prompts

    Example:
        >>> print(values_checkin())
        "**Values Check-In**\n\nValues are like a compass..."
    """
    return """**Values Check-In: What Matters Most?** 🧭

Values are like a compass—they point toward what gives your life meaning, even when the path is hard.

**Take a few minutes to reflect:**

**1. Imagine Your 80th Birthday**
People who love you are sharing what they appreciate about you. What do you hope they'd say?
- About how you treated others?
- About what you stood for?
- About how you handled challenges?

**2. What Makes You Come Alive?**
Think of a moment when you felt most *yourself*—engaged, energized, purposeful.
- What were you doing?
- Who were you with (or were you alone)?
- What value was being honored in that moment? (e.g., creativity, connection, growth, helping others, learning, adventure)

**3. Your Core Values (Choose 3-5)**
Which of these resonate most deeply right now?

- **Connection/Love**: Deep relationships, intimacy, belonging
- **Growth**: Learning, evolving, self-improvement
- **Creativity**: Self-expression, making things, originality
- **Contribution**: Helping others, making a difference, service
- **Adventure**: New experiences, exploration, spontaneity
- **Health/Vitality**: Physical well-being, energy, body respect
- **Authenticity**: Being genuine, honoring your truth
- **Achievement**: Accomplishing goals, mastery, competence
- **Peace**: Inner calm, balance, simplicity
- **Justice**: Fairness, equality, standing up for what's right
- **Spirituality**: Connection to something larger, meaning, faith
- **Independence**: Autonomy, freedom, self-reliance
- **Fun/Play**: Joy, humor, lightness, enjoyment

**4. The Gap Check**
Looking at your top 3-5 values:
- Which ones are you currently living in alignment with?
- Which ones have you drifted away from?
- What's one small action this week that would honor a neglected value?

**Remember:**
- Values aren't goals (they're never "done")
- You don't have to be perfect—just take steps in the valued direction
- It's okay if values shift over time or life seasons
- Knowing your values helps you make decisions when you feel stuck

**Reflection:** If you were 10% more aligned with your top value this week, what would you be doing differently?"""


def grounding_exercise(duration: int = 3) -> Dict[str, Any]:
    """
    Generate a 5-4-3-2-1 grounding exercise for anxiety, dissociation, or overwhelm.

    This sensory awareness technique helps interrupt rumination, flashbacks,
    or anxiety spirals by anchoring attention in the present moment through
    the five senses.

    Args:
        duration: Target duration in minutes (3-5 recommended)

    Returns:
        Structured grounding exercise with sensory prompts

    Example:
        >>> grounding_exercise(duration=3)
        {
            "technique": "5-4-3-2-1 Sensory Grounding",
            "purpose": "Anchor yourself in the present moment...",
            ...
        }
    """
    # Calculate pacing based on duration
    seconds_per_sense = (duration * 60) // 15  # Total 15 items to notice (5+4+3+2+1)

    return {
        "technique": "5-4-3-2-1 Sensory Grounding",
        "purpose": "Anchor yourself in the present moment using your five senses. Helpful for anxiety, panic, dissociation, or when thoughts feel overwhelming.",
        "duration_minutes": duration,
        "estimated_seconds_per_item": seconds_per_sense,
        "preparation": {
            "instruction": "Sit or stand comfortably. Take one deep breath. You're going to use your senses to connect with right here, right now.",
            "reminder": "There are no wrong answers. Just notice what's present without judgment."
        },
        "exercise": {
            "sight": {
                "count": 5,
                "prompt": "**5 things you can SEE** 👁️\nLook around you. Name 5 things you can see right now. Say them out loud or in your mind.",
                "examples": "The corner of a book. A shadow on the wall. The color of your shirt. A crack in the ceiling. The shape of a doorway.",
                "tip": "Really look. Notice small details you usually overlook—a texture, a color variation, the way light hits something."
            },
            "touch": {
                "count": 4,
                "prompt": "**4 things you can TOUCH** ✋\nNotice 4 physical sensations. You can touch objects or notice what's already touching you.",
                "examples": "Your feet on the floor. The chair supporting your back. The temperature of your hands. The fabric of your clothing. The smoothness or roughness of a nearby surface.",
                "tip": "Press your feet firmly into the ground. This is especially grounding. Notice temperature, texture, pressure."
            },
            "hearing": {
                "count": 3,
                "prompt": "**3 things you can HEAR** 👂\nPause and listen. What sounds are present, even faint ones?",
                "examples": "Your own breathing. A clock ticking. Traffic outside. The hum of electronics. Birdsong. Silence (yes, silence has a quality).",
                "tip": "Close your eyes for a moment if it helps you focus on sounds. Notice sounds both near and far."
            },
            "smell": {
                "count": 2,
                "prompt": "**2 things you can SMELL** 👃\nWhat do you notice in the air? If nothing obvious, that's okay—notice that.",
                "examples": "Coffee. Fresh air. Your own skin or clothing. Soap. A neutral 'indoor' smell. You can also imagine a pleasant smell if nothing is present.",
                "tip": "If you can't smell anything where you are, imagine a scent you love—ocean air, fresh bread, rain. Your brain will respond."
            },
            "taste": {
                "count": 1,
                "prompt": "**1 thing you can TASTE** 👅\nWhat do you taste in your mouth right now? Or what's a taste you enjoy?",
                "examples": "The aftertaste of a recent drink. Toothpaste. Your own mouth's neutral taste. Imagine the taste of something you love—chocolate, an orange, mint.",
                "tip": "If nothing is present, imagine biting into a lemon. Your mouth will likely react—that's your senses working!"
            }
        },
        "closing": {
            "instruction": "Take one more deep breath. You just connected with 15 different present-moment experiences.",
            "check_in": "Notice: Are you more present in your body and environment now? Even a slight shift is success.",
            "repeat": "You can repeat this exercise anytime, anywhere. Some people do it multiple times a day during stressful periods."
        },
        "variations": [
            "If 5-4-3-2-1 feels too long, try 3-2-1 (3 things you see, 2 you hear, 1 you feel)",
            "If you're very overwhelmed, just do '5 things I can see' and repeat it",
            "Combine with walking: Notice 5 things you see while walking slowly",
            "Do this with someone else—take turns naming what you notice"
        ],
        "when_to_use": [
            "Before a stressful event (presentation, difficult conversation, medical appointment)",
            "During a panic attack or high anxiety",
            "When you feel disconnected from your body or surroundings",
            "After a triggering memory or flashback",
            "Anytime you want to interrupt rumination and return to the present"
        ],
        "summary": f"In {duration} minutes, you anchored yourself with 5+4+3+2+1 = 15 present-moment observations. Your nervous system just received the message: 'I am here, I am safe, I am present.'"
    }


# Additional helper for quick grounding variants
def quick_grounding_options() -> List[Dict[str, str]]:
    """
    Provide a menu of quick grounding techniques beyond 5-4-3-2-1.

    Returns:
        List of grounding options with brief descriptions
    """
    return [
        {
            "name": "Cold Water Splash",
            "duration": "30 seconds",
            "instruction": "Splash cold water on your face or hold ice cubes. The temperature shock activates your dive reflex and interrupts panic.",
            "intensity": "high"
        },
        {
            "name": "Feet on Floor",
            "duration": "1 minute",
            "instruction": "Press your feet firmly into the ground. Notice the pressure, the support. Stand and shift your weight from foot to foot if needed.",
            "intensity": "low"
        },
        {
            "name": "Name Categories",
            "duration": "2-3 minutes",
            "instruction": "Pick a category (animals, cities, foods) and name as many as you can. This engages your thinking brain and interrupts emotion spirals.",
            "intensity": "medium"
        },
        {
            "name": "Hand on Heart",
            "duration": "2 minutes",
            "instruction": "Place your hand on your heart. Feel it beating. Say: 'I am here. I am safe. This feeling will pass.' Repeat slowly.",
            "intensity": "low"
        },
        {
            "name": "Butterfly Hug",
            "duration": "1-2 minutes",
            "instruction": "Cross your arms and place hands on opposite shoulders. Gently tap alternating hands. This bilateral stimulation is calming.",
            "intensity": "medium"
        },
        {
            "name": "Strong Muscle Tension",
            "duration": "2 minutes",
            "instruction": "Tense all your muscles hard for 10 seconds, then release completely. Repeat 3 times. This releases physical anxiety.",
            "intensity": "high"
        }
    ]
