from Sequence import Sequence

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAGIC_NUMBER = 10958

def main():
    seq = Sequence(DIGIT_SEQUENCE)
    print(seq.evaluate())

if __name__ == "__main__":
    main()