"""
Docstring for finding_prime_number

Finding Prime Number 
Prime Number - Divides only by itself and 1.

"""

def finding_prime_number():

    number = input("Enter numbers with spaces: ")

    number_list = number.split()

    for i in number_list:
        num = int(i)
        if num <= 1:
            continue
        is_prime = True
        for j in range(2, num-1):
            if num % j == 0:
                is_prime = False
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")


if __name__ == "__main__":
    finding_prime_number()




