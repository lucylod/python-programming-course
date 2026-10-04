from random import choice
import textwrap

class TextGeneratorChars:
    def __init__(self, filename):
        # (c1, c2) -> [Liste möglicher nächster Zeichen c3]
        self.possible_chars = {}

        # gesamten Text einlesen (inkl. Leerzeichen, Zeilenumbrüche usw.)
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        # Startzustand: zwei "leere" Zeichen (kann man auch anders wählen)
        c1 = ""
        c2 = ""

        # über alle Zeichen im Text iterieren
        for c3 in text:
            key = (c1, c2)
            if key not in self.possible_chars:
                self.possible_chars[key] = [c3]
            else:
                self.possible_chars[key].append(c3)

            # Fenster weiterschieben: (c1, c2) -> (c2, c3)
            c1, c2 = c2, c3

    def generate_text(self, char_count=400):
        # Startzustand wählen:
        # hier z.B. ein Paar, bei dem das zweite Zeichen groß ist (Satzanfang-ähnlich)
        candidates = [k for k in self.possible_chars
                      if len(k[1]) == 1 and k[1].isupper()]
        if candidates:
            c1, c2 = choice(candidates)
        else:
            c1, c2 = choice(list(self.possible_chars.keys()))

        text = ""

        for _ in range(char_count):
            text += c2  # aktuelles Zeichen anhängen

            key = (c1, c2)
            if key not in self.possible_chars:
                # Fallback: zufälligen Startzustand wählen
                c1, c2 = choice(list(self.possible_chars.keys()))
                continue

            # zufälliges nächstes Zeichen c3 aus der Liste wählen
            c3 = choice(self.possible_chars[key])

            # Fenster weiterschieben
            c1, c2 = c2, c3

        return textwrap.fill(text, width=70)


# Beispielaufruf mit deiner data.txt
generator = TextGeneratorChars("data.txt")
print(generator.generate_text(600))
