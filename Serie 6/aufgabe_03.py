x = 4

def alpha(p):
    x = 6
    y = 0 + p

    def beta(q):
        nonlocal y
        y += 1
        y = y + q + p
        z = 1

        def gamma():
            global x
            global z
            nonlocal y
            y += 1
            z = 2
            x += 3
            w = 5
            comp = [k*k for k in range(3)]
        gamma()

    for i in range(2):
        beta(2)

    for i in range(2):
        x += i

    return x,y


alpha_x,alpha_y=alpha(10)

print(f"Das lokale x aus alpha ist {alpha_x}\n"
      f"Das lokale y aus alpha ist {alpha_y}\n"
      f"Das globale x ist: {x}\n"
      f"Das globale z ist: {z}"
)