"""Running external commands with subprocess."""

import subprocess


def run_command(cmd, capture=True):
    """Run a shell command and return output."""
    result = subprocess.run(
        cmd, shell=True, capture_output=capture, text=True, timeout=10
    )
    return {"stdout": result.stdout.strip(), "stderr": result.stderr.strip(), "code": result.returncode}


def run_safe(args):
    """Run a command safely using a list (no shell injection)."""
    result = subprocess.run(args, capture_output=True, text=True, timeout=10)
    return result.stdout.strip()


def get_command_output(cmd):
    """Get just the output of a command."""
    return subprocess.check_output(cmd, shell=True, text=True, timeout=10).strip()


if __name__ == "__main__":
    print("Date:", run_command("date"))
    print("Python version:", run_safe(["python3", "--version"]))
    print("Hostname:", get_command_output("hostname"))
    print("Uptime:", run_command("uptime")["stdout"])
