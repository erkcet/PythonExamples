def show_user(name, *roles, active=True, **extras):
    print(name, roles, active, extras)

show_user("Lia", "admin", "editor", active=False, city="NY")
