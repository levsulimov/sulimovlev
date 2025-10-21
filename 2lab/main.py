

if __name__ == "__main__":
    pass
s1 = input("Строка 1: ")
s2 = input("Строка 2: ")

c1, c2 = {}, {}
for c in s1: c1[c] = c1.get(c, 0) + 1
for c in s2: c2[c] = c2.get(c, 0) + 1

g1, g2 = {}, {}
for k,v in c1.items(): g1[v] = g1.get(v, []) + [k]
for k,v in c2.items(): g2[v] = g2.get(v, []) + [k]

result = []
for cnt in g1:
    if cnt not in g2 or len(g1[cnt]) != len(g2[cnt]):
        print("Ошибка")
        break
    for a,b in zip(sorted(g1[cnt]), sorted(g2[cnt])):
        result.append(f"{a}={b}")
else:
    print(" ".join(result))# Ваш код здесь
