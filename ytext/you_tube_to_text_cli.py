import click
from ytext.you_tube_to_text_converter import YouTubeToTextConverter

def convert(apikey, watson_url, url, language='en', default_folder='./temp', convert=True):
  try:
    YouTubeToTextConverter(apikey, watson_url, url, language, default_folder, convert)
  except Exception:
    click.echo(f'Something went wrong.')

@click.command(name='convert')
@click.pass_context
def convert_cli(ctx):
  """
  Create dataset in a CKAN instance.
  """
  create(
         ctx.obj['APIKEY'],
         ctx.obj['WATSON_URL'],
         )