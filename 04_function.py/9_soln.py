def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i 


for num in even_generator(20):
    print(num)

    #yield means generate karna.