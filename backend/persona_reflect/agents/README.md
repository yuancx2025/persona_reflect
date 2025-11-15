# PersonaReflect Agents & Tools 🎭

**Complete reference for the four AI personas and their specialized toolsets.**

---

## 📋 Overview

PersonaReflect uses **4 specialized AI agents**, each with unique perspectives and **15+ evidence-based tools**. Each persona is powered by Google's Gemini via the ADK framework and equipped with therapeutic techniques from CBT, ACT, MBSR, and self-compassion research.

### Quick Reference

| Persona | Icon | Specialty | Tools | File |
|---------|------|-----------|-------|------|
| **Dr. Chen** | 🧠 | Cognitive-Behavioral Therapy | 3 CBT tools | `cognitive_behavioral.py` |
| **Maya** | 💙 | Empathetic Support | 4 emotional support tools | `empathetic_friend.py` |
| **Alex** | 📊 | Rational Analysis & Scheduling | 3 calendar tools | `rational_analyst.py` |
| **Sage** | 🧘 | Mindfulness & Grounding | 4 mindfulness tools | `mindfulness_mentor.py` |

**Orchestrator:** `orchestrator.py` - Coordinates all agents using Google ADK

---

## 🧠 Dr. Chen - Cognitive-Behavioral Therapy Coach

**File:** `cognitive_behavioral.py`  
**Approach:** Evidence-based CBT techniques for identifying and restructuring unhelpful thought patterns  
**Tools:** `TOOLS_CBT` + `TOOLS_RATIONAL`

### Personality & Style
- Professional yet warm clinical psychologist
- Structured, solution-focused approach
- Uses Socratic questioning to guide insight
- Balances validation with cognitive challenges

### Tools (3)

#### 1. `identify_distortions(text: str)` → List[Dict]
**Purpose:** Detect cognitive distortions in user's thoughts

**Identifies 9+ distortion types:**
- All-or-nothing thinking (black & white, no gray area)
- Catastrophizing (imagining worst outcomes)
- Overgeneralization (single event → always true)
- Mental filtering (ignoring positives, magnifying negatives)
- Should statements (rigid rules causing guilt)
- Labeling (defining self by single trait)
- Emotional reasoning (feelings = facts)
- Personalization (taking blame for external events)
- Jumping to conclusions (mind reading, fortune telling)

**Output:** List of detected distortions with:
- Evidence from the text
- Explanation of the distortion
- Suggested reframe
- Severity level (low/moderate/high)

**Example:**
```python
identify_distortions("I always fail at everything")
# Returns:
# [
#   {
#     "distortion": "all-or-nothing",
#     "evidence": "always, everything",
#     "explanation": "Using absolute terms suggests black-and-white thinking",
#     "reframe": "I've struggled with some things, but I've also succeeded at others"
#   },
#   ...
# ]
```

---

#### 2. `behavioral_activation(task: str, minutes: int = 5)` → Dict
**Purpose:** Break overwhelming tasks into 5-minute micro-actions

**The 5-Minute Rule:** Committing to just 5 minutes removes activation energy. Once started, momentum often builds naturally.

**Detects task categories and provides specific micro-actions:**
- **Writing** → "Open document, write just the title"
- **Studying** → "Gather materials, read first paragraph"
- **Exercise** → "Put on workout clothes"
- **Cleaning** → "Clear one small surface"
- **Communication** → "Draft first sentence, don't send yet"
- **Application** → "Fill in name and contact info"
- **Project** → "List 3-5 tiny steps"

**Output:**
- Original task
- Category
- Specific micro-action (≤5 min)
- Success criteria (achievable, measurable)
- Next step suggestion (if momentum builds)
- Permission to stop (reduces pressure)

---

#### 3. `thought_record(situation: str, thoughts: List[str], emotions: List[str])` → Dict
**Purpose:** Create structured ABC model thought records

**ABC Model (CBT foundation):**
- **A**: Activating Event (what happened)
- **B**: Beliefs/Thoughts (what you thought)
- **C**: Consequences (emotions & behaviors)

**Output Structure:**
- **A - Activating Event:** Situation analysis with objective facts
- **B - Beliefs:** Automatic thoughts + distortion analysis + evidence questions
- **C - Consequences:** Parsed emotions (with intensity 0-100), physical sensations
- **Cognitive Restructuring Prompts:**
  - Evidence for/against thoughts
  - Alternative interpretations
  - Friend perspective ("What would you tell a friend?")
  - Worst/best/realistic outcomes
  - Action steps
- **Balanced Thought Exercise:** Framework for creating more flexible thoughts
- **Re-rate Emotions:** Check if intensity decreased after restructuring

**Example:**
```python
thought_record(
    situation="Didn't get response to job application",
    thoughts=["I'm not qualified", "They rejected me", "I'll never get a job"],
    emotions=["anxious (80%)", "hopeless (70%)", "disappointed (60%)"]
)
```

---

### When Dr. Chen Excels
- Perfectionism and procrastination
- Negative self-talk and rumination
- Anxiety and catastrophic thinking
- Avoidance behaviors
- Need for structured problem-solving

---

## 💙 Maya - Empathetic Friend

**File:** `empathetic_friend.py`  
**Approach:** Compassionate listening, validation, and emotional support  
**Tools:** `TOOLS_SUPPORT`

### Personality & Style
- Warm, non-judgmental, deeply empathetic
- Validates emotions before offering solutions
- Uses "I" statements and reflective listening
- Prioritizes emotional safety and connection
- Balances empathy with gentle encouragement

### Tools (4)

#### 1. `reframe(negative_self_talk: str)` → str
**Purpose:** Transform self-criticism into self-compassion

**Based on:** Dr. Kristin Neff's self-compassion research

**Detects patterns:**
- "I'm a [negative label]" (failure, idiot, worthless)
- "I always/never..." (absolute language)
- "I should have..." (regret, hindsight)
- "I can't..." (helplessness)
- Catastrophizing language
- Comparison to others
- Perfectionism

**Output Format:**
1. **Validation:** "I hear that you're being really hard on yourself..."
2. **Perspective Shift:** Reframe the belief with nuance
3. **Compassionate Reframe:** Alternative statement with self-kindness
4. **Practice Prompt:** Hand-on-heart affirmation

**Example:**
```
Input: "I'm such an idiot for making that mistake"
Output: Validation + "Making a mistake doesn't make you an idiot—it makes you human" + self-compassion practice
```

---

#### 2. `grounding_exercise(duration: int = 3)` → Dict
**Purpose:** Quick breath & body awareness for overwhelm

**Technique:** Simplified grounding (breath + body anchor)

**4 Steps:**
1. **Find your breath** (hand on chest, feel rise/fall)
2. **Feel your body** (feet on floor, notice support)
3. **Soften one thing** (jaw, shoulders, fists)
4. **Say something kind** ("I'm here. I'm okay. This will pass.")

**When to use:**
- Before/during panic attack
- When emotions feel too big
- Racing thoughts
- Feeling disconnected or numb
- Before difficult conversations

---

#### 3. `resources(topic: str = "general")` → List[Dict]
**Purpose:** Curated mental health resources

**Topics supported:** crisis, therapy, anxiety, depression, student, general

**Resource Categories:**

**Crisis (always included if high-risk keywords detected):**
- 988 Suicide & Crisis Lifeline (call/text 988)
- Crisis Text Line (text HOME to 741741)
- Trevor Project (LGBTQ youth: 1-866-488-7386)
- SAMHSA National Helpline (1-800-662-4357)

**Therapy:**
- Psychology Today (therapist directory)
- Open Path Collective ($30-80/session)
- BetterHelp/Talkspace (online therapy)
- NAMI (support groups, helpline)

**Anxiety-specific:**
- ADAA (Anxiety & Depression Association)
- DARE App (panic/anxiety management)
- Headspace/Calm (meditation apps)

**Depression-specific:**
- DBSA (Depression & Bipolar Support Alliance)
- 7 Cups (peer support + affordable therapy)

**Self-Help:**
- MindTools (stress management, resilience)
- Therapist Aid (free CBT/DBT worksheets)
- Self-Compassion.org (Dr. Neff's resources)

**Student:**
- University counseling centers
- JED Foundation (teen/young adult mental health)

**Output:** List with name, type, contact, description, URL, availability

---

#### 4. `self_compassion_prompt()` → str
**Purpose:** Guided self-compassion practice

**Based on:** Dr. Kristin Neff's 3-component model

**3 Core Components:**
1. **Mindfulness:** "Right now, I'm struggling with ___" (acknowledge without judgment)
2. **Common Humanity:** "This is part of life. I'm not alone." (vs. isolation)
3. **Self-Kindness:** Hand on heart + compassionate phrases (vs. self-judgment)

**Phrases provided:**
- "May I be kind to myself in this moment"
- "I'm doing the best I can right now"
- "It's okay to struggle. I don't have to be perfect"
- "I deserve kindness, especially from myself"

**Why it matters (research-backed):**
- Greater emotional resilience
- Lower anxiety & depression
- More motivation to change (not less!)
- Better coping with failure

**Includes:** Link to self-compassion.org for guided meditations

---

### When Maya Excels
- Grief, loss, difficult emotions
- Loneliness and isolation
- Shame and self-criticism
- Need for validation before solutions
- Crisis support and resource navigation

---

## 📊 Alex - Rational Analyst & Time Manager

**File:** `rational_analyst.py`  
**Approach:** Logical analysis, data-driven insights, practical scheduling  
**Tools:** `TOOLS_RATIONAL` (calendar integration)

### Personality & Style
- Logical, organized, pragmatic
- Focuses on systems and processes
- Uses data and evidence
- Time management and productivity expert
- Direct but supportive communication

### Tools (3) - Google Calendar Integration

#### 1. `list_events(days: int = 7)` → List[Dict]
**Purpose:** Retrieve upcoming calendar events

**Real Integration:** Connects to Google Calendar API via OAuth

**Parameters:**
- `days`: Number of days to look ahead (default: 7)

**Output:** List of events with:
- Event ID
- Summary (title)
- Start time (ISO8601)
- End time (ISO8601)
- HTML link (view in Google Calendar)
- Status (confirmed/tentative/cancelled)

**Use Cases:**
- "Show me my schedule for the next week"
- Analyze workload before suggesting new commitments
- Identify busy periods causing stress

---

#### 2. `find_free_time(days: int = 3, duration_minutes: int = 60, work_hours: List[int] = [9, 18], topk: int = 3)` → List[Dict]
**Purpose:** Find available time slots based on existing calendar

**Parameters:**
- `days`: Days to search (default: 3)
- `duration_minutes`: Length of needed block (default: 60)
- `work_hours`: [start_hour, end_hour] in 24h format (default: 9am-6pm)
- `topk`: Number of suggestions (default: 3)

**Output:** List of available slots:
```python
[
  {
    "start": "2025-11-16T10:00:00+00:00",
    "end": "2025-11-16T11:00:00+00:00",
    "label": "Tomorrow morning (10:00 AM)"
  },
  ...
]
```

**Use Cases:**
- "When can I schedule a 1-hour focus session?"
- Find time for therapy appointments
- Schedule study blocks during finals
- Plan self-care activities

---

#### 3. `create_block(title: str, start_iso: str, duration_minutes: int = 60, description: str = "")` → Dict
**Purpose:** Create calendar events directly

**Parameters:**
- `title`: Event name (e.g., "Deep Work: Project Proposal")
- `start_iso`: Start time in ISO8601 format
- `duration_minutes`: Event length (default: 60)
- `description`: Optional notes

**Output:**
- Event ID
- HTML link to view/edit in Google Calendar

**Use Cases:**
- "Block 2 hours tomorrow for deep work"
- Schedule accountability check-ins
- Create break reminders during busy days
- Book focus time for avoided tasks (behavioral activation)

---

### Google Calendar OAuth Setup

**See main README section:** [📊 Google Calendar Integration](#-google-calendar-integration-rational-analyst--alex)

**Quick summary:**
1. Enable Google Calendar API in Cloud Console
2. Create OAuth credentials (Desktop app)
3. Download `credentials.json` → `backend/credentials.json`
4. Add test users in OAuth consent screen
5. First run opens browser for authorization
6. Token saved to `backend/.gcal_token.json`

---

### When Alex Excels
- Time management and procrastination
- Work-life balance issues
- Overwhelming schedules
- Need for practical, actionable plans
- Creating accountability systems

---

## 🧘 Sage - Mindfulness Mentor

**File:** `mindfulness_mentor.py`  
**Approach:** Present-moment awareness, values alignment, somatic techniques  
**Tools:** `TOOLS_MINDFUL`

### Personality & Style
- Calm, patient, grounding presence
- Uses poetic, sensory language
- Guides through experience vs. explaining
- Non-attachment to outcomes
- Emphasizes "noticing" over "fixing"

### Tools (4)

#### 1. `one_breath_instruction()` → str
**Purpose:** Immediate parasympathetic nervous system activation

**Simplest intervention:** One conscious breath can create a pause before reacting.

**Pattern:**
- **Inhale** slowly through nose (4 counts)
- **Hold** gently (2 counts)
- **Exhale** slowly through mouth (6 counts)

**Output:** Clear, calming instruction script with:
- Step-by-step guidance
- Reflection prompt ("Did anything shift?")
- Permission to repeat
- Reminder: available anytime, anywhere

**Evidence:** Activates parasympathetic "rest & digest" response

---

#### 2. `body_scan(duration: int = 5)` → Dict
**Purpose:** Guided body awareness meditation

**Based on:** MBSR (Mindfulness-Based Stress Reduction)

**Duration levels:**
- **3 min:** Brief (5 body parts, 30 sec each)
- **5-7 min:** Moderate (6 body parts, 45 sec each)
- **10+ min:** Detailed (11 body parts, 50 sec each)

**Output Structure:**
- **Preparation:** Position, initial breaths, intention
- **Script:** Section for each body part with:
  - Body area name
  - Approximate timestamp
  - Guidance text ("Notice sensations—warmth, tension, or nothing at all")
  - Duration in seconds
- **Closing:** Whole-body awareness, integration, gentle return
- **Tips:** What to do when mind wanders, if sleepy, if restless
- **Adaptations:** For overwhelm, sleepiness, restlessness

**Use Cases:**
- Release held tension
- Interrupt rumination
- Reconnect with physical self
- Before sleep

---

#### 3. `values_checkin()` → str
**Purpose:** Clarify personal values and alignment

**Based on:** ACT (Acceptance & Commitment Therapy) values work

**Values = Compass:** Point toward what gives life meaning, even when path is hard

**Reflection Prompts:**
1. **80th Birthday:** What would you hope people say about you?
2. **Come Alive Moment:** When did you feel most yourself? What value was honored?
3. **Core Values (Choose 3-5):** Connection, growth, creativity, contribution, adventure, health, authenticity, achievement, peace, justice, spirituality, independence, fun, etc.
4. **Gap Check:** Which values are you living? Which have you drifted from? What's one small action this week to honor a neglected value?

**Key Insight:** Values aren't goals (never "done"). They guide direction.

---

#### 4. `grounding_exercise(duration: int = 3)` → Dict
**Purpose:** 5-4-3-2-1 sensory grounding for anxiety/panic/dissociation

**Technique:** Anchor in present moment through five senses

**The Exercise:**
- **5 things you can SEE** 👁️ (notice small details)
- **4 things you can TOUCH** ✋ (press feet into floor)
- **3 things you can HEAR** 👂 (near and far)
- **2 things you can SMELL** 👃 (or imagine pleasant scent)
- **1 thing you can TASTE** 👅 (or imagine lemon)

**Output Structure:**
- Purpose & duration
- Preparation instructions
- Detailed guidance for each sense with examples
- Closing check-in
- Variations (3-2-1 shortcut, walking version)
- When to use (panic, dissociation, rumination, triggering memories)

**Bonus:** `quick_grounding_options()` provides 6 alternatives:
- Cold water splash (high intensity)
- Feet on floor (low intensity)
- Name categories (medium)
- Hand on heart (low)
- Butterfly hug (medium)
- Strong muscle tension (high)

---

### When Sage Excels
- Anxiety and panic attacks
- Stress and burnout
- Disconnection from body/self
- Decision paralysis
- Need for calm, non-judgmental space
- Existential questions and meaning-making

---

## 🔧 Technical Implementation

### Agent-Tool Mapping

```python
# In tools/__init__.py
TOOLS_RATIONAL = [list_events, find_free_time, create_block]
TOOLS_CBT = [identify_distortions, behavioral_activation, thought_record]
TOOLS_MINDFUL = [one_breath_instruction, body_scan, values_checkin, grounding_exercise]
TOOLS_SUPPORT = [reframe, grounding_exercise, resources, self_compassion_prompt]

# In agents/
# cognitive_behavioral.py
from persona_reflect.tools import TOOLS_RATIONAL, TOOLS_CBT

# empathetic_friend.py
from persona_reflect.tools import TOOLS_SUPPORT

# rational_analyst.py
from persona_reflect.tools import TOOLS_RATIONAL

# mindfulness_mentor.py
from persona_reflect.tools import TOOLS_MINDFUL
```

### Tool Design Principles

✅ **JSON-compatible types** for ADK function calling (no datetime objects, use ISO strings)  
✅ **Detailed docstrings** with Args, Returns, Examples  
✅ **Evidence-based techniques** (CBT, ACT, MBSR, self-compassion research)  
✅ **Structured outputs** (dicts/lists for easy parsing by agents)  
✅ **Flexible parameters** (duration, intensity, topic filters)  
✅ **User-friendly language** (no jargon in output)

### Adding a New Tool

```python
# 1. Define in appropriate tools/ file
def new_tool(param: str) -> Dict[str, Any]:
    """
    Tool description with clear purpose.
    
    Args:
        param: Parameter description
    
    Returns:
        Structured output with helpful keys
    
    Example:
        >>> new_tool("example input")
        {"result": "example output"}
    """
    return {"result": "data"}

# 2. Export in tools/__init__.py
from .tool_file import new_tool
TOOLS_CATEGORY = [..., new_tool]

# 3. Import in agent file
from persona_reflect.tools import TOOLS_CATEGORY

# 4. Agent can now call the tool via ADK
```

---

## 🎯 Orchestration

**File:** `orchestrator.py`

**Role:** Coordinates all 4 agents using Google ADK

**Flow:**
1. Receives user dilemma from FastAPI
2. Distributes to all agents in parallel
3. Each agent processes with their specialized tools
4. Collects responses
5. Returns unified response with all perspectives

**ADK Features Used:**
- Multi-agent routing
- Parallel execution
- Tool function calling
- State management

---

## 📚 Further Reading

- **CBT:** *Cognitive Behavior Therapy: Basics and Beyond* by Judith Beck
- **ACT:** *The Happiness Trap* by Russ Harris
- **MBSR:** *Full Catastrophe Living* by Jon Kabat-Zinn
- **Self-Compassion:** *Self-Compassion* by Kristin Neff
- **Google ADK:** https://google.github.io/adk-docs/

---

## 🚀 Usage

```python
# Interactive demo with all agents
cd backend
python interactive_demo.py

# API endpoint (all agents + tools)
POST http://localhost:8000/api/reflect
{
  "user_id": "demo_user",
  "dilemma": "I keep procrastinating on my important project"
}

# Response includes insights from all 4 agents, each using their specialized tools
```

---

*"Four perspectives, one goal: helping you navigate life's challenges with wisdom, compassion, and evidence-based support."*
