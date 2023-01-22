username = input()
user_password = input()

while True:
    data = input()

    if data == user_password:
        break

print(f"Welcome {username}")
