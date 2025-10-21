if __name__ == "__main__":
    pass
import random
n = int(input("Сколько строк? "))
m = int(input("Сколько столбцов? "))
max_sum = 0
best_row = 0
table = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 100))
    table.append(row)

print("\nМассив:")
for row in table:
    for number in row:
        print(f"{number:2}", end=" ")
    print()

print("\nМаксимальные числа в каждой строке:")
for i in range(n):
    max_in_row = max(table[i])
    print(f"Строка {i+1}: {max_in_row}")

print("\nМаксимальные числа в каждом столбце:")
for j in range(m):
    column_numbers = []
    for i in range(n):
        column_numbers.append(table[i][j])
    max_in_column = max(column_numbers)
    print(f"Столбец {j+1}: {max_in_column}")
    
if n == m:
    diag_sum = 0
    diag2_sum = 0
    for i in range(n):
        diag_sum += table[i][i]
        diag2_sum += table[i][n-1-i]
    
    print(f"\nСумма первой диагонали: {diag_sum}")
    print(f"Сумма второй диагонали: {diag2_sum}")
else:
    print("\nТаблица не квадратная")

for i in range(n):
    row_sum = sum(table[i])
    if row_sum > max_sum:
        max_sum = row_sum
        best_row = i
print(f"\nСтрока {best_row+1} имеет наибольшую сумму = {max_sum}")# Ваш код здесь
