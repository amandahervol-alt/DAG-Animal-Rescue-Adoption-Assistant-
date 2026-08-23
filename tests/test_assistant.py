import os
import subprocess
import sys
from pathlib import Path


def test_index_html_structure_and_tabs():
    index_file = Path("index.html")
    assert index_file.exists(), "index.html must exist"

    content = index_file.read_text(encoding="utf-8")

    # Check Tabs
    assert "AI Adoption Assistant" in content
    assert "Pet Compatibility Matcher" in content
    assert "Adoption Process & Fees" in content
    assert "Foster & Volunteer Hub" in content

    # Check Mode Display & Demo Mode
    assert "Instant Demo Mode" in content
    assert "useDemoMode" in content

    # Check Fees & Veterinary Care
    assert "$100" in content and "$200" in content  # Dog fees
    assert "$50" in content and "$100" in content   # Cat fees
    assert "Spay or Neuter Surgery" in content
    assert "Microchip Registration" in content


def test_system_prompt_anti_hallucination_guardrails():
    index_file = Path("index.html")
    content = index_file.read_text(encoding="utf-8")

    # Verify anti-hallucination instruction is present
    assert "Never make up specific live shelter animals" in content
    assert "Deming Animal Guardians Facebook page" in content
    assert "100% of medical" in content or "100% Medical Coverage" in content


def test_app_runner_no_serve():
    res = subprocess.run(
        [sys.executable, "app.py", "--no-serve"],
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "[OK] Validated index.html" in res.stdout
