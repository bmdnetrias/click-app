from pathlib import Path

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
    "--log-level", default="SUCCESS", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True, path_type=Path),
    default=None,
)
@click.pass_context
def cli(ctx, log_format, log_level, log_file):
    "{{ cookiecutter.description }}"

    ctx.ensure_object(dict)

    ctx.obj["logger"] = logging_config(log_format, log_level, log_file)
    ctx.obj["logger"].enable("{{ cookiecutter.underscored }}")


@cli.command(name="about")
@click.pass_context
def about(ctx):
    """{{ cookiecutter.description }}
    """

    logger = ctx.obj["logger"]
    
    logger.opt(colors=True).msg("<g>Here's some log output</g>")
