# Hermes?
# Mercury?
# Marathon?
# Pheidippides?
# Revere?

import string


def user_interface():
		print("\nWelcome to <program name>.")
# <future>
#		print("\nPlease select an option from the menu:\n\n")
#		print("1) Send A Message")
#		print("2) View Received Messages")
#		print("3) Manage Keys\n")
#
#		if selection == "1":
#			print("1")
#
#		if selection == "2":
#			print("2")
#
#		if selection == "3":
#			print("3")
# </future>

#		key_file = input("Enter the filepath of your key.")
		key_file = "key.txt"
		plain_text = input("\nEnter your plaintext:\n")
		print("")

		encrypt_decrypt(plain_text, key_file)

def auto_save(temp):
# Save the passed text to temporary_plaintext.txt and inform the user
# of your good deed.
	temp_save = open("temporary_plaintext.txt", "w")
	temp_save.write(temp)
	temp_save.close()
	print("\nFor your convenience, the text that you entered")
	print("has been stored in the same directory as this program")
	print("as temporary_plaintext.txt\n")


def check_key_len(plain_text, key_file):
	chars = 0

# Iterate over each line in the key file to determine the number of
# usable characters.
	with open(key_file, "r") as key_file_in:
		for line in key_file_in:
			chars += len(line)

# If the entered plaintext is longer than the key, do not proceed.
# Inform the user that they must get a new key.
	if(len(plain_text) > chars):
		print("\n!!! Operation Failed !!!\n")
		print("The size of your plaintext message exceeds the number")
		print("of availible characters left in your key. Please")
		print("contact your crypto administrator to be issued a new")
		print("key.\n")

# This isn't their fault! They shouldn't be punished by losing all of
# their hard work. Save their work for them.
		auto_save(plain_text)

		return 0

	else:
		return 1

def check_plaintext_len(plain_text, key_file):
# From multiple tests, the method employed to pull N characters of a
# key from a file seems to only be reliable to about 5k characters
# and some change. Verify that the plaintext does not exceed this.
	if(len(plain_text) > 5000):
		print("\n!!! Operation Failed !!!\n")
		print("Please limit plaintext input to 5000 characters or")
		print("less./n")

# Be nice and save their work for them. Even if they won't learn
# anything this way.
		auto_save(plain_text)

		return 0

	else:
		return 1

def reconcile_key(key_file, idx_to_slice):
# Open the key file and read
	try:
		key_file_in = open(key_file, "r")
		full_key = key_file_in.read()

# Slice the passed number of characters
		new_key = str(full_key[int(idx_to_slice):])
		key_file_in.close()

# Re-open the file and overwrite it with the sliced key
		key_file_out = open(key_file, "w")
		key_file_out.write(new_key)
		key_file_out.close()
	except OSError as e:
		print(e.errno)

def encrypt_decrypt(plain_text, key_file):
# Check to make sure that the plaintext is less than 5k characters.
	if check_plaintext_len(plain_text, key_file) == 0:
		raise SystemExit(0)

# Check to ensure adequate key length to accomodate plaintext.
	if check_key_len(plain_text, key_file) == 0:
		raise SystemExit(0)

# If both succeeed, grab a number of characters from the beginning
# of the key file that corresponds with the number of characters in the
# plaintext
	try:
		key_file_in = open(key_file, "r")
		key = key_file_in.read(len(plain_text))
		key_file_in.close()

# XOR plain_text against key
		output_text = "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(plain_text,key)])

# Write the output to a file
		output_file = open("output.txt", "w")
		output_file.write(output_text)
		output_file.close()

# Remove the used portion of the key
		reconcile_key(key_file, len(key))

		print("Operation successful!\n")
		print("Your output has been saved in the same directory as")
		print("this program as output.txt\n")
	except OSError as e:
		print(e.errno)


user_interface()
