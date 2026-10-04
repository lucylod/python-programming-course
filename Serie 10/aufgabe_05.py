import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_tictactoe(board):
    fig, ax = plt.subplots(figsize=(5, 5))

    # --- Spielfeld-Gitter zeichnen (3×3) ---
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

    # Gitterlinien
    ax.plot([1, 1], [0, 3], color="black", linewidth=2)
    ax.plot([2, 2], [0, 3], color="black", linewidth=2)
    ax.plot([0, 3], [1, 1], color="black", linewidth=2)
    ax.plot([0, 3], [2, 2], color="black", linewidth=2)

    # --- Symbole einzeichnen ---
    for i in range(3):          # Zeilen   (y)
        for j in range(3):      # Spalten  (x)
            cell = board[i][j]
            x = j + 0.5         # Mitte der Spalte
            y = 2.5 - i         # Mitte der Zeile (invertiert!)

            if cell == "o":
                circle = patches.Circle((x, y), 0.35, fill=False, linewidth=3)
                ax.add_patch(circle)

            elif cell == "x":
                square = patches.Rectangle((j + 0.15, 2.15 - i),
                                           0.7, 0.7, fill=False, linewidth=3)
                ax.add_patch(square)

    plt.title("Tic Tac Toe")
    plt.show()


# --- Beispiel ---
board = [
    ["x", "o", ""],
    ["", "x", ""],
    ["o", "", "o"]
]

plot_tictactoe(board)
