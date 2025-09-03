compound_words = set()
words = []

# Läs in alla ord tills EOF eller tom rad
while True:
    try:
        line = input()
        if line == "":   # tom rad avslutar
            break
        words.extend(line.split())  # lägg till orden i listan
    except EOFError:
        break

for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            compound_words.add(words[i] + words[j])

for word in sorted(compound_words):
    print(word)
