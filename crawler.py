import time
from tkinter import Tk, filedialog
import os


def countLines(filePath):
    length = 0
    with open(filePath, 'r') as file:
        lines = file.readlines()
        length += len(lines)
        file.close()
    return length


def count(dirPath):
    _sum = 0
    for file in os.listdir(dirPath):
        path = os.path.join(dirPath, file)
        print(path)
        if os.path.isfile(path):
            try:
                _sum += countLines(path)
            except:
                pass
        elif os.path.isdir(path):
            try:
                _sum += count(path)
            except:
                pass
    return _sum


def main():
    root = Tk()
    _dir = filedialog.askdirectory(
        initialdir="/", title="Select dir")
    _sum = count(_dir)
    print("\n\n\n" + _dir + ": " + str(_sum))
    root.destroy()
    time.sleep(1000)


if __name__ == "__main__":
    main()
