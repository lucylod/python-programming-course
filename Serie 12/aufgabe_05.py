import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

# Eckpunkte laden
vertices = np.load("vertices.npy")

# Bounding Box bestimmen
xmin, ymin = vertices.min(axis=0)
xmax, ymax = vertices.max(axis=0)

# Fläche des Rechtecks
rect_area = (xmax - xmin) * (ymax - ymin)

# Anzahl zufälliger Punkte
N = 200_000

# Zufällige Punkte im Rechteck
points = np.random.uniform(
    low=[xmin, ymin],
    high=[xmax, ymax],
    size=(N, 2)
)

# Polygon-Objekt
polygon = Path(vertices)

# Test: welche Punkte liegen im Polygon?
inside = polygon.contains_points(points)

# Monte-Carlo-Schätzung der Fläche
area_estimate = rect_area * inside.mean()

print("Geschätzte Fläche:", area_estimate)


plt.figure(figsize=(6, 6))

# Punkte außerhalb
plt.scatter(
    points[~inside, 0],
    points[~inside, 1],
    s=1,
    color="lightgray",
    label="außerhalb"
)

# Punkte innerhalb
plt.scatter(
    points[inside, 0],
    points[inside, 1],
    s=1,
    color="blue",
    label="innerhalb"
)

# Polygonrand zeichnen
closed_vertices = np.vstack([vertices, vertices[0]])
plt.plot(
    closed_vertices[:, 0],
    closed_vertices[:, 1],
    color="red",
    linewidth=2,
    label="Polygon"
)

plt.title("Monte-Carlo-Flächenberechnung")
plt.legend()
plt.axis("equal")
plt.show()

