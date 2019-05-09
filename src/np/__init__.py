import click
import api
from np import api


@click.group()
def cli():
    pass

@cli.command()
@click.argument('game_number')
def report(game_number):
    np_api = api.NeptuneAPI()
    #game_number="4848663437508608"
    click.echo(np_api.full_universe_report(game_number))

