"""Parse INI-style configuration text into a dictionary structure."""

import re


def parse_ini(text):
    """Parse INI text into a nested dict of {section: {key: value}}."""
    config, section = {}, "DEFAULT"
    config[section] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line[0] in '#;':
            continue
        match = re.match(r'\[(.+)\]', line)
        if match:
            section = match.group(1)
            config[section] = {}
        elif '=' in line:
            k, v = line.split('=', 1)
            config[section][k.strip()] = v.strip()
    return config


if __name__ == "__main__":
    ini_text = "[database]\nhost = localhost\nport = 5432\n\n[server]\nhost = 0.0.0.0\nport = 8080"
    config = parse_ini(ini_text)
    for section, values in config.items():
        if values:
            print(f"[{section}]")
            for k, v in values.items():
                print(f"  {k} = {v}")
