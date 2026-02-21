"""A simple template engine that replaces {{variable}} placeholders with values."""

import re


def render_template(template, context):
    """Replace {{key}} placeholders with values from context dict."""
    def replacer(match):
        key = match.group(1).strip()
        return str(context.get(key, match.group(0)))
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', replacer, template)


if __name__ == "__main__":
    template = """Dear {{ name }},

Thank you for your order #{{ order_id }}.
Your total is ${{ total }}.

We will ship to {{ city }}, {{ country }}.

Best regards,
{{ company }}"""

    context = {
        "name": "Alice",
        "order_id": "12345",
        "total": "99.99",
        "city": "New York",
        "country": "USA",
        "company": "Acme Corp",
    }
    print(render_template(template, context))
