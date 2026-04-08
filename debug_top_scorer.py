scores = {}
while True:
    user_input = input("Enter player and score as 'name score' (or type 'stop' to finish):\n")
    if user_input.lower() == "stop":
        break
    parts = user_input.split()
    name = parts[0]
    score = int(parts[1])
    if name in scores:
        scores[name] += score
    else:
        scores[name] = score
if len(scores) == 0:
    print("No scores recorded.")
else:
    top_name = ""
    top_score = -1
    for name in scores:
        if scores[name] > top_score:
            top_score = scores[name]
            top_name = name
    print(f"Top scorer: {top_name} with {top_score} points.")
