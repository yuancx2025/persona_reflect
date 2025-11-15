"""
Tools package for PersonaReflect agents

Exports specialized tool sets for each persona:
- TOOLS_RATIONAL: Calendar and scheduling tools for Alex (Rational Analyst)
- TOOLS_CBT: Cognitive-behavioral therapy tools for Dr. Chen
- TOOLS_MINDFUL: Mindfulness and grounding tools for Sage
- TOOLS_SUPPORT: Emotional support and resource tools for Maya
"""

# Calendar tools
from .calendar_tools import list_events, find_free_time, create_block, CALENDAR_TOOL_FUNCS

# CBT tools
from .cbt_tools import identify_distortions, behavioral_activation, thought_record

# Mindfulness tools
from .mindfulness_tools import (
    one_breath_instruction,
    body_scan,
    values_checkin,
    grounding_exercise as mindful_grounding
)

# Support tools
from .support_tools import (
    reframe,
    grounding_exercise as support_grounding,
    resources,
    self_compassion_prompt
)

# Persona-specific tool lists
TOOLS_RATIONAL = [list_events, find_free_time, create_block]

TOOLS_CBT = [identify_distortions, behavioral_activation, thought_record]

TOOLS_MINDFUL = [
    one_breath_instruction,
    body_scan,
    values_checkin,
    mindful_grounding
]

TOOLS_SUPPORT = [
    reframe,
    support_grounding,
    resources,
    self_compassion_prompt
]

# Backward compatibility
CALENDAR_TOOL_FUNCS = TOOLS_RATIONAL

__all__ = [
    # Legacy export
    "CALENDAR_TOOL_FUNCS",
    # Persona-specific tool lists
    "TOOLS_RATIONAL",
    "TOOLS_CBT",
    "TOOLS_MINDFUL",
    "TOOLS_SUPPORT",
    # Individual calendar tools
    "list_events",
    "find_free_time",
    "create_block",
    # Individual CBT tools
    "identify_distortions",
    "behavioral_activation",
    "thought_record",
    # Individual mindfulness tools
    "one_breath_instruction",
    "body_scan",
    "values_checkin",
    # Individual support tools
    "reframe",
    "resources",
    "self_compassion_prompt",
]
