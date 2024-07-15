def loadWords():
    with open("../data/allowed_words.txt") as f:
        words = f.read().splitlines()
    return words 

def main():
    print(loadWords())

if __name__ == "__main__":
    main()