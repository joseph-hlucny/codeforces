import math

def main():
    m, n = [int(x) for x in input().split()]
    count = 0
    count += math.floor(n / 2)
    count *= m
    if count and n % 2:
        count += math.floor(m / 2)
    print(count)

if __name__ == "__main__":
    main()
