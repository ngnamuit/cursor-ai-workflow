import os
import zipfile

base = "cursor-ai-workflow"

files = {
    "research/01_problem_analysis.md": "# Problem Analysis\n\n",
    "research/02_market_competitive_analysis.md": "# Market & Competitive Analysis\n\n",
    "research/03_technical_discovery.md": "# Technical Discovery\n\n",
    "research/04_solution_synthesis.md": "# Solution Synthesis\n\n",
    "docs/PRD.md": "# Product Requirements Document\n\n",
    "docs/decisions_log.md": "# Key Decisions Log\n\n",
    "plans/architecture.md": "# System Architecture\n\n",
    ".cursorrules": """You are a senior product-minded engineer.

Rules:
- Respect PRD and decisions_log as source of truth
- Prefer simple, explicit solutions
- Do not add features not specified
- Ask before making major changes
""",
}

os.makedirs(base, exist_ok=True)

for path, content in files.items():
    full_path = os.path.join(base, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

zip_name = "cursor-ai-workflow.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(base):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, arcname=file_path.replace(base + "/", ""))

print(f"✅ Created {zip_name}")
