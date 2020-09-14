# Author: William Dam
# Date: 09-11-2020
# Description: Random credit card number generation functions for Visa, MasterCard
# and Amex.  For research and development purposes only, numbers generated have
# valid prefixes and checksums, but will obviously not work through the credit card
# interchange network.
import random


#######################################################################
# Description: Helper function returns valid checksum for cc number.
# Uses Luhn algorithm.
# Arguments: String of credit card number without last digit
# Returns: Checksum for credit card number arg, as a single int
#######################################################################
def check_sum_digit(number):

    card_digits = number    # Holds incomplete card number passed from arg
    check_sum = 0           # Holds final checksum value
    counter = 0             # Track which digit is being calculated

    # Go through each digit of number passed in, right to left
    for nums in str(number):

        # Get last digit of card number
        digit = card_digits % 10

        # Apply function to every other digit using counter mod 2
        if counter % 2 == 0:
            if digit * 2 > 9:
                check_sum += (digit * 2 - 9)
            else:
                check_sum += (digit * 2)
        else:
            check_sum += digit

        # Remove last card digit
        card_digits = int(card_digits / 10)

        # Increment counter
        counter += 1

    # Return check sum
    return check_sum * 9 % 10


#######################################################################
# Description: Random Visa number generator
# Arguments: None
# Dependencies: check_sum_digit(number)
# Returns: Random valid Visa number as int
#######################################################################
def random_visa():

    # Set card number prefix 4
    prefix = 4

    # Generate random number
    body = random.randint(00000000000000, 99999999999999)

    # Concatenate leading zeros
    body = int(str(body).zfill(14))

    # Concatenate prefix
    num = int(str(prefix) + str(body))

    # Concatenate check digit
    num = int(str(num) + str(check_sum_digit(num)))

    # Return complete Visa card number
    return num


#######################################################################
# Description: Random MasterCard number generator
# Arguments: None
# Dependencies: check_sum_digit(number)
# Returns: Random valid MasterCard number as int
#######################################################################
def random_mc():

    # Randomly choose a prefix option
    prefix_choice = random.randint(1, 2)

    # Prefix [51, 55]
    if prefix_choice == 1:

        # Set prefix in range
        prefix = random.randint(51, 55)

        # Generate random number
        body = random.randint(0000000000000, 9999999999999)

        # Concatenate leading zeros
        body = int(str(body).zfill(13))

    # Prefix [2221, 2720]
    else:

        # Set prefix in range
        prefix = random.randint(2221, 2720)

        # Generate random number
        body = random.randint(00000000000, 99999999999)

        # Concatenate leading zeros
        body = int(str(body).zfill(11))

    # Concatenate prefix
    num = int(str(prefix) + str(body))

    # Concatenate check digit
    num = int(str(num) + str(check_sum_digit(num)))

    # Return complete MasterCard number
    return num


#######################################################################
# Description: Random Amex number generator
# Arguments: None
# Dependencies: check_sum_digit(number)
# Returns: Random valid Amex number as int
#######################################################################
def random_amex():

    # Randomly choose prefix choice option
    prefix_choice = random.randint(1, 2)

    # Assign prefix number
    if prefix_choice == 1:
        prefix = 34
    else:
        prefix = 37

    # Generate random number
    body = random.randint(000000000000, 999999999999)

    # Concatenate leading zeros
    body = int(str(body).zfill(12))

    # Concatenate prefix
    num = int(str(prefix) + str(body))

    # Concatenate check digit
    num = int(str(num) + str(check_sum_digit(num)))

    # Return complete Amex number
    return num
