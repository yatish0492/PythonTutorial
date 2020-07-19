'''

'''

names = ("Yatish", "Jeshwanth", "Gagan")
companies = ("Expedia", "HP", "IBM")


zipped = zip(names, companies)

setOfThem = set(zipped) # Output --> {('Yatish', 'Expedia'), ('Gagan', 'IBM'), ('Jeshwanth', 'HP')}

dictionaryOfThem = dict(zipped) # Output --> {'Yatish': 'Expedia', 'Jeshwanth': 'HP', 'Gagan': 'IBM'}

print(setOfThem)