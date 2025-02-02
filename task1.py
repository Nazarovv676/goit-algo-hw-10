from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні рішень
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Функція цілі (максимізація загальної кількості напоїв)
model += lemonade + fruit_juice, "Total Drinks Produced"

# Обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint")
model += (1 * lemonade <= 50, "Sugar Constraint")
model += (1 * lemonade <= 30, "Lemon Juice Constraint")
model += (2 * fruit_juice <= 40, "Fruit Puree Constraint")

# Розв'язання задачі
model.solve()

# Виведення результатів
results = {
    "Lemonade": lemonade.varValue,
    "Fruit_Juice": fruit_juice.varValue,
    "Total_Products": lemonade.varValue + fruit_juice.varValue
}

print("Optimal Production Plan:")
for product, amount in results.items():
    print(f"{product}: {amount}")
