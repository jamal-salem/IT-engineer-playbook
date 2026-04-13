def create_user(username):
    print(f"[+] Creating user: {username}")

users = ["admin", "guest", "test"]

for user in users:
    create_user(user)
