import typer

app = typer.Typer()

@app.command()
def hello( name:str, age:int):
    print(f"Hello {name},\n{name} how are you?\nI would guess you are {int(age)} years old.")
    
@app.command()
def goodbye(name:str, sound_of_silence:bool = False):
    if sound_of_silence:
        print("Hello darkness, my old friend. I've come to talk to you again.")
    else:
        print(f"Good bye, {name} my old friend, I've decided to leave this app again.")
    


if __name__ == "__main__":
    app()
