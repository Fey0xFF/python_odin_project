#import string for ascii
import string

#store user string and shift factor
plaintext = input("Please enter a sentence to encrypt: ")
shift = int(input("Please enter a shift factor: "))

#cipher function
def cipher(text, shiftfactor):
  #init key lists
  letters = list(string.ascii_lowercase[:26])
  capletters = list(string.ascii_uppercase[:26])
  ciphertext = ""

  #iterate through letter in string
  for letter in text:
    if letter in letters:
      index = letters.index(letter)
      index -= shiftfactor
      ciphertext = ciphertext + (letters[index])
    elif letter in capletters:
      index = capletters.index(letter)
      index -= shiftfactor
      ciphertext = ciphertext + (capletters[index])
    else:
      ciphertext += letter
  print (ciphertext)

#call cipher
cipher(plaintext, shift)
