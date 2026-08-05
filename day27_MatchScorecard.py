players = [("Rohit",45), ("Kohli",82), ("Pant",55), ("Bumrah",0), ("Gill",120), ("Iyer",33)]

#Top scorer — name and runs. Find using a loop, don't use max().
#Total team runs
#Average runs per player, rounded to 2 decimals
#How many players scored 50+ (fifties)
#Name(s) of any player who scored a duck (0 runs)


total_runs = 0
scored_fifty = 0
scored_duck = []

top_score = 0
top_name = ""



for i in players:
	total_runs = total_runs + i[1]

	if (i[1]>=50):
		scored_fifty += 1

	if (i[1] == 0):
		scored_duck.append(i[0])

	if (i[1] > top_score):
		top_score = i[1]
		top_name = i[0]


avg_runs = (total_runs / len(players))
print("Avg Runs:",round(avg_runs,2))

print("Total Team Runs:",total_runs)
print("No. of players who scored 50",scored_fifty)
print("Player who scored Duck:",scored_duck)
print("Top Scorer:",top_name,top_score)



