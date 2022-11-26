

def main():
    n = int(input())
    s1, s2, s3 = 0, 0, 0
    for i in range(n):
        v = [int(_) for _ in input().split()]
        s1 += v[0]
        s2 += v[1]
        s3 += v[2]
    if s1 != 0 or s2 != 0 or s3 != 0:
        print("NO")
    else:
        print("YES")

    
    
if __name__ == "__main__":
    main()
