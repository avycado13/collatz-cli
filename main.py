# /// script
# requires-python = ">=3.12"
# dependencies = ["matplotlib","click"]
# ///

from calculationbook import *

from tree import main
from helpers import collatz
import click


@click.group()
def cli():
    pass


@cli.command("collatz")
@click.argument("number")
def print_collatz(number: int):
    list = collatz(int(number))
    for num in list:
        print(str(num))
    print(f"{len(list)} steps")

@cli.command("tree")
@cli.argument("number")
def tree(number: int):
    pass
    # TODO add tree functionality
if __name__ == "__main__":
    cli()
