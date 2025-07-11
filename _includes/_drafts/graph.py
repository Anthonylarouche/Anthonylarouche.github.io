import numpy as np
import matplotlib.pyplot as plt

# Paramètres des deux lois normales
mu1, sigma1 = 0, 1             # Moyenne et écart-type du groupe 1
mu2, sigma2 = 1.5, 1           # Moyenne et écart-type du groupe 2 (moyenne décalée)

# Axe des x
x = np.linspace(-4, 6, 500)

# Densités normales
y1 = (1 / (sigma1 * np.sqrt(2 * np.pi))) * np.exp(- (x - mu1)**2 / (2 * sigma1**2))
y2 = (1 / (sigma2 * np.sqrt(2 * np.pi))) * np.exp(- (x - mu2)**2 / (2 * sigma2**2))

# Création du graphique
plt.figure(figsize=(10, 5))

# Tracer les deux courbes
plt.plot(x, y1, label='Groupe 1 : N(0, 1)', linewidth=2)
plt.plot(x, y2, label='Groupe 2 : N(1.5, 1)', linewidth=2)

# Tracer les lignes verticales aux moyennes
plt.axvline(mu1, color='black', linestyle='--')
plt.axvline(mu2, color='black', linestyle='--')

# Ajouter une double flèche entre les deux moyennes
plt.annotate(
    '', xy=(mu1, 0.42), xytext=(mu2, 0.42),
    arrowprops=dict(arrowstyle='<->', linewidth=1.5)
)
plt.text((mu1 + mu2)/2, 0.43, "Taille de l'effet", ha='center', fontsize=12)

# Mise en forme
plt.title("")
plt.xlabel("Valeur")
plt.ylabel("Densité")
plt.grid(False)
plt.legend()
plt.tight_layout()

# Afficher le graphique
plt.show()
