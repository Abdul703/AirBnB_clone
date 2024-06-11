#!/usr/bin/python3
from models.user import User

print(type(User.email) is str)
print(User.email == "")