file = open("log.txt")

lines = file.readlines()

errors = 0
for line in lines:
    if "error" in line:
        errors += 1

print("Errors found:", errors)

file.close()
