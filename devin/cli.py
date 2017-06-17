import click
import random


def _pick_intro():
    intros = ["Have you tried {}?",
              "Maybe you should listen to {}.",
              "What about {}?",
              "You should play {}."]
    return random.choice(intros)


def _load_albums():
    with open('albums/albums.txt', 'r') as f:
        albums = [album.strip() for album in f.readlines()]
    return albums


@click.command()
@click.option('--more-devin',
              is_flag=True,
              help="""Yo dawg. I hear you like Devin.
                   So I put some devin in your devin, so you can devin while
                   you devin.
                   """)
def main(more_devin=False):
    intro = _pick_intro()
    albums = _load_albums()
    album = random.choice(albums)
    rec = intro.format(album)
    if more_devin:
        click.echo(rec, nl=False)
        click.echo(" It's a good good album.")
    else:
        click.echo(rec)
