balls = ["1", "0", "4", "wd", "2", "W", "6", "0", "1", "nb", "4", "3"]


balls = ["1", "0", "4", "wd", "2", "W", "6", "0", "1", "nb", "4", "3"]

# Total Team Runs
total_runs = 0
wickets = 0
legal_balls = 0
fours = 0
sixes = 0
runs_off_bat = 0

for i in balls:
    if i.isdigit():
        total_runs = total_runs + int(i)
        legal_balls += 1
        runs_off_bat = runs_off_bat + int(i)

        if i == "4":
            fours += 1
        elif i == "6":
            sixes += 1
            
    elif i == "wd":
        total_runs = total_runs + 1

    elif i == "nb":
        total_runs = total_runs + 1
        
    elif i == "W":
        wickets += 1
        legal_balls += 1


print("Total runs:", total_runs)
print("Wickets:", wickets)
print("Legal balls:", legal_balls)
print("Fours:", fours)
print("Sixes:", sixes)

strike_rate = (runs_off_bat / legal_balls) * 100
print("Strike rate: ", round(strike_rate, 2))
# Wickets Fallen

# Legal balls bowled
# Number of fours
# Number of sixes
# Strike rate
