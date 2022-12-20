

def main():

    n, p1, p2, p3, t1, t2 = [int(_) for _ in input().split()]
    minutes = [0, 0, 0]
    r_prev = 0
    for _ in range(n):
        l, r = [int(_) for _ in input().split()]
        minutes[0] += r - l
        if r_prev:
            rest = l - r_prev
            if rest <= t1:
                minutes[0] += rest
            else:
                minutes[0] += t1
                rest -= t1
                if rest <= t2:
                    minutes[1] += rest
                else:
                    minutes[1] += t2
                    rest -= t2
                    minutes[2] += rest
        r_prev = r

    print(minutes[0] * p1 + minutes[1] * p2 + minutes[2] * p3)




if __name__ == "__main__":
    main()