"""
Use the Taylor expansion defined in `function_and_expansion.py`.
"""
from function_and_expansion import f1, Taylor_f1


def main():
    """
    Calculate some values of `f1` and it's Taylor expansion
    """
    x = [0, 0.001, 0.01, 0.1, 1]
    y = list([f1(x_) for x_ in x])
    z = list([Taylor_f1(x_, order=3) for x_ in x])

    print("")
    print("{0:>10s} |{1:>10s} |{2:>10s} ".format(
        "x", "f1(x)", "Taylor(x)"))
    print("{0:>11s}|{1:>11s}|{2:>11s}".format(
        *(3 * (11 * "-", ))))
    for x_val, f1_val, taylor in zip(x, y, z):
        print("{0: 10.3f} |{1: 10.7f} |{2: 10.7f} ".format(
            x_val, f1_val, taylor))


if __name__ == "__main__":

    main()
