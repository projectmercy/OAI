#Script used to remove User responses from a copy/pasta of ChatGPT frontend conversation

import os

filename = r"C:\Users\Kafeel\Desktop\gohan park.txt"
output_filename = os.path.splitext(filename)[0] + "_parsed.txt"

with open(filename, "r") as f:
    lines = f.readlines()

responses = []

for i in range(len(lines)-1):
    if "Michael Davis" not in lines[i] and "?" not in lines[i+1]:
        response = lines[i+1].strip()
        responses.append(response)

with open(output_filename, "a") as f:
    for response in responses:
        f.write(response + "\n")
