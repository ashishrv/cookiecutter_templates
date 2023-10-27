
import typer
from pprint import pprint
from dynaconf import settings

import {{cookiecutter.package_name}}.cli.items
import {{cookiecutter.package_name}}.cli.users

cli = typer.Typer()


@cli.command()
def showconfig():
    pprint(settings.as_dict())


@cli.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

cli.add_typer(users.app, name="users")
cli.add_typer(items.app, name="items")

if __name__ == "__main__":
    cli()
