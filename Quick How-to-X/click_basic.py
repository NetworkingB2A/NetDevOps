import click
# Quick example of using argparse
VERSION = "0.1.0"

@click.command()
@click.version_option(VERSION, message=f"Version: {VERSION}") # python click_basic.py --version
@click.argument("names", nargs=2)
@click.argument("age", nargs=1)
@click.option("-e", "--extra", type=str, default=None, help="type anything string you want in quotations.") #python click_basic.py Young buck 100 -e "This is the extra data you asked for."
@click.option("-s", "--shout", is_flag=True, help="Special feature if you want to yell.") #python click_basic.py Young buck 100 -e "This is the extra data you asked for. -s"
def say_hello(names:str = None, age:int = None, extra:str = None, shout:bool = None):
    """
To use this script your will need to enter your first name and you last name, followed by your age.\n
EXAMPLE:\n
python click_basic.py Young buck 100

OUTPUT:\n
Hello Young buck,

Young buck how are you?

I would guess you are 100 years old.
    """
    text = f"Hello {' '.join(names)},\n{' '.join(names)} how are you?\nI would guess you are {int(age)} years old."
    
    if shout:
        print(text.upper())
    else:
        print(text)
    if extra and shout:
        print(extra.upper())
    elif extra:
        print(extra)
    else:
        pass
    
    


    

 
def main():
    print("this is main")
    


if __name__ == "__main__":
    say_hello()
