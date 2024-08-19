from pathlib import Path
import typer
from typing_extensions import Annotated
import logging
from rich.logging import RichHandler
from enum import StrEnum
import logging.config

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
    }
)

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=str("NOTSET"),
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)


class LogLevel(StrEnum):
    """
    Solução estática para evitar os warinings do Pylance
    """

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="markdown",
    pretty_exceptions_show_locals=False,
)


class Ambiente(StrEnum):
    DEV = "dev"
    PROD = "prod"


class Arquitetura(StrEnum):
    ANDROID = "android"
    IOS = "ios"


class Produto(StrEnum):
    APP1 = "app1"
    APP2 = "app2"

@app.callback()
def main(
    ctx: typer.Context,
    log_level: Annotated[
        LogLevel, typer.Option(help="Configura o nível de detalhamento.")
    ] = LogLevel.INFO,
    show_log: Annotated[bool, typer.Option(help="Mostra ou oculta os logs.")] = True,
):
    """
    VFS-CLI

    A CLI tool for Y and Z.
    """
    logger.disabled = not show_log
    logger.setLevel(str(log_level))

    app_dir = typer.get_app_dir("red-tool")
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        logger.debug(f"Configurações não encontradas em `{config_path}`. Usando configurações padrão.")

    logger.debug(f"Excecutando o comando: {ctx.invoked_subcommand}")

@app.command()
def guiado():
    """
    Módulo para conduzir uma análise de forma interativa.

    **Create** a new *shinny* user:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Typer docs website](https://typer.tiangolo.com)
    """
    typer.echo("Nenhum módulo cadastrado")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

    print(1 / 0)


@app.command(rich_help_panel="CORP")
def download(
    uri: str = None,
    ambiente: Annotated[Ambiente, typer.Option(prompt=True)] = Ambiente.PROD,
    arquitetura: Annotated[
        Arquitetura, typer.Option(prompt=True)
    ] = Arquitetura.ANDROID,
):
    """
    Módulo para baixar builds dos repositórios internos.

    ---

    Documentação do módulo: [Typer docs website](https://typer.tiangolo.com)
    """
    logger.debug(f"{uri} {ambiente.value} {arquitetura.value}")


@app.command(rich_help_panel="CORP")
def manage_ticket():
    """
    Gerencia chamado

    Excecuta os modódulos de forma interativa.

    **Create** a new *shinny* user. :sparkles:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Typer docs website](https://typer.tiangolo.com)
    """
    typer.echo("Baixando...")


@app.command(rich_help_panel="Análise Estática")
def code_review():
    """
    Executa rotinas relacionadas a busca de padrões de código inseguros

    Excecuta os modódulos de forma interativa.

    **Create** a new *shinny* user. :sparkles:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Typer docs website](https://typer.tiangolo.com)
    """
    typer.echo("Baixando...")


@app.command(rich_help_panel="Análise Dinâmica")
def fuzzer():
    """
    Baixa arquivos dos repositórios.
    """
    typer.echo("Baixando...")


@app.command(rich_help_panel="Análise Dinâmica")
def fuzzer():
    """
    Baixa arquivos dos repositórios.
    """
    typer.echo("Baixando...")
