import logging

import click

from click_default_group import DefaultGroup
from .logconfig import DEFAULT_LOG_FORMAT, logging_config


@click.group(cls=DefaultGroup, default="about", default_if_no_args=True)
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    default=DEFAULT_LOG_FORMAT,
    help="Python logging format string",
)
@click.option(
    "--log-level", default="ERROR", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    default=None,
)
def cli(log_format, log_level, log_file):
    "{{ cookiecutter.description }}"

    logging_config(log_format, log_level, log_file)


@cli.command(name="about")
@click.argument()
def about():
    "{{ cookiecutter.description }}"

    click.echo("Here is some output")
    logging.info("Here's some log output")
