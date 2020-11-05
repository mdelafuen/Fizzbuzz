# solution to the Fizzbuzz problem
# written by Maria De La Fuente

def main():
    number = 1
    for i in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        else:
            print(number)
        number += 1



main()