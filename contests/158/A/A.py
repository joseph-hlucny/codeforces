

def main():
    n, k = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    score = p[k - 1]
    count = 0
    for i in range(n):
        if p[i] >= score and p[i]:
            count += 1
            continue
        pass
    print(count)

if __name__ == "__main__":
    main()
