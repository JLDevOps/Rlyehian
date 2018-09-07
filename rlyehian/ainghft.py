import os
import csv
import argparse

compendium = {}


# Load old text into the compendium with english being the key
# compendium = {type, {english | rlyehian}}
def ahahog_compendium_type():
    with open('kadishtuor.csv', mode='r') as kadishtuor_file:
        reader = csv.reader(kadishtuor_file)
        for row in reader:
            # Get distinct list
            if row[2] not in compendium:
                compendium[row[2]] = {}
            if row[0] not in compendium[row[2]]:
                compendium[row[2]][row[0]] = row[1]


# Load the old text into the compendium without word typing
# compendium = {english | rlyehian}
def ahahog_compendium():
    with open('kadishtuor.csv', mode='r') as kadishtuor_file:
        reader = csv.reader(kadishtuor_file)
        for row in reader:
            if row[0] not in compendium:
                compendium[row[0]] = row[1]


# Find the word from the dictionary
# def mgahnghft_aimgrluh(type, aimgrluh):
def mgahnghft_aimgrluh(aimgrluh):
    if aimgrluh in compendium:
        return compendium[aimgrluh]
    else:
        return aimgrluh


# # Translate the sentence
def ainghft(text):
    text_list = text.split()
    vulgtm = ''
    for word in text_list:
        print(word)
        aimgrluh = mgahnghft_aimgrluh(word)
        vulgtm += aimgrluh + ' '

    return vulgtm


def main():
    parser = argparse.ArgumentParser(description='Rlyehian Translator.  Speak the language of the old ones.')
    parser.add_argument('-t', '--text', help='Text to Translate', required=True)
    args = vars(parser.parse_args())
    text = args['text']

    ahahog_compendium()
    text = ainghft(text)
    print(text)


if __name__ == "__main__":
    main()
