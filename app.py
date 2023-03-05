import random

def pwd():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=,/?><'
    length = 10
    password=''
    for c in range(length):
        password += random.choice(chars)
    return password