"""Allow cookiecutter to be executable through `python -m cookiecutter`."""
from cookiecutter.cli.cli_parser import main


if __name__ == "__main__":  # pragma: no cover
    main(prog_name="cookiecutter")
