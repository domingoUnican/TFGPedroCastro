import matplotlib.pyplot as plt
import numpy as np
from formula_gen import calc_all_form_results
best_j = 2
variables = dict()
for i in range(2, 3+1):
    target_n_sols = np.power(2, np.power(2, i))
    variables[i] = []
    for j in range(best_j, 10):
        print(f"--- Testing for variables {i} with {j} operations")
        time, n_sols = calc_all_form_results(i, j)
        variables[i].append((round(time, 2), j, n_sols))
        if n_sols == target_n_sols:
            best_j = j
            break

for i in variables.keys():
    times, n_op, n_solutions = zip(*variables[i])
    plt.plot(times, n_solutions, marker='o')
    plt.axvline(x=times[-1], color='red', linestyle='--')
    plt.axhline(y=n_solutions[-1], color='red', linestyle='--')
    x_axis_labels = [f'{i}\n{j}' for i, j in zip(times, n_op)]
    plt.xticks(times, labels=x_axis_labels)
    plt.yticks(n_solutions)
    plt.savefig(f"plots/{i}_variables.png")
