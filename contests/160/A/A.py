

def main():
    n = int(input())
    a = [int(_) for _ in input().split()]
    a.sort(reverse=True)
    right = sum(a) # Value of coins not taken
    left = 0 # Value of coins taken
    coins = 0 # Coins taken
    for i in a:
        coins += 1
        right -= i
        left += i
        if left > right:
            break

    print(coins)


if __name__ == "__main__":
    main()