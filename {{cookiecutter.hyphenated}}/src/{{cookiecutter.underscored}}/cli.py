from pathlib import Path

import click

from click_default_group import DefaultGroup
from .logconfig import DEFAULT_LOG_FORMAT, LOGURU_LEVEL_NAMES, logging_config


@click.group(cls=DefaultGroup, default="about", default_if_no_args=True, invoke_without_command=True)
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    envvar="HADRONIC_LOG_FORMAT",
    show_envvar=True,
    default=DEFAULT_LOG_FORMAT,
    help="Loguru logging format string",
)
@click.option(
    "--log-level",
    type=click.Choice(LOGURU_LEVEL_NAMES + ["MSG"], case_sensitive=False),
    default="SUCCESS",
    help="Loguru logging level",
    envvar="HADRONIC_LOG_LEVEL",
    show_envvar=True,
    show_default=True,
)
@click.option(
    "--log-file",
    help="Loguru log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True, path_type=Path),
    envvar="HADRONIC_LOG_FILE",
    show_envvar=True,
    default=None,
)
@click.option(
    "--log-colorize / --no-log-colorize",
    help="Colorize log messages by default",
    envvar="HADRONIC_LOG_COLORIZE",
    show_envvar=True,
    default=True,
)
@click.pass_context
def cli(ctx, log_format, log_level, log_file, log_colorize):
    "{{ cookiecutter.description }}"

    ctx.ensure_object(dict)

    ctx.obj["logger"] = logging_config(log_format, log_level, log_file, log_colorize)
    ctx.obj["logger"].enable("{{ cookiecutter.underscored }}")


@cli.command(name="about", default=True)
@click.pass_context
def about(ctx):
    """{{ cookiecutter.description }}
    """

    logger = ctx.obj["logger"]
    
    logger.opt(colors=True).msg("<g>Here's some log output</g>")
