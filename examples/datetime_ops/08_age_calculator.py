"""Calculate age from a birthdate."""

from datetime import date


def calculate_age(birthdate):
    """Calculate current age in years from a birthdate."""
    today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age


def detailed_age(birthdate):
    """Calculate age in years, months, and days."""
    today = date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        from calendar import monthrange
        days += monthrange(today.year, prev_month)[1]
    if months < 0:
        years -= 1
        months += 12
    return {"years": years, "months": months, "days": days}


def days_until_birthday(birthdate):
    """Calculate days until the next birthday."""
    today = date.today()
    birthday = birthdate.replace(year=today.year)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    return (birthday - today).days


if __name__ == "__main__":
    bday = date(1990, 7, 15)
    print(f"Birthdate:      {bday}")
    print(f"Age:            {calculate_age(bday)} years")
    print(f"Detailed age:   {detailed_age(bday)}")
    print(f"Next birthday:  {days_until_birthday(bday)} days away")
