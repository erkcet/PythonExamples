"""Read and write config files using configparser."""

import configparser
import io


SAMPLE_CONFIG = """\
[app]
name = MyApp
debug = false
version = 1.2.3

[database]
host = localhost
port = 5432
name = mydb
"""


def load_config(text: str) -> configparser.ConfigParser:
    """Parse config from a string."""
    config = configparser.ConfigParser()
    config.read_file(io.StringIO(text))
    return config


def display_config(config: configparser.ConfigParser):
    """Print all sections and their key-value pairs."""
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"  {key} = {value}")
        print()


def demonstrate_config():
    """Load, read, and modify a config."""
    config = load_config(SAMPLE_CONFIG)
    display_config(config)

    print("-- Accessing values --")
    print(f"App name: {config.get('app', 'name')}")
    print(f"Debug:    {config.getboolean('app', 'debug')}")
    print(f"DB port:  {config.getint('database', 'port')}")


if __name__ == "__main__":
    demonstrate_config()
