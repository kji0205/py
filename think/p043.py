print("이터레이터를 병렬로 처리하려면 zip을 사용하자")
names = ["Cecilia", "Lise", "Marie"]
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)