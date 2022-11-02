

def main():
    w1, w2 = input().lower(), input().lower()
    if w1 < w2:
        print(-1)
    elif w1 == w2:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()
