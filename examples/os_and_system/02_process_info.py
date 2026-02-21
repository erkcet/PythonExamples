"""Process information: PID, current directory, and more."""

import os
import sys


def get_process_info():
    """Get current process information."""
    return {
        "pid": os.getpid(),
        "ppid": os.getppid(),
        "cwd": os.getcwd(),
        "uid": os.getuid() if hasattr(os, "getuid") else "N/A",
        "python": sys.executable,
        "version": sys.version.split()[0],
    }


def get_resource_info():
    """Get process resource usage (Unix-like systems)."""
    try:
        import resource
        usage = resource.getrusage(resource.RUSAGE_SELF)
        return {"user_time": usage.ru_utime, "sys_time": usage.ru_stime}
    except ImportError:
        return {"note": "resource module not available"}


def get_cpu_count():
    """Get the number of CPUs available."""
    return os.cpu_count() or 1


if __name__ == "__main__":
    info = get_process_info()
    print("Process info:")
    for k, v in info.items():
        print(f"  {k}: {v}")
    print(f"CPU count: {get_cpu_count()}")
    print(f"Resources: {get_resource_info()}")
