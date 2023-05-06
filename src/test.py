from hashlib import sha224

org = '123456'
pwd = sha224(org.encode('utf-8'))
pwdhex = pwd.hexdigest()
print(pwd)
print(pwdhex)