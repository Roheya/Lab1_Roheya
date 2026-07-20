#!/usr/bin/python3
import sys

def grade_evaluator(filename):
    assignments = []
    try :
        with open(filename) as f:
            lines = f.redlines()
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
            "weight":: weight
        })
# grade validation
for row in assignments:
    if score < 0 or score > 100:
        print(f"Invalid score {score} in {row["assignment""])        
