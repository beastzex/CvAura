import os, json, time
from openai import OpenAI
from schemas import ParsedResume, ScoreParameter, ScoreResponse

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def _call_grok_with_retry(prompt: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            time.sleep(wait_time)

FRESHER_PARAMS = [
    {"label": "Keyword Match",              "weight": 15},
    {"label": "Education Alignment",        "weight": 20},
    {"label": "Hackathons / Awards",        "weight": 10},
    {"label": "Projects & GitHub",          "weight": 15},
    {"label": "Certifications",             "weight": 10},
    {"label": "ATS Language",               "weight": 10},
    {"label": "Soft Skills",                "weight": 10},
    {"label": "LinkedIn Profile",           "weight": 10},
]

EXPERIENCED_PARAMS = [
    {"label": "Keyword Match",              "weight": 15},
    {"label": "Experience Quantification",  "weight": 20},
    {"label": "Role Progression",           "weight": 10},
    {"label": "Technical Depth",            "weight": 15},
    {"label": "Leadership & Impact",        "weight": 10},
    {"label": "ATS Language",               "weight": 10},
    {"label": "Industry Alignment",         "weight": 10},
    {"label": "Certifications",             "weight": 10},
]

def _build_prompt(parsed: dict, user_type: str, params: list[dict]) -> str:
    param_list = "\n".join(f'- "{p["label"]}" (weight {p["weight"]}%)' for p in params)
    return f"""
You are an expert ATS resume evaluator. Analyze the resume JSON below for a "{user_type}" candidate.

Score each parameter from 0-100 and provide one actionable feedback sentence per parameter.
Return ONLY valid JSON as an array:
[{{"label":"...","score":0-100,"weight":0-100,"feedback":"..."}}]

Parameters to score:
{param_list}

{"NOTE: If user_type is fresher, do NOT penalize for empty experience." if user_type == "fresher" else "NOTE: Focus heavily on quantified impact and action verbs in experience."}

RESUME JSON:
{json.dumps(parsed, indent=2)}

Return ONLY the JSON array, no markdown.
"""

def compute_score(parsed: dict, user_type: str) -> ScoreResponse:
    params = FRESHER_PARAMS if user_type == "fresher" else EXPERIENCED_PARAMS
    prompt = _build_prompt(parsed, user_type, params)
    response_text = _call_grok_with_retry(prompt)
    text = response_text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    items = json.loads(text)
    parameters = [ScoreParameter(**item) for item in items]
    overall = round(sum(p.score * p.weight / 100 for p in parameters))
    return ScoreResponse(overall_score=overall, parameters=parameters)
