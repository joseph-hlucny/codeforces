

def moves():
    for i in range(-2, 3):
        row = input().split()
        for j in range(-2, 3):
            if row[j + 2] == '1':
                return abs(i) + abs(j)

def main():
    print(moves())

if __name__ == "__main__":
    main()
