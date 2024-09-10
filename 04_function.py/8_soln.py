def print_kwargs(**kwargs):
    for key , value in kwargs.items(): 
        print(f"{key} : {value}")

print_kwargs(name = "shashank" , power = "lazer")

print_kwargs(name = "shashank" )

print_kwargs(name = "shashank" , power = "lazer" , enemy = "me")