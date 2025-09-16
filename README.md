# Repo Template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)

Welcome to **[Repo Template](https://github.com/gabrielbdornas/repo-template)**, a general project template powered by the [Copier library](https://copier.readthedocs.io/en/stable/)!
This template helps you kickstart all kinds of projects with best practices and pre-configured tools.

## Prerequisites

Before using this template, ensure you have the following:

1. Git 2.27+ installed.
1. Python 3.9+ installed.
1. [pipx installed](https://pipx.pypa.io/stable/installation/).
1. [Copier installed via pipx](https://copier.readthedocs.io/en/stable/#installation).
1. [Cookiecutter install alongside Copier](https://copier.readthedocs.io/en/stable/configuring/#jinja_extensions) using the command `pipx inject copier cookiecutter`.

## Getting Started

Run the `copier copy` command to create your new Python project:

```bash
$ copier copy --trust gh:gabrielbdornas/repo-template destination-folder
```

Follow the prompts provided by [Copier](https://copier.readthedocs.io/en/stable/) to customize your new project.
The `copier copy` command works similarly to `git clone`, but instead of cloning the template repository as-is, it creates a new folder (specified as `destination-folder`) and populates it with a fully personalized file structure based on your answers.
The resulting project is fully independent of the template repository.
Replace `destination-folder` with the path where you'd like to create your project, which could be just `.` to indicate the creation in your current working directory.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
