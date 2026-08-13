team_scores = {
    "Mumbai": [45, 82, 30, 12, 60],
    "Chennai": [70, 25, 90, 40, 15],
    "Bangalore": [55, 35, 20, 80, 65]
}

'''
Total runs for each team
Which team scored the most in total
Highest individual score across all teams, and which team it came from
Average per team, rounded to 2 decimals

Mumbai total: 229
Chennai total: 240
Bangalore total: 255
Top team: Bangalore
Highest individual: 90 (Chennai)
Mumbai avg: 45.8
Chennai avg: 48.0
Bangalore avg: 51.0
'''

top_team = ""
highest_team_total = 0

best_individual_team = ""
highest_individual = 0

for team,scores_list in team_scores.items():
	team_total = sum(scores_list)
	print(team, "total:", team_total)

	if team_total > highest_team_total:
		highest_team_total = team_total
		top_team = team

	team_best_score = max(scores_list)

	if team_best_score > highest_individual:
        	highest_individual = team_best_score
        	best_individual_team = team

print("Top team:", top_team)
print("Highest individual:", highest_individual, "(" + best_individual_team + ")")


for team, scores_list in team_scores.items():
    team_avg = sum(scores_list) / len(scores_list)
    print(team, "avg:", round(team_avg, 2))
