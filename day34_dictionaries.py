
scores = {"Rohit": 45, "Kohli": 82, "Pant": 55, "Bumrah": 0, "Gill": 120}

'''
Print:
All player names
All scores
Total runs
Name of highest scorer (no max())
Players who scored above 50 — as a list


Names: ['Rohit', 'Kohli', 'Pant', 'Bumrah', 'Gill']
Scores: [45, 82, 55, 0, 120]
Total: 302
Highest: Gill
Above 50: ['Kohli', 'Pant', 'Gill']

'''

list1 = scores.keys()
print("Names:",list(list1))

list2 = scores.values()
print("Scores:",list(list2))
total_runs = 0


total_runs = sum(list2)
print("Total:",total_runs)

highest_score = 0
best_player = ""

above_50 = []
for name,score in scores.items():
	if score > highest_score:
		highest_score = score
		best_player = name

	if score > 50:
		above_50.append(name)

print("Highest:",best_player)
print("Above 50:",above_50)


