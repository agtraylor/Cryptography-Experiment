This is a proof of concept for a secure OTP cryptography engine. It will
eventually be used to build an instant messaging platform.

Note: Engine.py and Key_Gen.py should be in the same directory

To use this, first run "Key_Gen.py". This will take from 20 seconds to 1 minute,
depending on current system load. This will produce a file called "key.txt" in
the same directory as "Key_Gen.py" This key is 10,000,000 bytes of secure random
data generated using Python's "secrets" module.

Next, run "Engine.py". You will be prompted to enter some plaintext. Do so and
press enter. This will create a file in the same directory as "Engine.py" named
"output.txt". This is your encrypted or decrypted text. Encryption and
decryption are achieved in the same way, as the only method used is XORing
against your key file.

Now, if you open "key.txt", you will notice that it is now shorter. The first
len(plaintext) characters have been sliced from the key, so that the same key
can be used for many encryptions/decryptions.

To verify proper operation of the engine:
  1. Comment out line 130 in "Engine.py"
  2. Run "Engine.py" and enter your plaintext
  3. Copy the text from "output.txt"
  4. Run "Engine.py" again
  5. Paste the text from "output.txt" into the console and run.
  6. Verify that the text has been returned to it's original Inform
