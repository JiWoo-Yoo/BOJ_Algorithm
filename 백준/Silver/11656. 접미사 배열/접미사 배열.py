s = input()
jms = []
for i in range(len(s)):
    jms.append(s[i:])

jms.sort()

for jm in jms:
    print(jm)
