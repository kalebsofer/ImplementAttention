#
#
import random


#
#
random.seed(42)


#
#
idx2tkn = {0: "?", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


#
#
tkn2idx = {v: k for k, v in idx2tkn.items()}


# Create patterns like this:
#
# --> [A, B, A, A, ?]
# --> B
#
# --> [D, ?, C, D, D]
# --> C
#
# --> [?, G, A, G, G]
# --> A
#
# --> [G, G, F, G, ?]
# --> F
#
def generate_item_pattern():
    """Generate a pattern sequence and its corresponding answer.

    Creates a 5-element sequence where:
    - One position contains a '?' (randomly placed)
    - One position contains a different letter (strB) (randomly placed, not at '?' position)
    - Remaining positions contain the same letter (strA)

    Returns:
        tuple: (list, str)
            - list: A 5-element list containing the pattern sequence
            - str: The answer (strB), which is the "odd one out" letter

    Example:
        >>> generate_item_pattern()
        (['A', 'B', 'A', 'A', '?'], 'B')
    """
    curL = list(idx2tkn.values())
    curL.remove("?")
    strA = random.choice(curL)
    curL.remove(strA)
    strB = random.choice(curL)
    lisA = [strA] * 5
    idxQ = random.randint(0, 4)
    lisA[idxQ] = "?"
    idxB = random.choice([i for i in range(5) if i != idxQ])
    lisA[idxB] = strB
    return lisA, strB


#
#
if __name__ == "__main__":
    trn = [generate_item_pattern() for _ in range(1)]
    print(len(idx2tkn))
    print(trn)
