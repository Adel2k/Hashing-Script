import hashlib
import sys

filename = sys.argv[1]

new = f"SHA512-{filename}"

if len(sys.argv) == 2:
	try:
		with open(sys.argv[1] , 'r') as file:
			with open(new, "w") as new_file:
				for line in file:
					new_file.write(line.strip())
					new_file.write(" -> ")
					new_file.write(hashlib.sha512(line.encode()).hexdigest())
					new_file.write("\n")
	except FileNotFoundError:
		print("File does not exict.")
else:
	print("Please enter the file name that you want to be hashed.")
