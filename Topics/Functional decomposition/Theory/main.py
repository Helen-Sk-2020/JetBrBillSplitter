#  You can experiment here, it won’t be checked
def calculate(amount, interest_rate, time):
    interest = float(amount * interest_rate * time / 100)
    total_amount = float(amount + interest)
    return interest, total_amount


def print_result(interest, total_amount):
    print(f'The interest is: {interest}')
    print(f'The total amount is: {total_amount}')
