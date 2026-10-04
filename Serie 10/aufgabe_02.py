import numpy as np
import matplotlib.pyplot as plt

# 1) Datei einlesen
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2) Liste aller Zeichen ohne Duplikate
chars = []
for ch in text:
    if ch not in chars:
        chars.append(ch)

# 3) Häufigkeiten der Zeichen bestimmen
freqs = []
for ch in chars:
    freqs.append(text.count(ch))

print("Zeichen:", chars)
print("Häufigkeiten:", freqs)

# 4) Balkendiagramm zeichnen
plt.figure(figsize=(18, 5))
x_pos = range(len(chars))
plt.bar(x_pos, freqs)

# 5) Achsenbeschriftung, Titel, Labels
labels = []
for ch in chars:
    if ch == " ":
        labels.append("<space>")
    elif ch == "\n":
        labels.append("\\n")
    elif ch == "\t":
        labels.append("\\t")
    else:
        labels.append(ch)

plt.xticks(x_pos, labels, rotation=90)
plt.xlabel("Zeichen")
plt.ylabel("Häufigkeit")
plt.title("Häufigkeit der Zeichen in data.txt")

plt.tight_layout()
plt.show()
