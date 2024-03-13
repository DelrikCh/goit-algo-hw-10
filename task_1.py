from pulp import *


def optimize_production(water, sugar, lemon_juice, fruit_pure):
    prob = LpProblem("Optimal_Production", LpMaximize)

    # Lemonade amount
    L = LpVariable('Lemonade', lowBound=0, cat='Continuous')
    # Fruit juice amount
    F = LpVariable('Fruit Juice', lowBound=0, cat='Continuous')

    prob += 2 * L + F <= water  # Water limitation
    prob += L <= sugar  # Sugar limitation
    prob += L <= lemon_juice  # Lemon juice limitation
    prob += 2 * F <= fruit_pure  # Fruit pure limitation

    # Objective function(maximize)
    prob += L + F
    prob.solve()

    # return Lemonade amount, Fruite juice amount
    return L, F


def main():
    L, F = optimize_production(100, 50, 30, 40)
    print("Lemonade amount: ", value(L))
    print("Fruit juice amount: ", value(F))


if __name__ == '__main__':
    main()
