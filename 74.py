def multiple_add(*args):
    total = 0
    for number in args:
        total += number
    return total

result = multiple_add(1,2,3,4,5,6,7,8,9,10,11)
print(result)