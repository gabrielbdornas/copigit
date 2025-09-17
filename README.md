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

Run the `copier copy` command to create your new project:

```bash
$ copier copy --trust gh:gabrielbdornas/repo-template destination-folder
```

Follow the prompts provided by our [Copier Repo Template](https://github.com/gabrielbdornas/repo-template) to customize your new project.
The `copier copy` command works similarly to `git clone`, but instead of copying the template repository as-is, it generates a new project structure tailored to your answers.

* **Case 1 – destination folder specified**

  ```bash
  $ copier copy --trust gh:gabrielbdornas/repo-template my-experiment
  ```

  Copier will create a folder called `my-experiment/` (if it doesn’t already exist).
  Inside it, you’ll be asked to choose a **project name** and its **directory name**.
  For example, if you answer `Awesome tool` for **project name** and `awesome-tool` for **project directory's name** when prompted:

  ```text
  my-experiment/
  └── awesome-tool/
      └── README.md
  ```

  Here, `my-experiment/` is just the outer container, and `awesome-tool/` is your actual git repo folder (validated against our naming rules).

* **Case 2 – using the current directory (`.`)**

  ```bash
  $ copier copy --trust gh:gabrielbdornas/repo-template .
  ```

  Copier will scaffold your project directly in the current directory.
  In this case, the **current folder name itself must follow the naming rules**.

  Example: if you run the command inside a folder named `awesome-tool/`, the result will be:

  ```text
  awesome-tool/
  ├── README.md
  ├── pyproject.toml
  └── ...
  ```

That way, users immediately understand:

* Why there are sometimes two levels (`destination-folder` + `project-dir`).
* How naming rules apply in each case.
* What the end result looks like on disk.

Would you like me to also add an **invalid example** (e.g. running in a folder called `My Project/` and showing that it fails validation)? That could make the rules even clearer.


### Naming rules

To keep all git repositories consistent and compatible across tools and operating systems, project directory names must follow these rules:

* Use **lowercase letters** only.
* Separate words with **hyphens (`-`)**.
* Keep names short and descriptive.
* **Do not use special characters** like `@`, `#`, `$`, `&`, spaces, or accented letters (`ç`, `é`, etc.).
* Valid examples: `inventory-app`, `data-tools`, `my-service`.
* Invalid examples: `My Project`, `proj@123`, `café-app`.

This approach gives you the freedom to choose where the project is created, while guaranteeing that every generated repository respects the same naming standards.

---

Would you like me to also **show what happens when Copier automatically suggests a slugified name** (e.g. `"My Awesome App"` → `my-awesome-app`) so users see the transformation in action?


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
