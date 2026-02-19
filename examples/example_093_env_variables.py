import os

mode = os.getenv("APP_MODE", "development")
print(f"Running in {mode} mode")
