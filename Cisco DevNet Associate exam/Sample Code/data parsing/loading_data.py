# first goal is to import the data from the different file types of data in this same folder.
# make this a little bit more programmatically correct and dont just load the file, load the path of the file.
# also use the __main__ method



import yaml
from pathlib import Path

def load_file(file_name: str) -> str:
    file = Path(__file__).parent / file_name
    print(type(str(file)))
    print(str(file))
    with open(file, "r") as file_to_read:
        file_data = file_to_read.read()


    return file_data


def main():
    print("working")


if __name__ == "__main__":
    print(load_file("data_load.yaml"))
    print(type(load_file("data_load.yaml")))
    main()


