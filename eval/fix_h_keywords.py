with open('/Users/andrew/Documents/AAAPPS5/OpenClaw/eval/run_phase_h.py', 'r') as f:
    lines = f.readlines()

new_lines = []
in_score_h = False
for i, line in enumerate(lines):
    if "def score_h_keywords" in line:
        in_score_h = True
        
    if in_score_h and "msg = f\"{correct}/{total} correct\"" in line:
        in_score_h = False
        
    if in_score_h:
        pass # we will rewrite it wholesale
    else:
        new_lines.append(line)

new_func = """def score_h_keywords(content, scoring):
    \"\"\"Score by checking if the expected keyword strings are present in the output text.\"\"\"
    answers = scoring.get("answers", {})
    if not answers:
        return 0, 0, "No answers defined."
    total = len(answers)
    text = content.lower()
    import re
    correct = 0
    wrong = []
    
    for key, expected in answers.items():
        kw_lower = str(expected).lower()
        if kw_lower == "yes":
            # For boolean constraints, check if the key's words are in the text
            words = [w for w in key.replace("_", " ").split() if len(w) >= 3]
            if words and all(w in text for w in words):
                correct += 1
            else:
                wrong.append(f"#{key}: missing")
            continue
            
        # Strip L12: prefixes from kw_lower
        kw_clean = re.sub(r'l\d+:\s*', '', kw_lower)
        if kw_clean in text:
            correct += 1
        elif kw_clean.replace("→", "->") in text:
            correct += 1
        else:
            words = [w for w in kw_clean.replace("/", " ").replace("→", " ").replace("-", " ").split() if len(w) > 3]
            if words and all(w in text for w in words):
                correct += 1
            else:
                wrong.append(f"#{key}: missing {expected}")
                
    msg = f"{correct}/{total} correct"
"""
# insert before the line that comes after score_h_keywords
idx = sum(1 for line in new_lines if "def score_h_content_planner" not in line) 
idx = next(i for i, line in enumerate(new_lines) if "def score_h_content_planner" in line)

new_lines.insert(idx, new_func)

with open('/Users/andrew/Documents/AAAPPS5/OpenClaw/eval/run_phase_h.py', 'w') as f:
    f.writelines(new_lines)
