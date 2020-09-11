import random


def check_sum_digit(number):

    card_digits = number
    check_sum = 0
    counter = 0

    for nums in str(number):
        digit = card_digits % 10

        if counter % 2 == 0:
            if digit * 2 > 9:
                check_sum += (digit * 2 - 9)
            else:
                check_sum += (digit * 2)
        else:
            check_sum += digit

        card_digits = int(card_digits / 10)
        counter += 1

    return check_sum * 9 % 10

def random_visa():

    prefix = 4
    body = random.randint(00000000000000, 99999999999999)
    num = int(str(prefix) + str(body).zfill(14))
    num = int(str(num) + str(check_sum_digit(num)))

    return num


def random_mc():

    prefix_choice = random.randint(1, 2)

    if prefix_choice == 1:
        prefix = random.randint(51, 55)
        body = random.randint(0000000000000, 9999999999999)
        body = int(str(body).zfill(13))
    else:
        prefix = random.randint(2221, 2720)
        body = random.randint(00000000000, 99999999999)
        body = int(str(body).zfill(11))

    num = int(str(prefix) + str(body))
    num = int(str(num) + str(check_sum_digit(num)))

    return num


def random_amex():

    prefix_choice = random.randint(1, 2)

    if prefix_choice == 1:
        prefix = 34
    else:
        prefix = 37

    body = random.randint(000000000000, 999999999999)
    body = int(str(body).zfill(12))

    num = int(str(prefix) + str(body))
    num = int(str(num) + str(check_sum_digit(num)))
