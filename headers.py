import requests
from pyfiglet import figlet_format
from termcolor import colored

url = "https://icanhazdadjoke.com/"
r = requests.get(url, headers ={"Accept": "application/json"} )
data = r.json()

ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="green")
print(colored_ascii)

print(colored(data['joke'], color="yellow") + "\n")