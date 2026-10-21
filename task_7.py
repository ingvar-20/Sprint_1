def sum_digits(num):
    total = 0
    for i in range(7):
        if num > 0:
            total = total + num % 10
            num = num // 10
    return total

def digit_root(num):
    for i in range(3):
        if num < 10:
            break
        num = sum_digits(num)
    return num

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))