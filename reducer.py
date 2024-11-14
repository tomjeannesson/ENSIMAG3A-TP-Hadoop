import sys

if __name__ == "__main__":
    data = sys.stdin.read()
    all_vales = {}
    for w in data.split("\n"):
        if w == "":
            continue
        word, count = w.split(" ")
        all_vales[word] = all_vales.get(word, 0) + int(count)
    for word, count in all_vales.items():
        print(f"{word} {count}")
