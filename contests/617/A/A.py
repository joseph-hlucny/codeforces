

def main():
    x = int(input())
    steps = x // 5
    if x < 5:
        steps = 1
    elif x % 5:
        steps += 1
    print(steps)

if __name__ == "__main__":
    main()
