"""
Phone Number Mnemonics

12/06/2021
"""


DIGIT_LETTERS = {0: ["0"], 1: ["1"], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: [
    "j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"],  8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}


def phoneNumberMnemonics(phoneNumber):
    currMnemonic = ["0"] * len(phoneNumber)
    foundMnemonics = []
    helperFunc(0, phoneNumber, currMnemonic, foundMnemonics)
    return foundMnemonics


def helperFunc(idx, phoneNumber, currMnemonic, foundMnemonics):
    if idx == len(phoneNumber):
        mnemonic = "".join(currMnemonic)
        foundMnemonics.append(mnemonic)
    else:
        number = phoneNumber[idx]
        letters = DIGIT_LETTERS[number]
        for char in letters:
            currMnemonic[idx] = char
            helperFunc(idx + 1, phoneNumber, currMnemonic, foundMnemonics)
