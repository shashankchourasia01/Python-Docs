def sum_all(*args):
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))




def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))