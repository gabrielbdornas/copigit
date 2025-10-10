from tests.conftest import project_dir

import os
import pytest

def test_readme_creation(create_project):
    """
    Test new project creation with README.md file.
    """

    project = create_project()
    project_path = project_dir(project)

    assert (project_path / 'README.md').exists()

@pytest.mark.parametrize('project_name', [
    ('1Meu Lindo Projeto'),
    ('MEU LINDO PROJETO'),
    ('meu-lindo-projeto'),
    ('meu_lindo_projeto'),
    ('Python Copier COM Café'),
    ('PYTHON COPIER COM VOCÊ'),
    ('PYTHON copier com fumaça'),
    ('copier à Grega'),
    ('copier_à_Grega'),
    ('copier___à_ Grega'),
    ('copipy'),
    ('COPIPY'),
    ('Copipy'),
])
def test_readme_content(create_project, project_name):
    """
    Test new project's README.md content.
    """

    project = create_project(overrides={'project_name': project_name})
    project_path = project_dir(project)

    readme_path = project_path / 'README.md'
    readme_content = readme_path.read_text(encoding='utf-8')

    assert readme_content == f"## {project_name}\n"
