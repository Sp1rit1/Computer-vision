def Max(a, b, c):
    a = float(input("Введите число а: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1

print(Max(0, 3, 4))
