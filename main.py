
result = []

def divider(a, b):
    if a < b:
        raise ValueError("Перше число менше за друге")

    if b > 100:
        raise IndexError("Друге число більше за 100")

    return a / b


data = [
    (10, 2),
    (2, 5),
    ("123", 4),
    (18, 0),
    ([], 15),
    (8, 4),
    (120, 101)
]

for a, b in data:
    try:
        res = divider(a, b)
        result.append(res)
        print(f"Результат ділення {a} / {b} = {res}")

    except Exception as error:
        print(f"Виникла помилка: {type(error).__name__}")
        print(f"Опис помилки: {error}")

print("\nРезультати успішних операцій:")
print(result)
