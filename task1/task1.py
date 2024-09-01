import sys


def solve(n, m):
    result = []
    idx = 0
    while True:
        result.append(str(idx + 1))
        idx = (idx + m - 1) % n
        if idx == 0:
            break
        
    return result


def main():
    if len(sys.argv) != 3:
        print("Use,please: taks1.py <n> <m>")
        sys.exit(1)
        
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = solve(n, m)
    print("".join(result))


if __name__ == "__main__":
    main()
