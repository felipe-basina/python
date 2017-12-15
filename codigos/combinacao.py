def combinar():
	dict = {'a':0, 'b':1, 'c':2}
	new_dict = {b:a for a, b in dict.items()}
	data = [2, 0, 5, 1, 0]
	final_data = [''.join([new_dict[a%3] for a in data])]
	print(final_data)

if __name__ == "__main__":
	combinar()