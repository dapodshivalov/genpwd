import random
import sys


def gen_syllable(k=2):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    if k != 2 and k != 3:
        return ""
    if k == 2:
        return random.choice(consonant) + random.choice(vowel)
    if k == 3:
        return random.choice(consonant) + random.choice(vowel) + random.choice(consonant)


def gen_digit():
    return random.randint(0, 9)


def to_uppercase_random(s):
    ind = random.randint(0, len(s) - 1)
    return s[:ind] + s[ind].upper() + s[ind + 1:]


def gen_pwd(length):
    # maximal number of syllables consist from 2 letter
    max2syl = length // 2
    numof2syl = random.randint(1, max2syl)
    numofdigit = random.randint(1, length - numof2syl * 2)
    numof3syl = (length - numof2syl - numofdigit) // 3

    if length > numofdigit + numof2syl + numof3syl:
        restlen = length - numofdigit - numof2syl - numof3syl
        numof2syl += restlen // 2
        numofdigit += restlen % 2

    pwd = ""
    selector = {
        0: lambda: str(gen_digit()),
        1: lambda: to_uppercase_random(gen_syllable()),
        2: lambda: to_uppercase_random(gen_syllable(3))
    }
    num = [0, 0, 0]
    maxnum = [numofdigit, numof2syl, numof3syl]
    while len(pwd) < length:
        choice = random.randint(0, 2)
        while num[choice] >= maxnum[choice]:
            choice = random.randint(0, 2)
        num[choice] += 1
        pwd += selector[choice]()
    return pwd


def main():
    try:
        length = max(3, int(sys.argv[1]))
    except IndexError:
        length = 7

    print(gen_pwd(length))


if __name__ == '__main__':
    main()
