# CvAura - Resume Optimization Platform

An AI-powered full-stack application that helps job seekers analyze, score, and optimize their resumes.

## Quick Start

### 📋 Prerequisites
- Node.js 16+
- Python 3.11+
- Supabase account
- Groq API key

### 🚀 Quick Setup

#### Frontend
```bash
cd aura-resume-studio
npm install
echo "VITE_API_URL=http://localhost:8000" > .env.local
npm run dev
# Open http://localhost:8080
```

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env with your credentials
echo "SUPABASE_URL=your-url" > .env
echo "SUPABASE_KEY=your-key" >> .env
echo "GROQ_API_KEY=your-groq-key" >> .env

uvicorn main:app --reload
# Server at http://localhost:8000
```

## 📚 Documentation

See [DOCUMENTATION.md](./DOCUMENTATION.md) for:
- Complete project overview
- Technical architecture
- Installation guide
- API documentation
- Database schema
- Deployment instructions
- Troubleshooting guide

## 🏗️ Project Structure

```
cvaura/
├── aura-resume-studio/     # React + Vite frontend
├── backend/                # FastAPI backend
├── Myvenv/                 # Python virtual env
└── DOCUMENTATION.md        # Full documentation
```

## 🎯 Key Features

- **Resume Upload & Parsing**: PDF/DOCX support with AI structuring
- **Smart Scoring**: Multi-parameter resume evaluation (0-100)
- **AI Chat Editor**: Natural language resume editing suggestions
- **Company Targeting**: Job description analysis and recommendations
- **PDF Export**: Generate professional optimized resumes

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React 18 + TypeScript + Vite + Tailwind |
| Backend | FastAPI + Python 3.11 |
| Database | Supabase (PostgreSQL) |
| AI | Groq Llama-3.1-70b-versatile (1000 req/min) |
| Hosting | Vercel + Railway |

## 📖 Common Commands

### Frontend
```bash
npm run dev          # Start dev server
npm run build        # Production build
npm run preview      # Preview build
npm run test         # Run tests
npm run lint         # Lint code
```

### Backend
```bash
uvicorn main:app --reload              # Dev server
python -m pytest                        # Run tests
black *.py                              # Format code
```

## 🚢 Deployment

- **Frontend**: Deploy to Vercel (auto-deploys from main)
- **Backend**: Deploy to Railway or Render

See [DOCUMENTATION.md - Deployment Guide](./DOCUMENTATION.md#deployment-guide) for detailed steps.

## 🔧 Environment Variables

### Backend (.env)
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
GROQ_API_KEY=your-groq-api-key
```

### Frontend (.env.local)
```
VITE_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

**Frontend won't connect to backend?**
- Ensure backend is running on port 8000
- Check VITE_API_URL in .env.local
- Check CORS settings in backend/main.py

**Supabase connection fails?**
- Verify SUPABASE_URL and SUPABASE_KEY
- Check if tables exist (run migration.sql)

**Groq API errors?**
- Verify GROQ_API_KEY is correct
- Check API is enabled at https://console.groq.com
- Verify rate limits (1000 requests/minute)

See [DOCUMENTATION.md - Troubleshooting](./DOCUMENTATION.md#troubleshooting) for more help.

## 📞 Support

For detailed information, see [DOCUMENTATION.md](./DOCUMENTATION.md)

---

**Status**: Active Development  
**Last Updated**: April 8, 2026
