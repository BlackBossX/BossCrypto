print("--------------------------------------------------")
print("     BossCrypt                                    ")
print("         Creating by BlackBossX                   ")
print("             Visit for more: www.blackboss.xyz    ")
print("--------------------------------------------------")

mapping = {  # Decoding Dictionaries
    "h": "a",
    "u": "b",
    "i": "c",
    "v": "d",
    "j": "e",
    "w": "f",
    "k": "g",
    "x": "h",
    "l": "i",
    "y": "j",
    "m": "k",
    "z": "l",
    "n": "m",
    "a": "n",
    "o": "o",
    "b": "p",
    "p": "q",
    "c": "r",
    "q": "s",
    "d": "t",
    "r": "u",
    "e": "v",
    "s": "w",
    "f": "x",
    "t": "y",
    "g": "z",

    "K": "A",
    "X": "B",
    "L": "C",
    "Y": "D",
    "M": "E",
    "Z": "F",
    "N": "G",
    "A": "H",
    "O": "I",
    "B": "J",
    "P": "K",
    "C": "L",
    "Q": "M",
    "D": "N",
    "R": "O",
    "E": "P",
    "S": "Q",
    "F": "R",
    "T": "S",
    "G": "T",
    "U": "U",
    "H": "V",
    "V": "W",
    "I": "X",
    "W": "Y",
    "J": "Z",

    "9": "0",
    "8": "1",
    "7": "2",
    "6": "3",
    "5": "4",
    "4": "5",
    "3": "6",
    "2": "7",
    "1": "8",
    "0": "9",
    " ": "=",
    ".": "_",
    ":": ".",
    "=": " ",
}
mapping_2 = {  # Encoding Dictionaries
    "a": "h",
    "b": "u",
    "c": "i",
    "d": "v",
    "e": "j",
    "f": "w",
    "g": "k",
    "h": "x",
    "i": "l",
    "j": "y",
    "k": "m",
    "l": "z",
    "m": "n",
    "n": "a",
    "o": "o",
    "p": "b",
    "q": "p",
    "r": "c",
    "s": "q",
    "t": "d",
    "u": "r",
    "v": "e",
    "w": "s",
    "x": "f",
    "y": "t",
    "z": "g",

    "A": "K",
    "B": "X",
    "C": "L",
    "D": "Y",
    "E": "M",
    "F": "Z",
    "G": "N",
    "H": "A",
    "I": "O",
    "J": "B",
    "K": "P",
    "L": "C",
    "M": "Q",
    "N": "D",
    "O": "R",
    "P": "E",
    "Q": "S",
    "R": "F",
    "S": "T",
    "T": "G",
    "U": "U",
    "V": "H",
    "W": "V",
    "X": "I",
    "Y": "W",
    "Z": "J",

    "0": "9",
    "1": "8",
    "2": "7",
    "3": "6",
    "4": "5",
    "5": "4",
    "6": "3",
    "7": "2",
    "8": "1",
    "9": "0",
    "=": " ",
    ".": ":",
    "_": ".",
    " ": "=",

}
flag = []
file = open("BossCrypto.txt").read().strip()  # Read BossCrypt file
print("Enter 1 to Encode")
print("Enter 2 to Decode")
choose = int(input(" "))  # Select method

if choose == 2:
    for i in range(0, len(file)):  # Decoding Function
        character = file[i:i + 1]  # Get character or value in the file
        print(character, mapping[character])
        flag.append(mapping[character])  # enter values or characters to array

elif choose == 1:
    for i in range(0, len(file)):  # Encoding Function
        character = file[i:i + 1]
        print(character, mapping_2[character])
        flag.append(mapping_2[character])
else:
    print("Invalid Input")
print("  ")
print("Flag : ", "".join(flag))  # Print Flag
