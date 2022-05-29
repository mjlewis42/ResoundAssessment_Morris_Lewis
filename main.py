"""
Normal audio = 0
Filler word = 1
Profanity = 2
Repetition = 3
"""

inputArray = [3, 1, 0, 0, 1, 1, 1, 0, 0, 2, 2, 3, 2, 1, 1, 0, 0, 1, 3, 0, 3, 2, 2, 1]


def main(inputArray):
    sounds = {}
    previous = 0
    start = 0

    for iteration, value in enumerate(inputArray):
        if previous != value:
            stop = iteration - 1
            keys = start, stop
            sounds.update({keys: previous})
            start = iteration
        if iteration == len(inputArray) - 1 and value != 0:
            stop = iteration
            keys = start, stop
            sounds.update({keys: value})
        previous = value

    print("Filler word: ", [k for k, v in sounds.items() if v == 1])
    print("Profanity: ", [k for k, v in sounds.items() if v == 2])
    print("Repetition: ", [k for k, v in sounds.items() if v == 3])


if __name__ == "__main__":
    main(inputArray)
