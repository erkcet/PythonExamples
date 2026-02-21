"""Adapter pattern: make incompatible interfaces work together."""


class EuropeanPlug:
    """A device with a European-style interface."""
    def provide_220v(self):
        return 220


class USSocket:
    """A socket expecting a US-style interface."""
    @staticmethod
    def supply(device):
        volts = device.provide_110v()
        return f"Supplying {volts}V"


class PlugAdapter:
    """Adapts a EuropeanPlug to work with a USSocket."""

    def __init__(self, euro_plug: EuropeanPlug):
        self._plug = euro_plug

    def provide_110v(self):
        """Convert 220V to 110V."""
        return self._plug.provide_220v() // 2


def demonstrate_adapter():
    """Show the adapter making incompatible objects cooperate."""
    euro = EuropeanPlug()
    adapter = PlugAdapter(euro)
    result = USSocket.supply(adapter)
    print(f"European plug via adapter: {result}")


if __name__ == "__main__":
    demonstrate_adapter()
