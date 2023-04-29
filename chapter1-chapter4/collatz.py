# Write your code here :-)
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
print("Enter number:")
try:
    num = int(input())
    while True:
        num = collatz(num)
        if num == 1:
            break

except ValueError:
    print("You must enter an integer.")

