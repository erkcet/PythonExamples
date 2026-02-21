"""Simple JSON validation without external libraries."""


def validate(data, schema):
    """Validate data against a simple schema definition."""
    errors = []
    _validate_recursive(data, schema, "", errors)
    return errors


def _validate_recursive(data, schema, path, errors):
    """Recursively validate data against schema."""
    expected_type = schema.get("type")
    type_map = {"string": str, "integer": int, "float": (int, float),
                "boolean": bool, "list": list, "dict": dict}
    if expected_type and expected_type in type_map:
        if not isinstance(data, type_map[expected_type]):
            errors.append(f"{path or 'root'}: expected {expected_type}, got {type(data).__name__}")
            return
    if expected_type == "dict" and "properties" in schema:
        for key, sub_schema in schema["properties"].items():
            if sub_schema.get("required") and key not in data:
                errors.append(f"{path}.{key}: required field missing")
            elif key in data:
                _validate_recursive(data[key], sub_schema, f"{path}.{key}", errors)
    if "min" in schema and data < schema["min"]:
        errors.append(f"{path}: value {data} < min {schema['min']}")


if __name__ == "__main__":
    schema = {"type": "dict", "properties": {
        "name": {"type": "string", "required": True},
        "age": {"type": "integer", "required": True, "min": 0},
        "email": {"type": "string"},
    }}
    good = {"name": "Alice", "age": 30, "email": "a@b.com"}
    bad = {"name": 123, "age": -1}
    print(f"Valid data errors: {validate(good, schema)}")
    print(f"Invalid data errors: {validate(bad, schema)}")
