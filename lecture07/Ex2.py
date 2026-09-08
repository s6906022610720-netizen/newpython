# Sample data structure for employee performance
performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

# 1. Calculate the average performance score for each employee.
averages = {}
for dept, employees in performance_data.items():
    averages[dept] = {}
    for name, scores in employees.items():
        averages[dept][name] = sum(scores) / len(scores)

# 2. Identify the top performer in each department based on their average score.
top_performers = {}
for dept, emp_avgs in averages.items():
    top_name = max(emp_avgs, key=emp_avgs.get)
    top_performers[dept] = (top_name, emp_avgs[top_name])

# 3. Determine the department with the highest average performance score.
dept_averages = {
    dept: sum(emp_avgs.values()) / len(emp_avgs)
    for dept, emp_avgs in averages.items()
}
best_dept = max(dept_averages, key=dept_averages.get)

# 4. Find employees who have shown continuous improvement.
improving_employees = []
for dept, employees in performance_data.items():
    for name, scores in employees.items():
        if all(scores[i] < scores[i + 1] for i in range(len(scores) - 1)):
            improving_employees.append(f"{name} ({dept})")

# 5. Generate a summary report.
print("Summary Report")
print("=" * 40)
for dept, employees in performance_data.items():
    print(f"\nDepartment: {dept}")
    print(f"  Department average: {dept_averages[dept]:.2f}")
    print(f"  Top performer: {top_performers[dept][0]} ({top_performers[dept][1]:.2f})")
    for name, scores in employees.items():
        trend = "Improving" if f"{name} ({dept})" in improving_employees else "No clear trend"
        print(f"  - {name}: scores={scores}, avg={averages[dept][name]:.2f}, {trend}")
print("\nOverall best department:", best_dept)