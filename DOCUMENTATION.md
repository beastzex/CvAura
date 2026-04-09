# CvAura - Resume Analysis & Optimization Platform

**Complete Project Documentation**

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Context & Purpose](#context--purpose)
3. [Key Features](#key-features)
4. [Tech Stack](#tech-stack)
5. [Technical Architecture](#technical-architecture)
6. [Directory Structure](#directory-structure)
7. [Installation & Setup](#installation--setup)
8. [Usage Guide](#usage-guide)
9. [API Documentation](#api-documentation)
10. [Database Schema](#database-schema)
11. [Development Guide](#development-guide)
12. [Deployment Guide](#deployment-guide)
13. [Environment Variables](#environment-variables)
14. [Troubleshooting](#troubleshooting)

---

## Project Overview

**CvAura** is a full-stack AI-powered resume analysis and optimization platform that helps job seekers improve their resumes through intelligent scoring, personalized editing suggestions, and company-specific targeting recommendations.

### Quick Stats
- **Frontend**: React + TypeScript + Vite + Tailwind CSS
- **Backend**: FastAPI + Python
- **Database**: Supabase (PostgreSQL)
- **AI Integration**: Groq Llama-3.1-70b-versatile API
- **File Processing**: PDF & DOCX support

---

## Context & Purpose

### Problem Statement
Job seekers struggle to:
- Optimize resumes for ATS (Applicant Tracking Systems)
- Understand what makes their resume competitive
- Tailor resumes for specific companies and roles
- Structure resume content professionally

### Solution
CvAura provides an all-in-one platform that:
- **Parses** resumes (PDF/DOCX) into structured data
- **Scores** resumes based on multiple criteria (fresher vs. experienced)
- **Suggests** improvements through AI-powered chat
- **Targets** companies with role-specific recommendations
- **Exports** optimized resumes as professional PDFs

### Target Users
- **Freshers**: Entry-level job seekers (graduates, interns)
- **Experienced Professionals**: Mid-career and senior professionals

---

## Key Features

### 1. **Resume Upload & Parsing**
- Support for PDF and DOCX formats
- Automatic extraction of structured data
- AI-powered parsing using Groq Llama-3.1-70b

### 2. **Resume Scoring**
- Comprehensive scoring algorithm (0-100)
- Multiple evaluation parameters:
  - Format & Structure
  - Content Relevance
  - Keywords & Skills
  - Achievement Metrics
  - Professional Presentation
- Different scoring criteria for freshers vs. experienced professionals

### 3. **AI-Powered Chat Editor**
- Section-specific editing assistance
- Natural language conversation for resume improvements
- Maintains conversation history for context
- Real-time suggestions

### 4. **Company Targeting & Recommendations**
- Analyzes job descriptions
- Provides company-specific recommendations
- Suggests skill emphasis for target roles
- Generates tailored content suggestions

### 5. **PDF Export**
- Generate professional PDF resumes
- Preserves formatting and structure
- Ready-to-send format

### 6. **Session Management**
- Persistent resume sessions using Supabase
- Multiple resume handling per session
- Score history and tracking

---

## Tech Stack

### Frontend
```
├── React 18.3.1
├── TypeScript
├── Vite (build tool)
├── React Router (navigation)
├── Tailwind CSS (styling)
├── Shadcn/ui (component library)
├── TanStack React Query (state management)
├── Framer Motion (animations)
└── Sonner (notifications)
```

### Backend
```
├── FastAPI 0.111.0 (web framework)
├── Uvicorn 0.29.0 (ASGI server)
├── Python 3.11+
├── Pydantic (validation)
├── Supabase (database & storage)
├── Groq API (Llama-3.1-70b-versatile LLM)
├── PyMuPDF (PDF processing)
├── python-docx (DOCX processing)
├── Scikit-learn (text processing)
├── ReportLab (PDF generation)
└── Playwright (web scraping)
```

### Infrastructure
```
├── Supabase (PostgreSQL, Storage)
├── Groq API (Llama-3.1-70b-versatile Model)
├── Railway/Render (Backend hosting)
└── Vercel (Frontend hosting)
```

---

## Technical Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      USER BROWSER                           │
│         (React + TypeScript + Tailwind CSS)                 │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼ HTTPS
┌─────────────────────────────────────────────────────────────┐
│                   VERCEL (Frontend)                         │
│  ├── SPA (Single Page Application)                         │
│  ├── React Router for navigation                           │
│  └── TanStack Query for API calls                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼ REST API Calls
┌─────────────────────────────────────────────────────────────┐
│                 RAILWAY/RENDER (Backend)                    │
│                    FastAPI Server                           │
│                                                              │
│  ├── /api/upload          → Upload resume (PDF/DOCX)        │
│  ├── /api/score           → Score resume                    │
│  ├── /api/chat-edit       → AI-powered editing              │
│  ├── /api/target-company  → Company targeting              │
│  ├── /api/export-pdf      → PDF export                     │
│  └── /api/health          → Health check                    │
│                                                              │
│  Services:                                                  │
│  ├── parser.py            → Extract & parse resume data    │
│  ├── scorer.py            → Calculate resume scores         │
│  ├── chat.py              → AI chat for editing             │
│  ├── targeting.py         → Company recommendations         │
│  ├── pdf_generator.py     → PDF export                     │
│  └── scraper.py           → Job description scraping       │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┴──────────────┐
        ▼                            ▼
┌──────────────────┐        ┌──────────────────┐
│    SUPABASE      │        │   GROQ API       │
│  ┌────────────┐  │        │ (Llama-3.1-70b)  │
│  │ PostgreSQL │  │        │                  │
│  │ Database   │  │        │  • Parsing       │
│  └────────────┘  │        │  • Scoring       │
│  ┌────────────┐  │        │  • Chat          │
│  │  Storage   │  │        │  • Recommendations
│  │  Bucket    │  │        │                  │
│  └────────────┘  │        └──────────────────┘
└──────────────────┘
```

### Data Flow

#### 1. Resume Upload Flow
```
User selects file
    ↓
Frontend validates file (PDF/DOCX)
    ↓
POST /api/upload (FormData)
    ↓
Backend extracts text (PyMuPDF/python-docx)
    ↓
Groq Llama-3.1-70b structures resume JSON
    ↓
Store in Supabase (database + storage)
    ↓
Return parsed_json + session_id to frontend
```

#### 2. Scoring Flow
```
Frontend sends parsed_json
    ↓
POST /api/score
    ↓
Backend runs scoring algorithm
    ↓
Groq generates parameter-specific feedback
    ↓
Store scores in Supabase
    ↓
Return scores to frontend
```

#### 3. AI Chat Flow
```
User sends editing request
    ↓
POST /api/chat-edit with section_data
    ↓
Groq Llama-3.1-70b generates suggestions
    ↓
Return updated_section + message
    ↓
Frontend merges changes with current state
```

#### 4. Company Targeting Flow
```
User provides job description
    ↓
POST /api/target-company
    ↓
Analyze resume vs. job requirements
    ↓
Groq Llama-3.1-70b generates recommendations
    ↓
Return targeted suggestions
```

---

## Directory Structure

```
cvaura/
├── aura-resume-studio/           # Frontend (React + Vite)
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/              # Shadcn/ui components
│   │   │   ├── ChatBubble.tsx
│   │   │   ├── ChatTab.tsx
│   │   │   ├── DocumentViewer.tsx
│   │   │   ├── LandingPage.tsx
│   │   │   ├── Workspace.tsx
│   │   │   ├── ScoreCard.tsx
│   │   │   └── TiltCard.tsx
│   │   ├── pages/
│   │   │   ├── Index.tsx         # Main page
│   │   │   └── NotFound.tsx
│   │   ├── context/
│   │   │   └── AppContext.tsx    # Global state
│   │   ├── hooks/
│   │   │   ├── use-mobile.tsx
│   │   │   └── use-toast.ts
│   │   ├── lib/
│   │   │   ├── api.ts            # API client
│   │   │   ├── mock-data.ts
│   │   │   └── utils.ts
│   │   ├── App.tsx
│   │   ├── main.tsx              # Entry point
│   │   ├── index.css
│   │   └── App.css
│   ├── public/
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   └── playwright.config.ts
│
├── backend/                       # FastAPI backend
│   ├── api/                      # For Vercel deployment
│   │   └── index.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── parser.py             # Resume parsing
│   │   ├── scorer.py             # Scoring algorithm
│   │   ├── chat.py               # AI chat
│   │   ├── targeting.py          # Company targeting
│   │   ├── pdf_generator.py      # PDF export
│   │   ├── scraper.py            # Job scraping
│   │   └── __init__.py
│   ├── main.py                   # FastAPI app
│   ├── db.py                     # Supabase client
│   ├── schemas.py                # Pydantic models
│   ├── requirements.txt
│   ├── migration.sql             # Database schema
│   ├── test_grok.py
│   └── vercel.json
│
├── Myvenv/                        # Python virtual environment
├── .env                           # Environment variables
├── package.json                   # Root package.json
└── DOCUMENTATION.md              # This file
```

---

## Installation & Setup

### Prerequisites
- **Node.js** 16+ and **npm** or **bun**
- **Python** 3.11+
- **Git**
- A **Supabase** account (for database)
- A **Groq** account (for Llama API)

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd cvaura
```

### Step 2: Frontend Setup

```bash
cd aura-resume-studio

# Install dependencies
npm install
# or
bun install

# Create .env.local
cat > .env.local << EOF
VITE_API_URL=http://localhost:8000
EOF

# Start development server
npm run dev
# Server runs at http://localhost:8080
```

### Step 3: Backend Setup

```bash
cd ../backend

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-api-key

# Groq API (Llama-3.1-70b-versatile)
GROQ_API_KEY=your-groq-api-key

# Optional: For scraping services
YOUTUBE_API_KEY=optional-youtube-key
EOF

# Run database migrations (one-time setup)
psql -U postgres -d your_db_name < migration.sql

# Start FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Server runs at http://localhost:8000
```

### Step 4: Database Setup (Supabase)

1. Create Supabase project at https://supabase.com
2. Create tables with migration script:
   ```sql
   -- Run migration.sql in Supabase SQL editor
   ```
3. Get API credentials:
   - Project URL
   - Anon Key (API Key)
   - Service Role Key (if needed)

### Step 5: Groq API Setup

1. Go to https://console.groq.com
2. Create API key
3. Add to `.env` as `GROQ_API_KEY`

**Why Groq?**
- Llama-3.1-70b-versatile model for superior reasoning
- 1000 requests/minute rate limit (vs Gemini's lower limits)
- Better context understanding for resume analysis
- Cost-effective for high-volume processing

---

## Usage Guide

### End-User Workflow

#### 1. Upload Resume
```
1. Open application at http://localhost:8080
2. Select resume file (PDF or DOCX)
3. Choose user type: "fresher" or "experienced"
4. Click "Upload" button
5. System extracts and structures resume data
```

#### 2. View Resume Score
```
1. After upload, view resume score (0-100)
2. See breakdown of scoring parameters:
   - Format & Structure
   - Content Quality
   - Keywords Relevance
   - Achievement Metrics
   - Professional Appearance
3. Read detailed feedback for each parameter
```

#### 3. Chat with AI Editor
```
1. Navigate to "Edit" tab
2. Select section to edit (experience, projects, etc.)
3. Ask for improvements in natural language
4. Examples:
   - "Make my work experience more impactful"
   - "Add more technical details to projects"
   - "Improve the achievement metrics"
5. Review suggested changes
6. Accept or ask for refinement
```

#### 4. Target Specific Company
```
1. Go to "Target Company" section
2. Paste job description OR enter company name
3. System analyzes resume vs. job requirements
4. Receive:
   - Skill gap analysis
   - Content recommendations
   - Keywords to add
   - Section-specific suggestions
```

#### 5. Export Resume
```
1. Make all desired edits
2. Click "Export as PDF"
3. Download professional PDF resume
4. Ready to submit to applications
```

---

## API Documentation

### Base URL
```
Development: http://localhost:8000
Production: https://your-backend-domain.com
```

### Authentication
Currently no authentication. CORS is open for development.

### Endpoints

#### 1. Upload Resume
```http
POST /api/upload
Content-Type: multipart/form-data

Parameters:
  - file: UploadFile (PDF or DOCX)
  - user_type: string ("fresher" or "experienced")

Response:
{
  "session_id": "uuid",
  "resume_id": "uuid",
  "storage_url": "string",
  "parsed_json": {
    "personal_info": {
      "name": "string",
      "email": "string",
      "phone": "string",
      "location": "string",
      "linkedin": "string",
      "github": "string",
      "summary": "string"
    },
    "education": [
      {
        "degree": "string",
        "school": "string",
        "year": "string",
        "gpa": "string"
      }
    ],
    "experience": [
      {
        "title": "string",
        "company": "string",
        "period": "string",
        "bullets": ["string"]
      }
    ],
    "projects": [
      {
        "name": "string",
        "description": "string",
        "tech_stack": ["string"],
        "link": "string"
      }
    ],
    "hackathons": [
      {
        "name": "string",
        "award": "string",
        "year": "string"
      }
    ],
    "skills": ["string"],
    "certifications": [
      {
        "name": "string",
        "issuer": "string",
        "year": "string"
      }
    ]
  }
}

Status Codes:
  - 200: Success
  - 400: Invalid file format or user_type
  - 500: Server error
```

#### 2. Score Resume
```http
POST /api/score

Body:
{
  "parsed_json": object,
  "user_type": "fresher" | "experienced",
  "resume_id": "uuid"
}

Response:
{
  "overall_score": 85,
  "parameters": [
    {
      "label": "Format & Structure",
      "score": 90,
      "weight": 15,
      "feedback": "Excellent formatting..."
    },
    {
      "label": "Content Quality",
      "score": 80,
      "weight": 25,
      "feedback": "Good content but..."
    },
    // ... more parameters
  ]
}

Status Codes:
  - 200: Success
  - 400: Invalid user_type
  - 500: Server error
```

#### 3. Chat/Edit Resume
```http
POST /api/chat-edit

Body:
{
  "prompt": "Make my experience more impactful",
  "section_key": "experience",
  "section_data": {
    "title": "Software Engineer",
    "company": "TechCorp",
    "period": "2022-2024",
    "bullets": ["Developed features", "Led team"]
  },
  "chat_history": [
    {
      "role": "user",
      "content": "Previous message"
    },
    {
      "role": "assistant",
      "content": "Previous response"
    }
  ]
}

Response:
{
  "updated_section": {
    "title": "Senior Software Engineer",
    "company": "TechCorp",
    "period": "2022-2024",
    "bullets": [
      "Architected and deployed microservices...",
      "Led team of 5 engineers..."
    ]
  },
  "message": "Updated your experience section with stronger action verbs and metrics..."
}

Status Codes:
  - 200: Success
  - 500: Server error
```

#### 4. Target Company
```http
POST /api/target-company

Body:
{
  "parsed_json": object,
  "target": "Senior Software Engineer at Google...", // job description
  "job_title": "Software Engineer",
  "company": "Google"
}

Response:
{
  "skill_gaps": ["Kubernetes", "GraphQL"],
  "recommended_skills": ["Docker", "AWS"],
  "content_suggestions": [
    {
      "section": "experience",
      "suggestion": "Emphasize cloud infrastructure experience"
    }
  ],
  "keywords_to_add": ["scalability", "microservices"],
  "overall_match_score": 78
}

Status Codes:
  - 200: Success
  - 500: Server error
```

#### 5. Export PDF
```http
POST /api/export-pdf

Body:
{
  "parsed_json": object
}

Response:
  PDF file (binary)

Headers:
  Content-Type: application/pdf
  Content-Disposition: attachment; filename=resume.pdf

Status Codes:
  - 200: Success
  - 500: PDF generation failed
```

#### 6. Health Check
```http
GET /api/health

Response:
{
  "status": "ok",
  "version": "1.0.0"
}

Status Codes:
  - 200: API is running
```

---

## Database Schema

### Tables

#### `sessions`
```sql
CREATE TABLE sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_type VARCHAR(20) NOT NULL, -- 'fresher' or 'experienced'
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

#### `resumes`
```sql
CREATE TABLE resumes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID REFERENCES sessions(id) ON DELETE CASCADE,
  storage_url VARCHAR(500) NOT NULL,
  parsed_json JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

#### `scores`
```sql
CREATE TABLE scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  resume_id UUID REFERENCES resumes(id) ON DELETE CASCADE,
  overall_score INT NOT NULL,
  parameter_breakdown_json JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### `chat_history` (optional)
```sql
CREATE TABLE chat_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID REFERENCES sessions(id) ON DELETE CASCADE,
  resume_id UUID REFERENCES resumes(id) ON DELETE CASCADE,
  section_key VARCHAR(50),
  messages JSONB NOT NULL, -- Array of {role, content}
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### Storage Buckets

#### `resumes` Bucket
- Path: `{session_id}/{filename}`
- Stores original resume files
- Public read access for storage_url generation

---

## Development Guide

### Code Structure

#### Frontend (`aura-resume-studio/src`)

**Components**:
- `LandingPage.tsx` - Home page with intro
- `Workspace.tsx` - Main working area
- `DocumentViewer.tsx` - PDF preview
- `ChatBubble.tsx`, `ChatTab.tsx` - Chat UI
- `ScoreCard.tsx`, `ScoreTab.tsx` - Scoring display
- `RecommendationsTab.tsx` - Company targeting results
- `NavLink.tsx`, `TiltCard.tsx` - UI components

**Context**:
- `AppContext.tsx` - Global app state (resume data, scores, etc.)

**Hooks**:
- `use-mobile.tsx` - Mobile detection
- `use-toast.ts` - Toast notifications

**Library**:
- `api.ts` - API client functions
- `utils.ts` - Utility functions
- `mock-data.ts` - Development mock data

#### Backend (`backend`)

**Services**:
- `parser.py` - Resume text extraction and structuring (Groq)
- `scorer.py` - Scoring algorithm implementation
- `chat.py` - AI chat for editing (Groq)
- `targeting.py` - Company/job analysis (Groq)
- `pdf_generator.py` - PDF export (ReportLab)
- `scraper.py` - Job description scraping (Playwright)

**Core**:
- `main.py` - FastAPI routes and endpoints
- `schemas.py` - Pydantic models for validation
- `db.py` - Supabase client initialization

### Adding a New Feature

#### 1. Backend
```python
# 1. Add Pydantic schema in schemas.py
class NewFeatureRequest(BaseModel):
    param1: str
    param2: Any

# 2. Create service file in services/new_feature.py
def process_feature(data: dict):
    # Your logic
    return result

# 3. Add endpoint in main.py
@app.post("/api/new-feature")
async def new_feature(body: NewFeatureRequest):
    result = process_feature(body.dict())
    return result
```

#### 2. Frontend
```typescript
// 1. Add API function in lib/api.ts
export async function callNewFeature(data: any) {
  const response = await fetch(`${API_BASE}/api/new-feature`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return response.json();
}

// 2. Use in component
const [result, setResult] = useState(null);

const handleNewFeature = async () => {
  const res = await callNewFeature(data);
  setResult(res);
};

// 3. Render in JSX
return <div>{result && <p>{result.message}</p>}</div>;
```

### Running Tests

```bash
# Frontend tests
cd aura-resume-studio
npm run test          # One-time
npm run test:watch    # Watch mode

# Backend tests (if configured)
cd backend
python -m pytest
```

### Linting & Formatting

```bash
# Frontend
cd aura-resume-studio
npm run lint          # Check for lint errors

# Python formatting (optional)
cd backend
black *.py            # Format files
pylint *.py           # Lint
```

---

## Deployment Guide

### Frontend Deployment (Vercel)

#### 1. Connect Repository
```bash
cd aura-resume-studio
npm install -g vercel
vercel login
vercel
```

#### 2. Configure Environment Variables
In Vercel Dashboard:
- Settings → Environment Variables
- Add: `VITE_API_URL=https://your-backend-url.com`

#### 3. Automatic Deployment
- Vercel auto-deploys on push to main branch
- Build command: `npm run build`
- Output directory: `dist`

### Backend Deployment (Railway)

#### 1. Create Docker Image
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 2. Deploy to Railway
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
cd backend
railway up
```

#### 3. Set Environment Variables in Railway
- SUPABASE_URL
- SUPABASE_KEY
- GROQ_API_KEY

### Alternative: Deploy to Render

#### 1. Create `render.yaml`
```yaml
services:
  - type: web
    name: cvaura-backend
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 8000
    envVars:
      - key: SUPABASE_URL
        sync: false
      - key: SUPABASE_KEY
        sync: false
      - key: GROQ_API_KEY
        sync: false
```

#### 2. Deploy
- Push to GitHub
- Connect repo to Render.com
- Auto-deploys on push

---

## Environment Variables

### Backend (.env)

```bash
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here
SUPABASE_SERVICE_KEY=optional-service-key

# Groq API (Llama-3.1-70b-versatile)
GROQ_API_KEY=your-groq-api-key

# Optional: YouTube API
YOUTUBE_API_KEY=youtube-api-key

# Optional: Database (if not using Supabase)
DATABASE_URL=postgresql://user:password@localhost/dbname

# Server Configuration
PORT=8000
ENVIRONMENT=development
```

### Frontend (.env.local)

```bash
# API Configuration
VITE_API_URL=http://localhost:8000

# Optional: Add other API keys if needed
VITE_GROQ_API_KEY=optional
```

### Production (.env.production)

```bash
# Backend
VITE_API_URL=https://your-production-backend-url.com

# Frontend deployed on Vercel, backend on Railway
```

---

## Troubleshooting

### Frontend Issues

#### 1. "Cannot find module '@/...'"
**Solution**: Check `tsconfig.json` alias settings
```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

#### 2. CORS errors when calling backend
**Solution**: Check backend CORS settings in `main.py`
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 3. Vite dev server won't start
**Solution**: Clear cache and reinstall
```bash
rm -rf node_modules .vite package-lock.json
npm install
npm run dev
```

### Backend Issues

#### 1. "ModuleNotFoundError: No module named 'fastapi'"
**Solution**: Activate virtual environment and install dependencies
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### 2. Supabase connection failed
**Solution**: Verify environment variables
```bash
# Check .env file
echo $SUPABASE_URL
echo $SUPABASE_KEY
```

#### 3. Groq API errors
**Solution**: Verify API key and quota
- Check key at https://console.groq.com/keys
- Ensure account has active API access
- Monitor rate limits (1000 requests/minute)
- Check available tokens in Groq console

#### 4. PDF generation fails
**Solution**: Ensure ReportLab is installed
```bash
pip install reportlab==4.0.7
```

#### 5. Timeout when processing large PDFs
**Solution**: Increase timeout in production
- Vercel: Increase timeout limit
- Railway: Increase request timeout
- Use async processing for large files

### Database Issues

#### 1. "Could not connect to database"
**Solution**: Verify Supabase connection
```bash
# Test with psql
psql -U postgres -h your-host -d your-db
```

#### 2. Tables don't exist
**Solution**: Run migration script
```bash
# In Supabase SQL editor, paste migration.sql content
# Or via psql:
psql -U postgres -d your_db < migration.sql
```

#### 3. Storage bucket not accessible
**Solution**: Check bucket permissions in Supabase
- Navigate to Storage → resumes bucket
- Verify public read is enabled
- Check policy permissions

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ValueError: invalid literal for int()` | Score calculation error | Check user_type is valid ("fresher"/"experienced") |
| `FileNotFoundError: PDF not found` | File upload failed | Check Supabase storage bucket exists |
| `json.JSONDecodeError` | Invalid JSON response | Check Groq API response format |
| `Connection refused` | Backend not running | Start backend with `uvicorn main:app --reload` |
| `401 Unauthorized` | Invalid API key | Verify GROQ_API_KEY or SUPABASE_KEY |

---

## Performance Optimization

### Frontend
```typescript
// Use React.memo for expensive components
export const ScoreCard = React.memo(({ score }) => {
  return <div>{score}</div>;
});

// Use useMemo for expensive calculations
const memoizedScore = useMemo(() => calculateScore(resume), [resume]);

// Use code splitting
const ChatTab = React.lazy(() => import('./ChatTab'));
```

### Backend
```python
# Use caching for frequent operations
from functools import lru_cache

@lru_cache(maxsize=128)
def get_scoring_rules(user_type: str):
    return load_scoring_config(user_type)

# Use async for I/O operations
@app.post("/api/upload")
async def upload_resume(file: UploadFile):
    # Async file processing
    pass
```

### Database
```sql
-- Index frequently queried columns
CREATE INDEX idx_sessions_user_type ON sessions(user_type);
CREATE INDEX idx_resumes_session_id ON resumes(session_id);
CREATE INDEX idx_scores_resume_id ON scores(resume_id);
```

---

## Security Considerations

### Authentication (Recommended for Production)
```python
# Add JWT authentication
from fastapi.security import HTTPBearer, HTTPAuthCredential

security = HTTPBearer()

@app.post("/api/upload")
async def upload_resume(credentials: HTTPAuthCredential = Depends(security)):
    # Verify token
    # Process upload
    pass
```

### Rate Limiting
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/upload")
@limiter.limit("5/minute")
async def upload_resume(request: Request):
    pass
```

### Input Validation
- Always use Pydantic schemas
- Validate file types and sizes
- Sanitize user input
- Check SQL injection vulnerabilities

### Environment Secrets
- Never commit `.env` files
- Use `.env.example` template
- Rotate API keys regularly
- Monitor API usage

---

## Contributing Guidelines

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -m "Add feature"`
3. Push to branch: `git push origin feature/your-feature`
4. Create Pull Request with description
5. Wait for review and merge

---

## Support & Contact

For issues, questions, or suggestions:
- Create GitHub issue
- Contact development team
- Email support

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-04-08 | Initial release |
| 1.1.0 | TBD | Auth system |
| 1.2.0 | TBD | Advanced analytics |
| 2.0.0 | TBD | Mobile app |

---

## Roadmap

### Phase 1 (Current)
- ✅ Resume upload & parsing
- ✅ Scoring algorithm
- ✅ AI chat editing
- ✅ Company targeting

### Phase 2 (Q2 2024)
- 🔄 User authentication
- 🔄 Resume history & versioning
- 🔄 Batch resume processing
- 🔄 Advanced analytics dashboard

### Phase 3 (Q3 2024)
- 🔄 Mobile application
- 🔄 Integration with job boards
- 🔄 Real-time collaboration
- 🔄 Resume templates library

### Phase 4 (Q4 2024)
- 🔄 AI mock interviews
- 🔄 LinkedIn optimization
- 🔄 Cover letter generation
- 🔄 Enterprise features

---

**Last Updated**: April 8, 2026  
**Status**: Active Development  
**Maintained By**: Development Team
