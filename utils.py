def is_prime(number):
    if number == 2 or number == 3:
        return True
    return not (number % 2 == 0 or number % 3 == 0 or number == 1)


def in_range(number):
    return 1 <= number <= 1000000


def Task(number):
    if is_prime(number):
        return "is prime"
    elif not in_range(number):
        return "number range error"

    direction = 1
    current_number = number + direction
    prime_numbers = list()
    while not len(prime_numbers) == 2:

        if not in_range(current_number):
            direction = -direction
            current_number = number + direction

        if not(current_number in prime_numbers) and is_prime(current_number):
            prime_numbers.append(current_number)
            direction = -direction
            current_number = number + direction
        else:
            current_number += direction
    return f"{prime_numbers[0]} {prime_numbers[1]}"


print(Task(1))
