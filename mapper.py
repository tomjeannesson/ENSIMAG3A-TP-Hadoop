import sys

if __name__ == "__main__":
    data = sys.stdin.read()
    for word in data.split(" "):
        print(f"{word} 1")
