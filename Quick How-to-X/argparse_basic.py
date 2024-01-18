import argparse
# Quick example of using argparse

def say_hello( name:str = None, age:int = None):
    print(f"Hello {name},\n{name} how are you?\nI would guess you are {int(age)} years old.")

 
def main():
    print("this is main")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This will take you name and age and print out something")
    parser.add_argument('name', metavar='name', type=str, help='Enter your name')
    parser.add_argument('age', metavar='age', type=str, help='Enter your age')
    args = parser.parse_args()
    
    name = args.name
    age = args.age
    
    say_hello(name= name, age= age)
