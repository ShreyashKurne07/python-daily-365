def required_final_sgpa(current_cgpa, target_cgpa, semesters_completed=6):
    total_current = current_cgpa * semesters_completed
    target_total = target_cgpa * 8
    return round((target_total - total_current) / (8 - semesters_completed), 2)

target = 8.5
current = 8.1
req_sgpa = required_final_sgpa(current, target)
print(f"SPPU Final Year Target - Required SGPA for next 2 sems: {req_sgpa}")
