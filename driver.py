
input_text = [None,]
with open("INPUT.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = filter(None, content)
for x in content:
    x = x.split()
    x = [int(y) for y in x]
    input_text.insert(x[0], x[1])

