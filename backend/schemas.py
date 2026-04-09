from pydantic import BaseModel
from typing import Any, Optional

# ── Resume structured sections ──────────────────────────────────────────────

class PersonalInfo(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    github: str = ""
    summary: str = ""

class EducationItem(BaseModel):
    degree: str = ""
    school: str = ""
    year: str | int = ""
    gpa: str = ""

class ExperienceItem(BaseModel):
    title: str = ""
    company: str = ""
    period: str = ""
    bullets: list[str] = []

class ProjectItem(BaseModel):
    name: str = ""
    description: str = ""
    tech_stack: list[str] = []
    link: str = ""

class HackathonItem(BaseModel):
    name: str = ""
    award: str = ""
    year: str | int = ""

class CertificationItem(BaseModel):
    name: str = ""
    issuer: str = ""
    year: str | int = ""

class ParsedResume(BaseModel):
    personal_info: PersonalInfo = PersonalInfo()
    education: list[EducationItem] = []
    experience: list[ExperienceItem] = []
    projects: list[ProjectItem] = []
    hackathons: list[HackathonItem] = []
    skills: list[str] = []
    certifications: list[CertificationItem] = []

# ── API request/response bodies ──────────────────────────────────────────────

class ScoreRequest(BaseModel):
    parsed_json: dict[str, Any]
    user_type: str          # "fresher" | "experienced"
    resume_id: str

class ScoreParameter(BaseModel):
    label: str
    score: int
    weight: int
    feedback: str

class ScoreResponse(BaseModel):
    overall_score: int
    parameters: list[ScoreParameter]

class ChatRequest(BaseModel):
    prompt: str
    section_key: str        # e.g. "experience", "projects"
    section_data: Any
    chat_history: list[dict[str, str]] = []

class ChatResponse(BaseModel):
    updated_section: Any
    message: str

class TargetRequest(BaseModel):
    parsed_json: dict[str, Any]
    target: str             # company name or full JD text
    job_title: str = ""     # e.g., "Software Engineer", "SDE Intern"
    company: str = ""       # e.g., "Google", "Amazon"
