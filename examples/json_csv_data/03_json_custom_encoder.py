"""Custom JSON encoder and decoder for non-standard types."""

import json
from datetime import datetime, date
from decimal import Decimal


class CustomEncoder(json.JSONEncoder):
    """JSON encoder that handles datetime, date, Decimal, and sets."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return {"__type__": "datetime", "value": obj.isoformat()}
        if isinstance(obj, date):
            return {"__type__": "date", "value": obj.isoformat()}
        if isinstance(obj, Decimal):
            return {"__type__": "decimal", "value": str(obj)}
        if isinstance(obj, set):
            return {"__type__": "set", "value": list(obj)}
        return super().default(obj)


def custom_decoder(obj):
    """Object hook to decode custom types."""
    if "__type__" in obj:
        if obj["__type__"] == "datetime":
            return datetime.fromisoformat(obj["value"])
        if obj["__type__"] == "date":
            return date.fromisoformat(obj["value"])
        if obj["__type__"] == "decimal":
            return Decimal(obj["value"])
        if obj["__type__"] == "set":
            return set(obj["value"])
    return obj


if __name__ == "__main__":
    data = {
        "timestamp": datetime.now(), "birthday": date(1990, 5, 15),
        "price": Decimal("19.99"), "tags": {"python", "json"},
    }
    encoded = json.dumps(data, cls=CustomEncoder, indent=2)
    print(f"Encoded:\n{encoded}")
    decoded = json.loads(encoded, object_hook=custom_decoder)
    print(f"\nDecoded types: {[(k, type(v).__name__) for k, v in decoded.items()]}")
