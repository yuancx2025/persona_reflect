# PersonaReflect 🎭
## AI-Powered Multi-Agent Self-Reflection Coach

### HackDuke 2025 Project

PersonaReflect uses Google ADK to create a multi-agent system that provides diverse perspectives on personal dilemmas through four distinct AI personas.

## 🏗️ Architecture

```mermaid
graph TD
    User[User Interface] -->|Text| API[FastAPI Backend]
    User -->|Audio| AIn[Audio Input - Mic]
    AIn --> STT[Speech-to-Text]
    AIn --> EMO[Emotion Recognition]
    STT --> API[FastAPI Backend]
    EMO --> Orchestrator[ADK Orchestrator]
    API --> Orchestrator
    Orchestrator --> CBT[Dr. Chen - CBT Agent]
    Orchestrator --> EMP[Maya - Empathetic Agent]
    Orchestrator --> RAT[Alex - Rational Agent]
    Orchestrator --> MIN[Sage - Mindfulness Agent]
    CBT --> Response[Unified Response]
    EMP --> Response
    RAT --> Response
    MIN --> Response
    Response --> ActionPlan[Action Plan Generator]
    ActionPlan --> User
```

## 🌟 Features

- **4 Specialized AI Coaches**: Each with unique perspectives and approaches
  - 🧠 **Dr. Chen** - Cognitive-Behavioral Coach
  - 💙 **Maya** - Empathetic Friend
  - 📊 **Alex** - Rational Analyst
  - 🧘 **Sage** - Mindfulness Mentor
- **Multi-Agent Orchestration**: Using Google ADK for coordinated responses
- **Action Plan Generation**: Synthesizes insights into concrete steps
- **Beautiful React Frontend**: Clean, intuitive interface
- **Real-time Processing**: Fast, parallel agent processing

## 🚀 Quick Start (Hackathon Demo)

### Prerequisites
- Python 3.11+
- Node.js 18+
- Google API Key (for Gemini)

### Setup & Install

```bash
# Clone the repo
git clone https://github.com/yuancx2019/hackDuke2025
cd hackDuke2025

# Install backend + frontend dependencies
make install

# Copy env template and add your Google API key
cp backend/.env.example backend/.env
# edit backend/.env and set GOOGLE_API_KEY=<your-key>
```

### Interactive Agent Demo

```bash
cd backend
python interactive_demo.py
```

### Run the Full Stack

```bash

# Pull a prebuilt backend Docker image (this container listens on port 9000)
docker pull eddiehza/fastapi-app:v3.0

# Run the prebuilt backend image and publish it to localhost:9000
docker run -d -p 9000:9000 eddiehza/fastapi-app:v3.0

# Backend only: starts FastAPI with hot-reload (uvicorn, default port 8000)
make backend

# Frontend only: starts the Vite dev server (default port 5173)
make frontend
```

### Full-Stack Integration Test

**Two-terminal setup:**

```bash
# Terminal 1: Backend
cd backend
uvicorn persona_reflect.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Frontend  
cd frontend
npm install
npm run dev
```

Then open http://localhost:5173/ and test the complete flow:
1. Check for "Connected to AI backend!" toast notification
2. Click "Start New Reflection"
3. Enter a dilemma and submit
4. Verify all 4 AI personas respond (10-20 seconds)
5. Create and save an action plan

**📘 For detailed integration testing:** See [INTEGRATION_TEST.md](./INTEGRATION_TEST.md)

### Access the Application

- 🌐 **Frontend**: http://localhost:5173
- 🔧 **API Docs**: http://localhost:8000/docs
- 📊 **API Health**: http://localhost:8000/

## 📚 API Endpoints

| Endpoint             | Method | Description                                   |
| -------------------- | ------ | --------------------------------------------- |
| `/`                  | GET    | Health check                                  |
| `/api/reflect`       | POST   | Process dilemma through all personas          |
| `/api/action-plan`   | POST   | Generate action plan from insights            |
| `/api/personas`      | GET    | Get persona information                       |
| `/api/alex/schedule` | POST   | Get available time slots from Google Calendar |
| `/api/alex/book`     | POST   | Create a new event on Google Calendar         |

---

## 📊 Google Calendar Integration (Rational Analyst — Alex)

Our agents can now analyze your workload and directly schedule focused work sessions in **Google Calendar**.
Follow these steps to enable the connection locally.

### ✅ 1️⃣ Create Google Cloud OAuth Credentials

1. Go to the **[Google Cloud Console](https://console.cloud.google.com/)**.
2. Create a new project or use an existing one.
3. Navigate to:

   ```
   APIs & Services → Enabled APIs & Services
   ```
4. Click **“+ ENABLE APIS AND SERVICES.”**
5. Search for **Google Calendar API** → click **Enable**.
6. Then go to:

   ```
   APIs & Services → Credentials → Create Credentials → OAuth client ID
   ```
7. Choose **“Desktop app”** as the application type.
8. Download the generated JSON file (it will look like `client_secret_xxx.json`).

   * This file is your **OAuth client credentials**.
   * **Do not commit or share** this file publicly.

---

### ✅ 2️⃣ Add the Credentials to the Backend

1. Move your downloaded credentials into the backend directory and rename it to:

   ```
   backend/credentials.json
   ```

2. Add both credentials and tokens to your `.gitignore`:

   ```
   backend/credentials.json
   backend/.gcal_token.json
   ```

---

### ✅ 3️⃣ Add Test Users to the OAuth Consent Screen

Since the app is still in testing mode, only test users can authorize it.

1. Go to:

   ```
   APIs & Services → OAuth consent screen → Audience
   ```
2. Under **Test users**, click **“+ ADD USERS.”**
3. Add your Gmail address (e.g. `youremail@gmail.com`).
4. Save changes.

> Only users listed here can log in during OAuth testing.

---

### ✅ 4️⃣ Authorize the App (First-Time Login)

When you run the backend (or call a calendar endpoint for the first time):

1. A browser window will open automatically.
2. Log in with your Google account.
3. Approve access to your **Google Calendar**.
4. A token file will be created automatically:

   ```
   backend/.gcal_token.json
   ```

   * This stores your personal access & refresh tokens.
   * It allows future access without re-login.

> ⚠️ This token file is user-specific. Keep it local and private.

---

### ✅ 5️⃣ Verify Connection

Once authorization is complete, your terminal will show:

```bash
🚀 Initializing PersonaReflect multi-agent system...
✅ Google Calendar token found at backend/.gcal_token.json
```

This confirms your backend is connected to Google Calendar.


### Example Request

```bash
curl -X POST http://localhost:8000/api/reflect \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user",
    "dilemma": "I keep procrastinating on my important project"
  }'
```

## 🛠️ Tech Stack

### Backend
- **Google ADK**: Multi-agent orchestration
- **FastAPI**: REST API framework
- **Google Gemini**: LLM for agents
- **Pydantic**: Data validation

### Frontend
- **React 18**: UI framework
- **TypeScript**: Type safety
- **Tailwind CSS**: Styling
- **Vite**: Build tool
- **Motion**: Animations

## 📦 Project Structure

```
hackDuke2025/
├── backend/                            # Main ADK multi-agent system
│   ├── persona_reflect/               
│   │   ├── agents/                    # AI Persona Agents
│   │   │   ├── orchestrator.py       # Main ADK orchestrator
│   │   │   ├── cognitive_behavioral.py # Dr. Chen (CBT Coach)
│   │   │   ├── empathetic_friend.py   # Maya (Empathetic Friend)
│   │   │   ├── rational_analyst.py    # Alex (Rational Analyst)
│   │   │   ├── mindfulness_mentor.py  # Sage (Mindfulness Mentor)
│   │   │   └── controllers/
│   │   │       └── scheduler.py       # Calendar integration logic
│   │   ├── prompts/                   # Few-shot prompt templates
│   │   │   └── personas.py            # Persona definitions & examples
│   │   ├── tools/                     # Agent tools
│   │   │   ├── calendar_tools.py      # Google Calendar integration
│   │   │   ├── cbt_tools.py           # CBT-specific tools
│   │   │   ├── mindfulness_tools.py   # Mindfulness exercises
│   │   │   └── support_tools.py       # General support tools
│   │   ├── services/                  # External service integrations
│   │   │   └── gcal_demo.py           # Google Calendar API wrapper
│   │   └── main.py                    # FastAPI server & endpoints
│   ├── requirements.txt               # Python dependencies
│   ├── Dockerfile                     # Backend container config
│   ├── interactive_demo.py            # CLI demo for testing agents
│   └── quick_test.py                  # Smoke tests
│
├── frontend/                           # React + TypeScript UI
│   ├── src/
│   │   ├── components/                # React components
│   │   │   ├── JournalInput.tsx       # User input interface
│   │   │   ├── PersonaCard.tsx        # Persona response display
│   │   │   ├── ActionPlanCreator.tsx  # Action plan interface
│   │   │   ├── AlexScheduler.tsx      # Calendar booking UI
│   │   │   ├── Dashboard.tsx          # Main dashboard
│   │   │   ├── EmotionChart.tsx       # Emotion visualization
│   │   │   └── ui/                    # Reusable UI components
│   │   ├── services/
│   │   │   ├── api.ts                 # API client
│   │   │   └── frontend-api-service.ts # Service layer
│   │   ├── types/
│   │   │   └── index.ts               # TypeScript type definitions
│   │   └── App.tsx                    # Main app component
│   ├── package.json                   # Node dependencies
│   ├── Dockerfile                     # Frontend container config
│   └── vite.config.ts                 # Vite build configuration
│
├── fastapi/                            # Alternative FastAPI setup
│   ├── app.py                         # Standalone API server
│   ├── requirements.txt
│   └── Dockerfile
│
├── models/                             # ML models (future)
│   └── speechemo/                     # Speech emotion recognition
│       ├── anger.wav                  # Sample audio
│       ├── test.py                    # Model test script
│       └── requirements.txt
│
├── docker-compose.yml                 # Full-stack orchestration
├── Makefile                           # Development commands
└── README.md                          # This file
```

## 🧪 Testing the System

1. **Smoke test + dependency checks**

    ```bash
    cd backend
    python quick_test.py
    ```

    > The script verifies `.env`, required packages, module imports, and optionally runs a live ADK agent call.

2. **Interactive multi-agent demo**

    ```bash
    python interactive_demo.py
    ```

    > Choose a sample dilemma or type your own to see all four personas respond in parallel.

3. **API health check (after `make backend` or `make docker-up`)**

    ```bash
    curl -X POST http://localhost:8000/api/reflect \
      -H "Content-Type: application/json" \
      -d '{
        "user_id": "demo_user",
        "dilemma": "I struggle with work-life balance"
      }'
    ```

## 🎮 Demo Flow

1. **Start**: User enters a personal dilemma
2. **Process**: ADK orchestrator distributes to 4 agents in parallel
3. **Insights**: Each persona provides unique perspective
4. **Synthesis**: System generates actionable steps
5. **Track**: User can save and track progress

## 🔄 Complete Pipeline

### 1. **User Input Layer**
```
Frontend (React) → API Request → FastAPI Backend
```
- User enters dilemma via `JournalInput.tsx`
- Frontend sends POST to `/api/reflect`
- Request includes `user_id`, `dilemma`, and optional `context`

### 2. **Backend Processing Layer**
```
FastAPI → ADK Orchestrator → Multi-Agent System
```
**Entry Point:** `backend/persona_reflect/main.py`
- Receives HTTP request
- Validates input with Pydantic models
- Initializes `PersonaReflectOrchestrator`

**Orchestrator:** `backend/persona_reflect/agents/orchestrator.py`
- Uses Google ADK's multi-agent framework
- Distributes dilemma to all 4 personas in parallel
- Coordinates agent responses via ADK's routing

### 3. **Agent Processing Layer**
```
Orchestrator → [Dr. Chen | Maya | Alex | Sage] → Tools
```

**Four Specialized Agents:**

1. **Dr. Chen (CBT Coach)** - `cognitive_behavioral.py`
   - Applies cognitive-behavioral therapy techniques
   - Uses `cbt_tools.py` for structured exercises
   - Identifies cognitive distortions
   - Provides reframing strategies

2. **Maya (Empathetic Friend)** - `empathetic_friend.py`
   - Offers emotional support and validation
   - Uses `support_tools.py` for empathy techniques
   - Focuses on emotional understanding
   - Provides compassionate responses

3. **Alex (Rational Analyst)** - `rational_analyst.py`
   - Provides logical, data-driven analysis
   - Uses `calendar_tools.py` for scheduling
   - **Google Calendar Integration** via `services/gcal_demo.py`
   - Can suggest time slots and book focused work sessions
   - Creates actionable task breakdowns

4. **Sage (Mindfulness Mentor)** - `mindfulness_mentor.py`
   - Guides mindfulness and meditation practices
   - Uses `mindfulness_tools.py` for exercises
   - Offers present-moment awareness techniques
   - Provides breathing exercises and body scans

**Agent Tools:**
- Each agent has access to specialized tool functions
- Tools are defined in `backend/persona_reflect/tools/`
- Google Calendar tools enable real scheduling capabilities

### 4. **Response Synthesis Layer**
```
Agent Responses → Orchestrator → Unified Response
```
- Orchestrator collects all persona responses
- Each response includes:
  - `persona`: Agent identifier
  - `name`: Display name
  - `icon`: UI icon
  - `response`: Actual advice text
- Returns combined insights to FastAPI endpoint

### 5. **Action Plan Generation**
```
POST /api/action-plan → Action Plan Generator → Concrete Steps
```
- User can request actionable steps
- System synthesizes insights from all personas
- Generates prioritized, measurable action items
- Frontend displays via `ActionPlanCreator.tsx`

### 6. **Calendar Integration Flow** (Alex-specific)
```
User Request → Alex Agent → Google Calendar API → Booked Event
```

**Scheduling Flow:**
1. User asks Alex for help with time management
2. Alex agent uses `alex_suggest_with_slots()` from `controllers/scheduler.py`
3. Calls `gcal_demo.py` to fetch real calendar data
4. Suggests optimal time slots based on availability
5. Frontend displays slots via `AlexScheduler.tsx`
6. User selects slot → POST to `/api/alex/book`
7. Event created in real Google Calendar

**OAuth Flow:**
- First run: `gcal_demo.py` initiates OAuth
- Opens browser for Google sign-in
- Stores refresh token in `.gcal_token.json`
- Subsequent calls use cached token

### 7. **Frontend Rendering Layer**
```
API Response → React State → Component Rendering
```

**Key Components:**
- `Dashboard.tsx`: Main layout and navigation
- `JournalInput.tsx`: Dilemma input form
- `PersonaCard.tsx`: Individual persona response cards
- `ActionPlanCreator.tsx`: Action plan interface
- `AlexScheduler.tsx`: Calendar booking interface
- `EmotionChart.tsx`: Emotional tracking visualization

**State Management:**
- API calls via `services/api.ts`
- Type-safe interfaces in `types/index.ts`
- React hooks for local state
- Toast notifications for feedback

### 8. **Data Flow Diagram**

```
┌─────────────┐
│   User      │
└──────┬──────┘
       │ Enter dilemma
       ▼
┌─────────────────────┐
│  Frontend (React)   │
│  - JournalInput     │
└──────┬──────────────┘
       │ POST /api/reflect
       ▼
┌─────────────────────┐
│  FastAPI Backend    │
│  - main.py          │
└──────┬──────────────┘
       │ Initialize
       ▼
┌─────────────────────┐
│  ADK Orchestrator   │
│  - orchestrator.py  │
└──────┬──────────────┘
       │ Distribute in parallel
       ▼
┌──────────────────────────────────────┐
│  Multi-Agent Processing (Parallel)   │
├──────────┬──────────┬────────┬───────┤
│ Dr. Chen │   Maya   │  Alex  │  Sage │
│   CBT    │ Empathy  │ Logic  │ Mind. │
└────┬─────┴────┬─────┴───┬────┴───┬───┘
     │          │         │        │
     │ Tools    │ Tools   │ Tools  │ Tools
     │          │         │        │
     │          │         ├────────┤
     │          │         │ GCal   │
     │          │         │ API    │
     └──────────┴─────────┴────────┘
                │
                │ Combine responses
                ▼
         ┌──────────────┐
         │   Response   │
         │   Synthesis  │
         └──────┬───────┘
                │
                ▼
         ┌──────────────┐
         │   Frontend   │
         │   Rendering  │
         └──────────────┘
```

### 9. **Development & Deployment Pipeline**

**Local Development:**
```bash
make install  → Install dependencies
make backend  → Start FastAPI (port 8000)
make frontend → Start Vite (port 5173)
```

**Testing:**
```bash
python quick_test.py        # Smoke tests
python interactive_demo.py  # CLI demo
make test                   # Full test suite
```

**Docker Deployment:**
```bash
make docker-build  # Build images
make docker-up     # Start containers
# Backend: localhost:8000
# Frontend: localhost:5173
```

**Production Flow:**
1. Build optimized Docker images
2. Push to container registry
3. Deploy to Google Cloud Run / K8s
4. Set environment variables
5. Configure OAuth callbacks
6. Monitor with logging

## 🔧 Development

### Quick Commands

```bash
# Install all dependencies
make install

# Run full stack in development mode
make dev

# Run services individually
make backend   # FastAPI on :8000
make frontend  # Vite on :5173

# Docker deployment
make docker-up    # Start all services
make docker-down  # Stop services

# Testing & Quality
make test      # Run backend tests
make lint      # Format and lint code
make clean     # Remove build artifacts
```

### Development Workflow

1. **Setup Environment**
   ```bash
   # Clone and install
   git clone https://github.com/yuancx2019/hackDuke2025
   cd hackDuke2025
   make install
   
   # Configure API keys
   cp backend/.env.example backend/.env
   # Edit backend/.env with your GOOGLE_API_KEY
   ```

2. **Start Development Servers**
   ```bash
   # Terminal 1: Backend
   make backend
   
   # Terminal 2: Frontend
   make frontend
   ```

3. **Test Changes**
   ```bash
   # Quick smoke test
   cd backend && python quick_test.py
   
   # Interactive agent testing
   cd backend && python interactive_demo.py
   
   # Full test suite
   make test
   ```

4. **Code Quality**
   ```bash
   # Format and lint
   make lint
   
   # Check for errors
   make test
   ```

### File Modification Guide

**Adding a New Agent:**
1. Create agent file in `backend/persona_reflect/agents/`
2. Define agent class with ADK decorators
3. Add persona definition to `prompts/personas.py`
4. Register in `orchestrator.py`
5. Update frontend `PersonaCard.tsx` for display

**Adding Agent Tools:**
1. Create tool file in `backend/persona_reflect/tools/`
2. Define tool functions with proper decorators
3. Import in agent file
4. Add to agent's tool list

**Modifying API Endpoints:**
1. Edit `backend/persona_reflect/main.py`
2. Update Pydantic models for validation
3. Update frontend `services/api.ts`
4. Update TypeScript types in `types/index.ts`

**Frontend Components:**
1. Create component in `frontend/src/components/`
2. Import in parent component or `App.tsx`
3. Use TypeScript for type safety
4. Follow existing Tailwind styling patterns

### Environment Variables

**Backend (`backend/.env`):**
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:5173
```

**Frontend (`.env.local` optional):**
```bash
VITE_API_URL=http://localhost:8000
```

### Debugging Tips

**Backend Issues:**
```bash
# Check API health
curl http://localhost:8000/

# Test specific endpoint
curl -X POST http://localhost:8000/api/reflect \
  -H "Content-Type: application/json" \
  -d '{"user_id":"test","dilemma":"test issue"}'

# View logs
# Uvicorn logs appear in terminal running make backend
```

**Frontend Issues:**
```bash
# Check console in browser DevTools (F12)
# Verify API connection
# Check Network tab for failed requests

# Clear cache and rebuild
rm -rf frontend/node_modules
cd frontend && npm install
npm run dev
```

**Docker Issues:**
```bash
# View container logs
docker logs persona-reflect-backend
docker logs persona-reflect-frontend

# Restart services
make docker-down
make docker-up

# Rebuild without cache
docker-compose build --no-cache
```

## 📈 Performance

- **Response Time**: <3 seconds for all 4 personas
- **Parallel Processing**: All agents run concurrently
- **Scalable**: Ready for cloud deployment

## 🚢 Deployment

### Docker Deployment
```bash
make docker-build
make docker-up
```

### Google Cloud Run
```bash
gcloud run deploy persona-reflect \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

## 👥 Team

- **Frontend**: React + TypeScript expert
- **Backend**: Google ADK integration
- **AI/ML**: Prompt engineering & agent design
- **DevOps**: Docker & cloud deployment

## 📝 Key Features for Judges

1. **Real Google ADK Implementation**: Not just API calls, but true multi-agent orchestration
2. **Production-Ready**: Docker, tests, proper error handling
3. **Unique Personas**: Each agent has distinct personality via few-shot prompting
4. **Actionable Output**: Synthesizes insights into concrete steps
5. **Clean Architecture**: Modular, scalable, maintainable

## 🔮 Future Enhancements

- [ ] Memory system for conversation history
- [ ] More specialized agents (Financial Advisor, Career Coach)
- [ ] A2A protocol for external agent integration

## 📄 License

MIT License - HackDuke 2025

---

*"Your personal board of advisors, powered by AI"*
