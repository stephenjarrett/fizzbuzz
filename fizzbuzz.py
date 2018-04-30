
def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(fizzbuzzprint())
        elif num % 3 == 0:
            print(fizzprint())
        elif num % 5 == 0:
            print(buzzprint())
        else: 
            print(num)
    return

def fizzprint():
    message = 'Fizz'
    return message
def buzzprint():
    message = 'Buzz'
    return message
def fizzbuzzprint():
    message = 'FizzBuzz'
    return message

fizzbuzz()