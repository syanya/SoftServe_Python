import math

def divisor(number):
    sum_of_divisors = 0
    for i in range(1,math.ceil(math.sqrt(number))):
        if i * i == number:
            sum += i
            break
        if number % i == 0:
            sum_of_divisors += i
            sum_of_divisors += number/i
    return sum_of_divisors

maximal = 0
number_with_maximal_sum = 0
for i in range(1,10001):
    if divisor(i) > maximal:
        maximal = divisor(i)
        number_with_maximal_sum = i
print("Number with maximal sum of divisors is ", number_with_maximal_sum)
