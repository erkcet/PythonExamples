"""Strip HTML tags from a string to extract plain text."""

import re


def strip_html(html):
    """Remove all HTML tags and decode common entities."""
    text = re.sub(r'<[^>]+>', '', html)
    entities = {'&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'"}
    for entity, char in entities.items():
        text = text.replace(entity, char)
    return text.strip()


if __name__ == "__main__":
    samples = [
        "<h1>Welcome</h1>",
        "<p>This is <b>bold</b> and <i>italic</i></p>",
        '<a href="https://example.com">Click &amp; go</a>',
        "<ul><li>Item 1</li><li>Item 2</li></ul>",
    ]
    for html in samples:
        print(f"HTML:  {html}")
        print(f"Text:  {strip_html(html)}")
        print()
