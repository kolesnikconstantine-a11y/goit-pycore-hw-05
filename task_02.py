import re
# приймає рядок як аргумент і повертає генератор, що ітерує по всіх дійсних числах у тексті
def generator_numbers(text: str):
    #регулярні вираз, з урахуванням, що числа чітко відокремлені пробілами.
    pattern = r"\s\d+\.\d+\s"
    matches = re.findall(pattern, text)
    for el in matches:
        # Застосування конструкції yield у функції
        yield el.strip()

# sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.
def sum_profit(text: str, func: callable):
    sum_ = 0
    for line in func(text):
        sum_ += float(line)
    return sum_


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
