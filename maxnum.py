
num = int(input("inter numbers: "))
num = abs(num)  


max_digit = 0

while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10

print("maxnum:", max_digit)
