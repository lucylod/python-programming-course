def float_to_floating_point(x, M=4, emin=-4, emax=4, normalized=False):

    if isinstance(x, int):
        p, q = x, 1
    elif isinstance(x, float):
        p, q = x.as_integer_ratio()  
    else:
        raise TypeError("x muss int oder float sein!")

    twoM = 2 ** M

    best_num, best_den = 0, 1
    best_sign, best_A, best_e = 1, 0, 0

    best_dist_num = abs(p)
    best_dist_den = 1

    A_start = (2 ** (M - 1)) if normalized else 0

    for sign in (1, -1):
        for e in range(emin, emax + 1):
            for A in range(A_start, twoM):

                if e >= 0:
                    n = sign * A * (2 ** e)
                    d = twoM
                else:
                    n = sign * A
                    d = twoM * (2 ** (-e))  

                dist_num = abs(p * d - n * q)

                if dist_num * best_dist_den < best_dist_num * d:
                    best_num, best_den = n, d
                    best_dist_num, best_dist_den = dist_num, d
                    best_sign, best_A, best_e = sign, A, e   

                elif dist_num * best_dist_den == best_dist_num * d:
                    if abs(n) * best_den < abs(best_num) * d:
                        best_num, best_den = n, d
                        best_dist_num, best_dist_den = dist_num, d
                        best_sign, best_A, best_e = sign, A, e

    return best_num, best_den, best_sign, best_A, best_e


num, den, sign, A, e = float_to_floating_point(2.75, M=4, emin=-4, emax=4, normalized=True)

print(
    f"x̃ = {num}/{den}, "
    f"sign = {sign}, "
    f"mantisse = 0.{A:04b}_2, "
    f"e = {e}"
)
