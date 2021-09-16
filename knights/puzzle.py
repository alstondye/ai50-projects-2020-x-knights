from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence01 = And(AKnight, AKnave)
    
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A is a Knight if what they said is the truth.
    Biconditional(AKnight, sentence01),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence11 = And(AKnave, BKnave)
      
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
 
    # A is a Knight if what they said is true.
    Biconditional(AKnight, sentence11),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence21 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentence22 = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A is a Knight if what they said is true (Both must be Knights or Knaves)
    # B is a Knight if what they said is true (Both must be different)
    Biconditional(AKnight, sentence21),
    Biconditional(BKnight, sentence22),
)
    
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence31 = Or(AKnight, AKnave)
sentence32 = And(Implication(AKnight, AKnave), BKnight)
sentence33 = And(CKnave, BKnight)
sentence34 = And(AKnight, CKnight)  
    
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A is a Knight if what they said (sentence31) is true
    # B is a Knight if what they said (sentence32) is true
    # If B is a Knave, then what they said about C is false
    # C is a Knight if what they said (sentence 34) is true
    Biconditional(AKnight, sentence31),
    Biconditional(BKnight, sentence32),
    Biconditional(BKnight, sentence33),
    Biconditional(AKnight, sentence34),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
