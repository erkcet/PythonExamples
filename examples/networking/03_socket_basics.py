"""Basic socket concepts demonstration (no actual connections)."""

import socket


def get_local_hostname():
    """Get the local machine's hostname and IP."""
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "127.0.0.1"
    return hostname, ip


def demonstrate_address_families():
    """Show available socket address families."""
    families = {"AF_INET": socket.AF_INET, "AF_INET6": socket.AF_INET6}
    types = {"SOCK_STREAM (TCP)": socket.SOCK_STREAM, "SOCK_DGRAM (UDP)": socket.SOCK_DGRAM}
    return families, types


def resolve_hostname(hostname):
    """Resolve a hostname to IP addresses."""
    try:
        results = socket.getaddrinfo(hostname, None, socket.AF_INET)
        return list({r[4][0] for r in results})
    except socket.gaierror:
        return []


if __name__ == "__main__":
    host, ip = get_local_hostname()
    print(f"Hostname: {host}, IP: {ip}")
    families, types = demonstrate_address_families()
    print(f"Address families: {families}")
    print(f"Socket types: {types}")
    ips = resolve_hostname("localhost")
    print(f"localhost resolves to: {ips}")
