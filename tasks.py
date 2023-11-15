# Third Party
from invoke import task

@task
def tidy(c):
    """Format, and sort imports."""
    c.run("ruff . --fix")

@task
def toc(c):
    """Automate documentation tasks."""
    c.run("md_toc --in-place github --header-levels 4 README.md")
