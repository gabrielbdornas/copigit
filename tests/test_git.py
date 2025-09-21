from tests.conftest import project_dir

import pytest

def test_git_creation(create_project):
    """
    Test new project creation with .git folder.
    """

    project = create_project()
    _project_dir = project_dir(project)
    project_path_structure = _project_dir[3]

    assert '.git' in project_path_structure
