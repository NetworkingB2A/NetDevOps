def my_dect(function_name):
    def temp(*args, **kwargs):
        print("function starting")
        function_name(*args, **kwargs)
        print("function done")
    return temp


@my_dect
def my_name(person_name = "adam"):
    print(f"your name is {person_name}")


my_name("bill")
my_name("frank")