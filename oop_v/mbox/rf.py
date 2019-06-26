file_name = "mbox.txt"

data = "X-DSPAM-Probability: "

out = open("out.txt", "w")
persons = {}
x = 0


for lines in open(file_name, "r"):
    if data in lines:
        x += float(lines[21:])
print(x)
