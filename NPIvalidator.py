import math
import fileinput
import os


def modulo_10(x):
    """Get the nearest rounded up number multiple of 10"""
    return int(math.ceil(x / 10.0)) * 10


def to_list(_str):
    """
    Converts a string of digits to a list of strings
    Example:
    >>>> to_list("0123456789")
    >>>> list(0,1,2,3,4,5,6,7,8,9)
    :param _str: (str) iput string, should be numerical only
    :return: (list) a list of digits (e.g. integers)
    """
    return [int(digit) for digit in str(_str)]


def to_string(_list):
    """Converts a list of integers to a string of digits"""
    return ''.join([str(digit) for digit in _list])


def to_digits(_list):
    """Converts a list of integers to a list of digits"""
    return to_list(to_string(_list))


def parse_luhn(luhn_input):
    _list = to_list(luhn_input) if isinstance(luhn_input,str) else luhn_input
    try:
        luhn_list = _list[0:9]
        checkdigit = _list[9]
        check = False if len(_list) <> 10 else True
    except (IndexError, TypeError) as e:
        luhn_list = None
        checkdigit = None
        check = False
    return luhn_list, checkdigit, check

def is_luhn_valid(luhn_string):
    luhn_list, check_digit, valid_check = parse_luhn(luhn_string)
    check_actual = 999
    if valid_check :
        left_digits = luhn_list[-2::-2]
        right_digits = luhn_list[-1::-2]
        double_alternate_digits = to_digits([e*2 for e in right_digits])
        checksum  = sum(double_alternate_digits + left_digits)
        modulo    = modulo_10(checksum)
        check_actual = modulo - checksum
        #print luhn_string, checksum, modulo, check_actual
    return check_actual == check_digit


# Step 1: Check if the length of NPI number is of 10 digits
# Step 2: If correct, seperate check digit from Luhn number - Check Digit is 10th Digit and Luhn Number = first 9 Digits
# Step 3: Define Luhn Checksum Function, input is a 9 digit Luhn number and output is checkdigit. 
# Step 3a: Extract right alternate digits, left alternate digits
# Step 3b: Double the value of right alternate digits and add them together
# Step 3d: Add the result from Step 3b, 3c to form the checksum
# Step 3e: do the modulo 10 of the checksum and subtract the actual check sum to get the actual check digit
# Step 3f: Compate the check digit from Step 3e to the given check digit, if they are equal then NPI is correct otherwise incorrect.

npi_list=[]
input_file='npiinput.txt'

with open(input_file,'r') as in_file: 
    lines = in_file.readlines()
    npi_list = [ w.strip() for w in lines ] 

print npi_list
os.remove('npioutput.txt')
outputfile = 'npioutput.txt'
with open(outputfile, 'w') as out_file:
    for x in npi_list:
        is_luhn_valid(x)
        out_file.write('\t'.join([x, str(is_luhn_valid(x)), '\n']))