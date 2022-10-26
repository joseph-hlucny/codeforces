

def main():
    n = int(input())
    count = 0
    for i in range(n):
        v1, v2, v3 = input().split(" ")
        if int(v1) + int(v2) + int(v3) > 1:
           count += 1 

    print(count)

if __name__ == "__main__":
    main()
