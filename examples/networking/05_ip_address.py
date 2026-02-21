"""Working with IP addresses using the ipaddress module."""

import ipaddress


def analyze_ip(addr_str):
    """Analyze an IP address and return its properties."""
    addr = ipaddress.ip_address(addr_str)
    return {
        "address": str(addr), "version": addr.version,
        "is_private": addr.is_private, "is_loopback": addr.is_loopback,
        "is_global": addr.is_global, "packed": addr.packed.hex(),
    }


def list_network_hosts(cidr):
    """List all usable host addresses in a network."""
    network = ipaddress.ip_network(cidr, strict=False)
    return {
        "network": str(network), "netmask": str(network.netmask),
        "broadcast": str(network.broadcast_address),
        "num_hosts": network.num_addresses - 2,
        "first_5": [str(h) for h in list(network.hosts())[:5]],
    }


def is_ip_in_network(ip_str, cidr):
    """Check if an IP address belongs to a network."""
    return ipaddress.ip_address(ip_str) in ipaddress.ip_network(cidr, strict=False)


if __name__ == "__main__":
    print("IPv4:", analyze_ip("192.168.1.1"))
    print("IPv6:", analyze_ip("::1"))
    print("Network:", list_network_hosts("10.0.0.0/24"))
    print("In network:", is_ip_in_network("10.0.0.50", "10.0.0.0/24"))
