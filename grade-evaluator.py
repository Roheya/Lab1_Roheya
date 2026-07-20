#!/usr/bin/python3
import sys

def grade_evaluator(filename):
    assignments = []
    try :
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: File '{filename}' not found.")
        return

    for line in lines[1:]:
        parts = line.split()
        if len(parts) < 4:
            continue
        weight = parts[-1]
        score = parts[-2]
        group = parts[-3]
        name = "".join(parts[:-3])
        assignments.append({
            "assignment": name,
            "group": group,
            "score": score,
            "weight": weight
        })
# grade validation

    for row in assignments:
        score = int(row["score"])
        if score < 0 or score > 100:
            print(f"Invalid score {score} in {row['assignment']}")

#weight validation 
    total_weight = sum(int(row["weight"]) for row in assignments)
    if total_weight == 100:
        print("the sum of the assignment weight is exactly 100")
    else:
        print("Error: the total weight must equal to 100")
    

    #Ensuring that the formative weight adds up to 60
    formative_weight = 0
    for row in assignments:
        if row["group"] == "Formative":
            weight = int(row["weight"])
            formative_weight += weight
    print(f"the formative assignment adds up to {formative_weight}")
    
    # Ensuring that the summative weight adds up to 40
    summative_weight = 0
    for row in assignments:
        if row["group"] == "Summative":
            weight = int(row["weight"])
            summative_weight += weight
    print(f"the summative assignments adds up to {summative_weight} exactly")



grade_evaluator("grades.csv")
