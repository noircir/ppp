def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeting David!"
	elif "David" in kwargs:
		return f"{kwargs['David']} David!"
	return "Not sure who that is..."

print(special_greeting(David = 'Hello'))
print(special_greeting(Bob = 'Hello'))
print(special_greeting(David = 'special'))
print(special_greeting(Heather="Howdy", David = 'Howdy'))

	
