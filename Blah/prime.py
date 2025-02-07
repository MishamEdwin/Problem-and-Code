"""2 3 5 7"""
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

n=10

for nums in range(1,n+1):
    print(nums,is_prime(nums))

