
import fileinput
import sys

# if any line contains this text, I want to modify the whole line.
text = "\"fecha\":"

x = fileinput.input(
    files="/Users/yashraj/Desktop/date format update/date.txt", inplace=1)
for line in x:
    if text in line:
        new_text = " \"fecha\":\"" + [t.split('-')[2] + '-' + t.split('-')[1] + '-' + t.split(
            '-')[0] for t in line.split() if t.endswith('-2021')][0] + "\","
        line = new_text
    sys.stdout.write(line)
x.close()
