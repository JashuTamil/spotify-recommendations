with open("2024_swe_internship_vibe_analysis_assignment.BIN", "rb") as f:
    data = f.readlines()

new = []

for i in data:
    temp = i.decode("ASCII")
    new.append(temp)

print(new[0])