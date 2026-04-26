import re
import os

ids_to_fix = [6, 11, 15, 19, 29, 33, 35, 37, 39, 44, 46, 50, 51, 52, 53, 54, 59]

files = ["batch2.py", "batch3.py", "batch4.py", "batch5.py", "batch6.py"]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # We will find the blocks for each id and replace "json_values" -> "h_keywords"
    for current_id in ids_to_fix:
        # Regex to find the id definition and the following scoring_type
        pattern = re.compile(f'("id": {current_id},.*?)"scoring_type": "json_values"', re.DOTALL)
        content = pattern.sub(r'\1"scoring_type": "h_keywords"', content)
        
    with open(f, "w") as file:
        file.write(content)
print("Done fixing scorers")
