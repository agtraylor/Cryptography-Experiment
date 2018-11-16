# time is only used for debugging and performance testing
#import time
import secrets
import string

# start_time is only used for debugging and performance testing
#start_time = time.time()

alphabet = string.ascii_letters + string.digits

print("\nGenerating key file.")
print("Please note that this could take up to 1 minute.\n")

OTP_Key = ''.join(secrets.choice(alphabet) for i in range(10000000))

Key_File = open("key.txt", "w")
Key_File.write(OTP_Key)
Key_File.close()

print("\nYour key has been generated. It is in the directory of this program")
print("and is named key.txt\n")

# This print function is only used for debugging and performance testing
#print("--- %s seconds ---" % (time.time() - start_time))