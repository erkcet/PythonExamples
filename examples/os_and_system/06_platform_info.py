"""Platform and system information using platform module."""

import platform
import sys
import struct


def get_system_info():
    """Get comprehensive system information."""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture()[0],
    }


def get_python_info():
    """Get Python interpreter information."""
    return {
        "version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "bits": struct.calcsize("P") * 8,
        "prefix": sys.prefix,
    }


def is_64bit():
    """Check if running on a 64-bit system."""
    return struct.calcsize("P") * 8 == 64


if __name__ == "__main__":
    print("System info:")
    for k, v in get_system_info().items():
        print(f"  {k}: {v}")
    print("\nPython info:")
    for k, v in get_python_info().items():
        print(f"  {k}: {v}")
    print(f"\n64-bit: {is_64bit()}")
    print(f"Platform: {platform.platform()}")
