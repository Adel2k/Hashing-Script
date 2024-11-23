import hashlib
import sys

if len(sys.argv) == 2:
	try:
		with open(sys.argv[1] , 'r') as file:
			with open("hashed.txt", "w") as new_file:
				for line in file:
					new_file.write(line.strip())
					new_file.write(" -> ")
					new_file.write(hashlib.sha256(line.encode()).hexdigest())
					new_file.write("\n")
	except FileNotFoundError:
		print("File does not exict.")
else:
	print("Please enter the file name that you want to be hashed.")
