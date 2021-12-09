import matplotlib.pyplot as plt
import numpy as np


def decode(start, end):
    dict = {chr(i): 0 for i in range(97, 104)}

    for number in start:
        if len(number) == 2:
            one = number[0], number[1]
        if len(number) == 4:
            four = number[0], number[1], number[2], number[3]
        for character in number:
            dict[character] += 1
    print(f'{dict}')
    dircRedirect = {
        "a": [name for name, age in dict.items() if age == 8],
        "b": [name for name, age in dict.items() if age == 6],
        "c": [name for name, age in dict.items() if age == 8],
        "d": [name for name, age in dict.items() if age == 7],
        "e": [name for name, age in dict.items() if age == 4],
        "f": [name for name, age in dict.items() if age == 9],
        "g": [name for name, age in dict.items() if age == 7]
    }
    print(dircRedirect)
    dircRedirect["c"] = [x for x in one if x in dircRedirect["c"]]
    dircRedirect["a"] = [x for x in dircRedirect["a"] if x not in dircRedirect["c"]]
    dircRedirect["d"] = [x for x in four if x in dircRedirect["d"]]
    dircRedirect["g"] = [x for x in dircRedirect["g"] if x not in dircRedirect["d"]]
    out = [[[name for name, age in dircRedirect.items() if age == [char]][0] for char in output] for output in end]
    print(dircRedirect)
    outpp = []
    for number in out:
        chara = ""
        for char in sorted(number):
            chara += char
        outpp.append(chara)
    return outpp


if __name__ == '__main__':
    with open("Days/Day8/input.txt") as f:
        lines = f.readlines()
    count = 0
    numberCode = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    output = []

    for line in lines:
        start2, end2 = line.replace("\n", "").split(" | ")
        start = start2.split(" ")
        end = end2.split(" ")
        string = decode(start, end)
        out = ""
        for number in string:
            for i in range(len(numberCode)):
                if number == numberCode[i]:
                    out = out + str(i)
        output.append(int(out))
        print(f"{start2} | {end2} -> {string} = {out}")
        break
    print(sum(output))
