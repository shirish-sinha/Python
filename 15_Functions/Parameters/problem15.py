def create_email(username, domain="example.com"):
    return f"{username}@{domain}"


print(create_email("asha"))
print(create_email("rahul", "school.edu"))
