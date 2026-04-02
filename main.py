from generator import generate_gnp
from analysis import is_connected, largest_component_size
import numpy as np
import matplotlib.pyplot as plt

n = 50
trials = 100

ps = np.linspace(0, 0.2, 25)

conn_results = []
giant_results = []

for p in ps:
    connected_count = 0
    total_largest = 0

    for _ in range(trials):
        g = generate_gnp(n, p)

        # conectividade
        if is_connected(g):
            connected_count += 1

        # maior componente
        total_largest += largest_component_size(g)

    conn_results.append(connected_count / trials)
    giant_results.append((total_largest / trials) / n)

plt.plot(ps, conn_results, label="Connectivity", marker='o')
plt.plot(ps, giant_results, label="Giant Component", marker='x')

plt.xlabel("p")
plt.ylabel("Value")

plt.legend()
plt.grid()
plt.title("Transitions in random graphs")

# linhas teóricas
plt.axvline(1/n, linestyle='--', label="1/n")
plt.axvline(np.log(n)/n, linestyle='--', label="ln(n)/n")

plt.show()