{%- if 'y' in cookiecutter.use_click %}
import sys
import logging

import click
from click import echo
{%- endif %}


__version__ = '{{ cookiecutter.version }}'

{% if 'y' in cookiecutter.use_click %}
@click.command()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@click.option(
    '--debug',
    is_flag=True,
    help='enable debug logging'
)
def main(debug):
    """Main entry point"""
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")
{%- endif %}
