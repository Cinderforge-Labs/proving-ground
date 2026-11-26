import sys


def main():
    upto = int(sys.argv[1]) if len(sys.argv) > 1 else 99
    for n in range(1, upto + 1):
        print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)


if __name__ == "__main__":
    main()
