from math import ceil

def main():
    n, d = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    cur = 1
    moves = 0
    for _ in range(n - 1):
        if b[cur] == b[cur - 1]:
            moves += 1
            b[cur] += d
        elif b[cur] < b[cur - 1]:
            diff = b[cur - 1] - b[cur]
            tmp_moves = ceil(diff / d)
            if diff % d == 0:
                moves += 1
                b[cur] += d
            b[cur] += d * tmp_moves
            moves += tmp_moves
        cur += 1
    
    print(moves)
    

if __name__ == "__main__":
    main()