
from sys import argv, exit
import csv


def main():
    if len(argv) != 3:
        print("Error, please do it again.")
        exit(1)

    baza_danych = argv[1]
    sekwencja = argv[2]
    identities = []


    with open(baza_danych, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        #make dictionary
        #https://python.hotexamples.com/examples/csv/DictReader/fieldnames/python-dictreader-fieldnames-method-examples.html
        substrings = reader.fieldnames[2:]

        #https://www.codegrepper.com/code-examples/python/dictreader+fieldnames+python

        fieldnames = ['first_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for row in reader:

            identities.append(row)


    # https://www.w3schools.com/python/ref_dictionary_fromkeys.asp

    x = ('substring','substring','substring')
    y = 0

    sekwencja_liczba = dict.fromkeys(substrings, 0)



    with open(sekwencja, "r") as plik:

        sekwencja_lista = plik.readline()

        for substring in substrings:

            sekwencja_liczba[substring] = lookfor_recaps(sekwencja_lista, substring)


    for identity in identities:
        zgodnosc = 0

        #https://www.programiz.com/python-programming/break-continue
        for substring in substrings:
            if int(identity[substring]) != sekwencja_liczba[substring]:
                continue
            zgodnosc += 1

        if zgodnosc == len(substrings):
            print(identity['name'])
            exit(0)

    print("No match")
    exit(1)

# looking for longest recaps
def lookfor_recaps(sekwencja_lista, substring):

    longest_recaps = 0
    for i in range(len(sekwencja_lista)):

        recaps = 0

        if sekwencja_lista[i: i + len(substring)] == substring:

            recaps += 1
            #  count for consecutive recaps
            while sekwencja_lista[i: i + len(substring)] == sekwencja_lista[i + len(substring): i + (2 * len(substring))]:

                recaps += 1

                i += len(substring)

        # for max count
        while recaps > longest_recaps:
            longest_recaps = recaps
    return longest_recaps



main()