from urllib.request import urlopen
from urllib.error import URLError

try:
    with urlopen("https://example.com", timeout=5) as response:
        print(response.status)
except URLError as err:
    print(f"request failed: {err.reason}")
