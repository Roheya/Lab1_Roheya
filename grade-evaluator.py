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
    if formative_weight == 60:
        print("the formative assignments add up to exactly 60")
    else:
        print("Error: formative weight must equal 60")
    # Ensuring that the summative weight adds up to 40
    summative_weight = 0
    for row in assignments:
        if row["group"] == "Summative":
            weight = int(row["weight"])
            summative_weight += weight
    if summative_weight == 40:
        print("the summative assignment adds up to exactly 40")
    else:
        print("Error: summative grade must equal 40")
    
    # Calculating the GPA
    sum_weighted_score = 0
    for row in assignments:
        score = int(row["score"])
        weight = int(row["weight"])
        weighted_score = score * weight
        sum_weighted_score += weighted_score
    
    Total_Grade = (sum_weighted_score)/100
    GPA = (Total_Grade/100)*5.0
    
    print(f"Total grade = {Total_Grade}")
    print(f"the final GPA is {GPA}")

    #Final decision(pass/fail)
    #checking the percentage score for formative
    formative_weighted_score = 0
    formative_weight = 0
    for row in assignments:
        if row["group"] == "Formative":
            score = int(row["score"])
            weight = int(row["weight"])
            formative_weighted_score += (score*weight)/100
            formative_weight += weight
    #percentage for formative
    formative_percentage =(formative_weighted_score/formative_weight)*100
    if formative_percentage >= 50:
        print(f"Result: PASSED with a percentage of {formative_percentage}")
    else:
        print(f"Result: FAILED with a percentage of {formative_percentage}")

    #checking percentage score for summative
    summative_weighted_score = 0
    summative_weight = 0
    for row in assignments:
        if row["group"] == "Summative":
            score = int(row["score"])
            weight = int(row["weight"])
            summative_weighted_score += (score*weight)/100
            summative_weight += weight
    summative_percentage = (summative_weighted_score/summative_weight)*100
    if summative_percentage >= 50:
        print(f"Result: PASSED with a percentage of {summative_percentage}")
    else:
        print(f"Result: FAILED with a percentage of {summative_percentage}")

    print(f"the student PASSED with a percentage of {summative_percentage} in the submmative and a percentage of {formative_percentage} in the formative")
grade_evaluator("grades.csv")
