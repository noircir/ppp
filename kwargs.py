def fav_colors(**kwargs):
	print(kwargs)
	for person, color in kwargs.items():
		print(f"{person.upper()}'s favorite color is {color}	")

fav_colors(elena="green", colt="royal deep amazing purple", ruby="red")