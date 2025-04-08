import random
import string

characters = f'{string.ascii_letters}1234567890@#$'


number_of_passwords = int(input('Enter number of passwords to be generated: '))
length_of_passwords = int(input('Input passwords length: '))

print('\nPASSWORDS:')


for pwd in range(number_of_passwords):
  password = ''
  for c in range(length_of_passwords):
    password += random.choice(characters)
  print(password)