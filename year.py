'''
print("Введите год:")
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f' {year} - это високосный год')
else:
    print(f' {year} - это не високосный год')