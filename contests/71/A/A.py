

def main():
    n = int(input())
    for i in range(n):
        abb(input())

def abb(w):
    if len(w) > 10:
        print(w[0] + str(len(w) - 2) + w[-1])
    else:
        print(w)

if __name__ == "__main__":
    main()
