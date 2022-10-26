import math


def main():
    n, m, a = [int(x) for x in input().split()]
    vert = a < n
    hori = a < m
    if a < n:
        tiles1 = math.ceil(n / a)
    if a < m:
        tiles2 = math.ceil(m / a)
    if a == 1:
        print(m * n)
    elif vert and hori:
        print(math.ceil(n / a) * math.ceil(m / a))
    elif vert:
        print(math.ceil(n / a))
    elif hori:
        print(math.ceil(m / a))
    else:
        print(1)

if __name__ == "__main__":
    main()
