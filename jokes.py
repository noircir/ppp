import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="green")
print(colored_ascii)

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
r = requests.get(url,
                 headers={"Accept": "application/json"},
                 params={"term": topic}
                 )
data = r.json()

num_jokes = data['total_jokes']

if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {topic}. For example: \n")
	print(colored(choice(data["results"])["joke"], color="magenta"))
elif num_jokes == 1:
	print(f"There is only one joke about {topic}. Here it is: \n")
	print(colored(data['results'][0]['joke'], color="yellow") + "\n")
else:
	print(colored(f"Sorry, I don't have any jokes about {topic}", color="blue"))


