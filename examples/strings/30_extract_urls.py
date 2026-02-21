"""Extract URLs from a block of text using regex."""

import re

URL_PATTERN = re.compile(r'https?://[^\s<>"\)]+')


def extract_urls(text):
    """Return a list of URLs found in the text."""
    return URL_PATTERN.findall(text)


if __name__ == "__main__":
    text = """
    Visit https://www.python.org for Python docs.
    Also check http://example.com/path?q=1&r=2 for more info.
    Our repo is at https://github.com/user/repo.git and
    the blog is https://blog.example.com/2024/01/hello-world
    """
    urls = extract_urls(text)
    print("Found URLs:")
    for url in urls:
        print(f"  {url}")
    print(f"Total: {len(urls)}")
