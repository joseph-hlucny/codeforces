

def main():
    a, b = [int(_) for _ in input().split()]
    count = 0
    while True:
        count += 1
        a *= 3
        b *= 2
        if a > b:
            print(count)
            break

if __name__ == "__main__":
    main()
