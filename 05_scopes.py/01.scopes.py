def f1():
    x=44
    def f2():
        print(x)
    f2()
f1()



def chai(num):
    def actual(x):
        return x ** num
    return actual



f = chai(2)
g = chai(3)

print(f(4))
print(f(4))