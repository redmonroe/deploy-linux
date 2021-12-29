from sqlalchemy import inspect, create_engine
from datetime import date
import click
from config import Config
from app.models import db, Categories

@click.group()
def cli():
    pass

@cli.command()
def database_test():
    db.create_all()
    table_names = inspect(db.engine).get_table_names()
    for item in table_names:
        print(item)

cli.add_command(database_test)

if __name__ == '__main__':
    cli()