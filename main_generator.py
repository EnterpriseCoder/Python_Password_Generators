import crypt
from hmac import compare_digest as compare_hash
import string
import random

# Password Generator By Arda Duman
def StrongPassword():
    plaintext = input('username please : ')
    hashed = crypt.crypt(plaintext)
    print(hashed)

def long_password():
    my_pass_list = string.ascii_letters,string.hexdigits,string.punctuation
    my_password = ''.join(random.choice(my_pass_list)*2 for x in range(int(random.randint(10,14))))
    hashed = crypt.crypt(my_password)

    if my_password.islower() != True and my_password.isupper() != True and my_password.isprintable() == True:
        print(my_password)
    else:
        print('sorry')

def My_Password():
    uniqueness = int(input('input uniqueness of characters input between 0-100'))
    power = int(input('input how powerfull password you want input between 6-25'))

    my_list = ()
    for x in range(uniqueness):
        extreme = random.choice(string.ascii_letters),random.choice(string.hexdigits),random.choice(string.punctuation)
        my_list += extreme
        
    my_password = ''.join((random.choice(my_list) for x in range(power)))
    print('we have combined {0} different characters for this time. '.format(len(my_list)))
    if my_password.islower() != True and my_password.isupper() != True and my_password.isprintable() == True:
        print(my_password)
    else:
        print('sorry')


def BasicPass():
    my_pass_list =string.hexdigits
    my_password = ''.join((random.choice(my_pass_list) for x in range(8)))
    print(my_password)

print('hello choose one of BasicPass , RegularPassword, StrongPassword ')

x = input('1 for basic 2 for regular 3 for strong 4 for long password')
if x == '1':
    BasicPass()
elif x == '2':
    My_Password()
elif  x == '3':
    StrongPassword()
elif x == '4':
    long_password()
else:
    print('please input between 1 and 3')