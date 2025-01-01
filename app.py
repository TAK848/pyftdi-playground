import sys

from src.co2 import co2


def main():
    print("Hello from pyftdi-playground!")


def main():
    print("Hello from visban-ftdi!")
    # 引数からモードを取得
    mode = sys.argv[1]
    if mode == "co2":
        co2()
    else:
        print("Invalid mode")
        sys.exit(1)

if __name__ == "__main__":
    main()
