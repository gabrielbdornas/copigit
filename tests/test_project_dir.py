from tests.conftest import project_dir

import pytest


def test_project_dir_creation(create_project):
    """
    Test new project creation in general.
    """

    project = create_project()
    project_path = project_dir(project)

    assert project.exit_code == 0
    assert project.exception is None
    assert len([folder for folder in project_path.parent.glob('*')]) == 1
    assert project_path.is_dir()
    assert project_path.stem == 'new-python-project'


@pytest.mark.parametrize('project_name, project_dir_name', [
    ('1Meu Lindo Projeto', '1meu-lindo-projeto'),
    ('MEU LINDO PROJETO', 'meu-lindo-projeto'),
    ('meu-lindo-projeto', 'meu-lindo-projeto'),
    ('meu_lindo_projeto', 'meu-lindo-projeto'),
    ('Python Copier COM Café', 'python-copier-com-cafe'),
    ('PYTHON COPIER COM VOCÊ', 'python-copier-com-voce'),
    ('PYTHON copier com fumaça', 'python-copier-com-fumaca'),
    ('copier à Grega', 'copier-a-grega'),
    ('copier_à_Grega', 'copier-a-grega'),
    ('copier___à_ Grega', 'copier-a-grega'),
    ('copipy', 'copipy'),
    ('COPIPY', 'copipy'),
    ('Copipy', 'copipy'),
])
def test_project_dir_name_slugify(create_project, project_name, project_dir_name):
    """
    Test new project directory name and the slugify process.
    The `project_dir_name` variable must contains lowercase letters, digits or hyphens.
    If the  keep_project_dir_name == 'yes' it must use the  `slugify` filter provided by the
    `cookiecutter.extensions.SlugifyExtension` Jinja extension.
    """
    project = create_project(overrides={'project_name': project_name})
    project_path = project_dir(project)

    assert project_path.stem == project_dir_name


@pytest.mark.parametrize('project_name, project_dir_name', [
    ('Me Adapt', 'meadapt.com'),
    ('1Meu Lindo Projeto', 'meu-lindo'),
    ('MEU LINDO PROJETO', 'meu'),
])
def test_user_project_dir_name(create_project, project_name, project_dir_name):
    """
    Test new project directory name witout the slugify process.
    The `project_dir_name` variable must contains lowercase letters, digits, hyphens or dots.
    If the  keep_project_dir_name == 'no' it must use the  validator added to the project_dir_name question.
    """
    project = create_project(overrides={'project_name': project_name,
                                        'keep_project_dir_name': 'no',
                                        'project_dir_name': project_dir_name,})
    project_path = project_dir(project)

    assert project_path.name == project_dir_name

@pytest.mark.parametrize('project_name, project_dir_name', [
    ('MEU LINDO PROJETO', 'meu_lindo_projeto'),
    ('Orçamento', 'orçamento'),
    ('ORÇAMENTO', 'ORÇAMENTO'),
    ('Python Copier COM Café', 'python-copier-com-café'),

])
def test_user_project_dir_name_failed(create_project, project_name, project_dir_name):
    """
    Test new project directory name witout the slugify process.
    The `project_dir_name` variable must contains lowercase letters, digits, hyphens or dots.
    If the  keep_project_dir_name == 'no' it must use the  validator added to the project_dir_name question.
    If the `project_dir_name` not follow the rules, it must failed.
    """
    project = create_project(overrides={'project_name': project_name,
                                        'keep_project_dir_name': 'no',
                                        'project_dir_name': project_dir_name,})
    assert project.exit_code == -1
    assert "Validation error for question 'project_dir_name'" in str(project.exception)


def test_user_project_name_failed(create_project):
    """
    The `project_name` variable must be provided.
    If not, it must failed.
    """

    project = create_project(overrides={'project_name': '',
                                        'keep_project_dir_name': 'no',
                                        'project_dir_name': '',})
    assert project.exit_code == -1
    assert "Validation error for question 'project_name'" in str(project.exception)
