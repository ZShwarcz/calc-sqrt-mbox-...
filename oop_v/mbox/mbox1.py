import re

def get_email():
    input_file = open("mbox.txt", mode='r', encoding="utf-8")
    output_file = open("emails.txt", mode='w', encoding="utf-8")
    email_temp = "From: "

    for line in input_file:
        if email_temp in line:
            output_file.write(line[6:])
    input_file.close()
    output_file.close()

def count_email():
    read_file = open("emails.txt", mode='r', encoding="utf-8")

    result = open("result.txt", mode="w", encoding="utf-8")

    file_file = read_file.read().lower()

    match_pattern = re.findall(r"[\w._-]+@[\w._-]+\.[\w.]+", file_file)

    frequency = {}

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        result.write(words + "\t\t" + str(frequency[words]) + "\n")

def average_value():
    op = open("mbox.txt", mode='r', encoding="utf-8")
    temp = "X-DSPAM-Confidence: "
    count = value = 0
    for line in op:
        if temp in line:
            count +=1
            value += float(line[20:])
    print("Average X-DSPAM-Confidence: " + str(value / count))
    op.close()


get_email()
count_email()
average_value()








