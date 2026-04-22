from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn
from pathlib import Path

app = FastAPI(title="Yasharth Rai - Portfolio")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Portfolio data
portfolio_data = {
    "name": "Yasharth Rai",
    "title": "Product‑minded PM",
    "location": "Noida",
    "tagline": "Turning messy data into confident decisions.",
    "subtitle": "Product‑minded project manager with a data backbone — bridging stakeholders, engineering, and metrics so shipping feels calm, not chaotic.",
    "meta": [
        {"dot": True, "text": "Open to opportunities"},
        {"text": "AFSB Recommended"},
        {"text": "Ex‑Amazon · GlobalLogic (Google xWF)"}
    ],
    "photo": "https://user-gen-media-assets.s3.amazonaws.com/gemini_images/fcef846d-d0b4-4088-8fee-c9f92f3f45d5.png",
    "photo_label": "Most recent: BuildPiper · Jr. PM",
    "tagline_card": "I work best where product, ops, and analytics intersect — owning sprints, roadmaps, and dashboards that tell the truth.",
    "skills_tags": [
        "Agile / Scrum",
        "SQL · Power BI",
        "Risk & Fraud Analysis",
        "User‑centric thinking"
    ],
    "stats": [
        {"label": "Years in delivery", "value": "2+"},
        {"label": "Fraud reduction", "value": "22%"},
        {"label": "Feature adoption", "value": "15%"},
        {"label": "Transactions reviewed", "value": "10K+"}
    ],
    "experience": [
        {
            "role": "Junior Project Manager",
            "company": "BuildPiper",
            "company_desc": "DevOps platform",
            "period": "Mar 2026 – Present",
            "location": "Noida",
            "current": True,
            "description": [
                "Own day‑to‑day delivery for cross‑functional squads, keeping sprints scope‑tight and stakeholders genuinely informed.",
                "Translate vague asks into clear tickets, prioritised roadmaps, and measurable success metrics.",
                "Partner with engineering to make trade‑offs explicit — aligning technical constraints with business timelines."
            ],
            "tags": ["Sprint rituals", "Roadmapping", "Stakeholder comms", "GTM support"]
        },
        {
            "role": "Analyst — Google xWF",
            "company": "GlobalLogic",
            "company_desc": "Google ecosystem",
            "period": "May 2025 – Feb 2026",
            "location": "Gurugram",
            "current": False,
            "description": [
                "Designed and maintained dashboards for the Health & Home product line that became the single source of truth for product leads.",
                "Turned raw event streams into clean, explainable views for PMs and legal teams — reducing 'data arguments' in reviews.",
                "Worked closely with product leads to define thresholds, alerts, and narratives around user behaviour and abuse patterns."
            ],
            "tags": ["Stakeholder‑first storytelling", "Product analytics", "SQL · dashboards"]
        },
        {
            "role": "Risk Investigator",
            "company": "Amazon",
            "company_desc": "Fraud & abuse",
            "period": "Jun 2024 – Apr 2025",
            "location": "Virtual",
            "current": False,
            "description": [
                "Analysed seller and transaction behaviour to identify fraud patterns, contributing to a 22% improvement in detection for my queue.",
                "Documented edge cases and playbooks that shortened ramp‑up time for new investigators.",
                "Collaborated with program managers to flag policy gaps and propose data‑backed process changes."
            ],
            "tags": ["Risk analysis", "Ops playbooks", "Pattern recognition"]
        }
    ],
    "about": {
        "paragraphs": [
            "I started on the operations side, grew obsessed with the patterns inside the data, and naturally drifted toward product and project work. At GlobalLogic, I spent nearly a year embedded in Google's Health & Home ecosystem; at Amazon, I looked at risk through the lens of people, not just flags.",
            "Today, as a Junior Project Manager at BuildPiper, I use that background to keep teams honest with numbers while still protecting the human side of delivery — scope, health, and trust."
        ],
        "pills": [
            "Agile / Scrum",
            "SQL · 5★ comfort",
            "Power BI & dashboards",
            "Product discovery",
            "Stakeholder management"
        ],
        "footnote": "Beyond work, I'm an AFSB‑recommended candidate and a solo bike rider — the kind who plans routes with the same care as release plans."
    },
    "skills": [
        {
            "label": "SQL & data modelling",
            "value": "Expert",
            "level": 90
        },
        {
            "label": "Project / sprint management",
            "value": "Advanced",
            "level": 80
        },
        {
            "label": "Product thinking & discovery",
            "value": "Advanced",
            "level": 75
        },
        {
            "label": "Stakeholder communication",
            "value": "Advanced",
            "level": 80
        }
    ],
    "tools": [
        {
            "title": "Delivery & planning",
            "desc": "Jira, ClickUp, Notion, sprint rituals, roadmap ownership"
        },
        {
            "title": "Analytics & BI",
            "desc": "SQL, Power BI, Excel (VBA/macros), dashboard design"
        },
        {
            "title": "Product & discovery",
            "desc": "User interviews, problem framing, metric definition"
        },
        {
            "title": "Ops & risk",
            "desc": "Fraud/risk analysis, playbook design, edge‑case mapping"
        }
    ],
    "life": [
        {
            "tag": "Bike rides",
            "title": "Maps, mountains, and quiet roads.",
            "body": "Solo rides on my Himalayan are where I do a surprising amount of thinking — about systems, trade‑offs, and what 'good work' feels like."
        },
        {
            "tag": "Learning",
            "title": "Always in 'product school'.",
            "body": "I break down products I use daily — flows, pricing, onboarding — and experiment with data‑driven side projects to sharpen the craft."
        },
        {
            "tag": "People",
            "title": "Tea + honest conversations.",
            "body": "Whether it's 1:1s with engineers or catching up with friends, I care about creating spaces where people feel heard, not pitched to."
        }
    ],
    "contact": {
        "text": "If you're looking for someone who can live in both dashboards and sprint boards, I'd love to explore how I can help your team.",
        "email": "raiyasharth4@gmail.com",
        "linkedin": "https://www.linkedin.com/in/yasharth-rai"
    }
}

@app.get("/", response_class=HTMLResponse)
async def get_portfolio(request: Request):
    """Serve the portfolio homepage"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": portfolio_data
    })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "Yasharth Rai - Portfolio"}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
