import click
from coursegen import create_project_structure

@click.command()
@click.argument("course_name")
def main(course_name):
    """CLI entry point for generating Udemy course structure."""
    create_project_structure(course_name)

if __name__ == "__main__":
    main()
