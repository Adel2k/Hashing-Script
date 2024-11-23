import hashlib

password = input("Enter your password: ")

if len(password) > 8:
	print("Strong password")
	print("Your hashed password is: ", hashlib.sha256(password.encode()).hexdigest())
else:
	print("Weak password")
	print("Your hashed password is: ", hashlib.sha256(password.encode()).hexdigest())
