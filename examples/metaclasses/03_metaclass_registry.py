"""Registry pattern using a metaclass."""


class PluginRegistry(type):
    """Metaclass that automatically registers subclasses."""
    _registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:  # Don't register the base class itself
            mcs._registry[name.lower()] = cls
        return cls

    @classmethod
    def get(mcs, name):
        return mcs._registry.get(name.lower())

    @classmethod
    def all_plugins(mcs):
        return dict(mcs._registry)


class Plugin(metaclass=PluginRegistry):
    """Base class for plugins."""
    def execute(self):
        raise NotImplementedError


class JSONPlugin(Plugin):
    def execute(self):
        return "Processing JSON"


class XMLPlugin(Plugin):
    def execute(self):
        return "Processing XML"


class CSVPlugin(Plugin):
    def execute(self):
        return "Processing CSV"


if __name__ == "__main__":
    print("Registered plugins:")
    for name, cls in PluginRegistry.all_plugins().items():
        instance = cls()
        print(f"  {name}: {instance.execute()}")
    plugin = PluginRegistry.get("jsonplugin")
    print(f"\nLookup 'jsonplugin': {plugin().execute()}")
