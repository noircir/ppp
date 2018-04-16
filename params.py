import requests
import random
from pyfiglet import figlet_format
from termcolor import colored

count = 0

ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="green")
print(colored_ascii)

url = "https://icanhazdadjoke.com/search"
topic = input("Let me tell you a joke! Give me a topic: ")

# try:

r = requests.get(url,
                 headers={"Accept": "application/json"},
                 params={"term": topic}
                 )
data = r.json()
if len(data) >= 1:
	if len(data) == 1:
		print(f"Sorry, I don't have any jokes about {topic}")
	else:
		for item in data['results']:
			count+=1

	print(f"I've got {count} jokes about {topic}. Here's one: " + "\n")

	random_index = random.randint(0, count-1)
	print(colored(data['results'][random_index]['joke'], color="yellow") + "\n")
else:
	print(f"Sorry, I don't have any jokes about {topic}")


 
	
