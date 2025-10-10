from tests.conftest import project_dir

import subprocess
import pytest

def test_git_creation(create_project):
    """
    Test new project creation with .git folder.
    """

    project = create_project()
    project_path = project_dir(project)

    assert (project_path / '.git').exists()


def test_initial_commit_created(create_project):
    """
    Test that an initial commit exists in the newly created project.
    """
    project = create_project()
    project_path = project_dir(project)

    result = subprocess.run(
        ["git", "-C", project_path, "log", "-1", "--pretty=%s"],
        capture_output=True,
        text=True,
    )

    commit_message = result.stdout.strip()

    assert "Initial" in commit_message or "init" in commit_message.lower(), (
        f"Unexpected initial commit message: {commit_message!r}"
    )
