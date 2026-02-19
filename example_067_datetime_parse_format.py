from datetime import datetime

dt = datetime.strptime("2026-02-19 14:30", "%Y-%m-%d %H:%M")
print(dt.strftime("%b %d, %Y %I:%M %p"))
