"""
Placeholder tests — replace with repo-specific tests.
These ensure CI passes from day one without a live Oracle connection.
Tests against synthetic data only — no credentials needed in CI.
"""

import os


def test_placeholder():
    """
    Placeholder test — always passes.
    Replace with actual business logic tests.
    """
    assert True


def test_env_example_exists():
    """
    Verify .env.example is committed.
    Anyone cloning the repo needs this to know what credentials to set up.
    """
    assert os.path.exists(
        ".env.example"
    ), ".env.example must exist — others need it to configure the repo"


def test_requirements_exist():
    """Verify requirements.txt is committed."""
    assert os.path.exists(
        "requirements.txt"
    ), "requirements.txt must exist for pip install to work"


def test_data_md_exists():
    """Verify DATA.md is committed — documents synthetic data approach."""
    assert os.path.exists(
        "DATA.md"
    ), "DATA.md must exist — documents the synthetic data strategy"


def test_architecture_md_exists():
    """Verify ARCHITECTURE.md with Mermaid diagram exists."""
    assert os.path.exists(
        "ARCHITECTURE.md"
    ), "ARCHITECTURE.md must exist — contains the Mermaid architecture diagram"
