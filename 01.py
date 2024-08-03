from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="maximize-drink-production", sense=LpMaximize)

x = LpVariable(name="lemonade", lowBound=0, cat='Integer')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

model += (x + y, "Total Products")

model += (2 * x + y <= 100, "Water Constraint")

model += (x <= 50, "Sugar Constraint")

model += (x <= 30, "Lemon Juice Constraint")

model += (2 * y <= 40, "Fruit Puree Constraint")

model.solve()

lemonade_count = x.varValue
fruit_juice_count = y.varValue
total_products = lemonade_count + fruit_juice_count

(lemonade_count, fruit_juice_count, total_products)