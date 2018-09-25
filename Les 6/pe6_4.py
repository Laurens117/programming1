def newpassword(oldpassword, password):
    if oldpassword not in password and len(password) >= 6:
        return True
    else:
        return False

oldpassword='pythoniscool'
password='abcdef'
print(newpassword(oldpassword, password))


