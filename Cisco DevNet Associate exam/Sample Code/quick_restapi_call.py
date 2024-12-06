import requests
import os

username = os.getenv("username") if os.getenv("username") is not None else input("Please enter your Username: ")
password = os.getenv("PASSWORD")



response = requests.get(url="https://api.chucknorris.io/jokes/random", verify=False)

print(response.json()['value'])