import numpy as np
import matplotlib.pyplot as plt

# Données ONS - Wilaya d'Ouargla
years = [1966, 1977, 1987, 1998, 2008, 2013]
population = [20000, 42098, 81721, 139381, 558558, 627677]

# Modèle exponentiel: P(t) = P0 * exp(r*t)
P0 = 627677
r = 0.02
years_proj = np.arange(2013, 2031)
pop_proj = P0 * np.exp(r * (years_proj - 2013))

print("Population projetée Ouargla 2030:", int(pop_proj[-1]))

plt.plot(years, population, 'o-', label='Données ONS')
plt.plot(years_proj, pop_proj, '--', label='Projection (r=2%)')
plt.title('Projection démographique - Ouargla')
plt.legend()
plt.grid(True)
plt.show()
