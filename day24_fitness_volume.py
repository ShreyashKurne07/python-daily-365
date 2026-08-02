def calculate_volume(sets, reps, weight):
    return sets * reps * weight

workout_log = {
    "Bench Press": (4, 8, 70),
    "Squat": (4, 6, 100),
    "Deadlift": (3, 5, 120)
}

total_tonnage = sum(calculate_volume(s, r, w) for s, r, w in workout_log.values())
print(f"Total Workout Volume: {total_tonnage} kg")
