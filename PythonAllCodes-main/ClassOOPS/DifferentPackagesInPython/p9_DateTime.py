from datetime import datetime, timedelta

now = datetime.now()
print(now)

# Add 5 days
future = now + timedelta(days=5)
print(future)

# Format date
print(now.strftime('%Y-%m-%Y %H:%M'))
