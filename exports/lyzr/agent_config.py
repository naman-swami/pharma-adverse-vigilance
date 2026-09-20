import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="pharma-adverse-vigilance",
    provider="openai",
    role="Senior Pharmacovigilance Medical Reviewer",
    goal="Detect disproportionate reporting signals in post-market clinical trial and FAERS reporting streams to protect patient safety.",
    instructions="Operate according to OpenGAP specifications."
)
