

def main():
    n = int(input())
    count = 0
    for i in range(n):
        w = input()
        if w[1] == "+":
            count += 1
        else:
            count -= 1
    print(count)

if __name__ == "__main__":
    main()
