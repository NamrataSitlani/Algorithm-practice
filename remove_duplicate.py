l = [{'a': 123, 'b': 1234},
        {'a': 3222, 'b': 1234},
        {'a': 123, 'b': 1234}]
seen = set()
new_l = []

for d in l:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)
print(new_l)
