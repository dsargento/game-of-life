from sys import argv
from src import window


def main():
    if len(argv) <= 1:
        print("Usage: python3.6 game-of-life.py [input file path]")
        return
    try:
        file = open(argv[1], 'r', 1)
    except IOError:
        print("File not found or path is incorrect")
        return
    array = build_array(file)
    window.Window(array)


def build_array(file):
    array = []
    for line in file:
        array.append(line)
    return array


if __name__ == '__main__':
    main()
