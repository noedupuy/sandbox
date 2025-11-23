import numpy as np
import pandas as pd

# Création d'un petit dataset synthétique
np.random.seed(42)
x = np.linspace(0, 10, 50)


y = np.sin(x) + 0.2 * np.random.randn(50)

df = pd.DataFrame({"x": x, "y": y, "category": np.random.choice(["A", "B"], size=50)})
