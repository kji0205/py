'''가능한 모든 순열과 조합 순환'''

from itertools import permutations, combinations, combinations_with_replacement

items = [1, 2, 3]
print(sum(1 for _ in permutations(items)))
for p in permutations(items):
    print(p)
print(sum(1 for _ in permutations(items, 2)))
for p in permutations(items, 2):
    print(p)

# print(sum(1 for _ in combinations(items, 3)))
# for c in combinations(items, 3):
#     print(c)
# print(sum(1 for _ in combinations(items, 2)))
# for c in combinations(items, 2):
#     print(c)
# print(sum(1 for _ in combinations(items, 1)))
# for c in combinations(items, 1):
#     print(c)

print(sum(1 for _ in combinations_with_replacement(items, 3)))
for c in combinations_with_replacement(items, 3):
    print(c)

