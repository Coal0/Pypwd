#!/usr/bin/env python
import base64, random, hashlib #import the necessary modules


def hashPwd(pwd):
	'''Use SHA512 to hash the password'''
	h = hashlib.sha512()
	byte_pwd = str.encode(pwd)
	h.update(byte_pwd)
	hashed_pwd = h.hexdigest()
	return hashed_pwd

def base64_encode(hashed_pwd):
	'''Encode the resulting hashed pass in base644 to increase length and complexity'''
	byts = str.encode(hashed_pwd)
	b64_1 = base64.b64encode(byts)
	b64_2 = base64.b64encode(b64_1)
	b64_3 = base64.b64encode(b64_2)
	b64_4 = base64.b64encode(b64_3)
	return b64_4

def select_range(b64_string, length, seed, sym_num = 4):
	'''Select a slice of the huge final base64 string '''
	random.seed(seed)
	begin = random.randint(0, len(b64_string) - length - 1)
	chosen_slice = b64_string[begin:begin + length - sym_num]
	decoded_slice = chosen_slice.decode()
	return list(decoded_slice)

def sym_insert(pwd_slice, seed, sym_num = 4):
        '''insert a couple special characters into the pass'''
        syms = "!@#$%^&*()_+\\|\"}{][/.?>,<`'"
        random.seed(seed)
        for i in range(sym_num):
                rand_pos = random.randint(0, len(pwd_slice) - 1)
                rand_char = random.choice(syms)
                pwd_slice.insert(rand_pos, rand_char)

        return ''.join(pwd_slice)


if __name__ == "__main__":
        print('\n\n    ##############A Python script to boost password strength #################')
        print('    #               Secure passwords must be strings of                      #')
        print('    #           random characters, but humans are bad at generating          #')
        print('    #              random things, and , truly random strings                 #')
        print('    #           are tricky to remember and impossible to reproduce.          #')
        print('    #             So I wrote this tool to solve the above problem.           #')
        print('    #                     All you will have to remember is                   #')
        print('    #                      the initial password (eg: John),                  #')
        print('    #        a multiplication key (a number), a password seed (a number)     #')
        print('    #          the number of special characters to insert, and of course     #')
        print('    #             the length of the final password to be generated.          #')
        print('    #                      Hope it proves useful to you!                     #')
        print('    #######################################################################\n\n')

        pwd = input("Enter your password: ")
        mult_key = input("\nEnter a multiplication key (or leave blank to use 1): ")
        try:
                key = int(mult_key)
        except ValueError:
                key = 1
        new_pwd = pwd * key
        hashed_pwd = hashPwd(new_pwd)
        b64_string = base64_encode(hashed_pwd)
        length = int(input("\nEnter the desired password length (should be less than %s): " % len(b64_string)))
        seed = int(input("\nEnter a password seed (any number greater than 0): "))
        num = input("\nEnter the number of special characters to insert or leave blank " \
                  + "if you don't want to insert any special characters (not recommended): ")
        try:
                sym_num = int(num)
        except ValueError:
                sym_num = 0
        pwd_slice = select_range(b64_string, length, seed, sym_num)
        final_pwd = sym_insert(pwd_slice, seed, sym_num)
        print("The final password is: %s" % final_pwd)
