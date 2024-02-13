n = int(input())
words = set()
for _ in range(n):
    i = input()
    words.add(i)
    
words = sorted(words, key=lambda x : (len(x), x))

for word in words:
    print(word)
