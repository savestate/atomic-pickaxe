
# TODO:
# Aliteration
# More Granular Generation
# Syllables
# Add input validation to wildcards.txt (can be bypassed regardless in a file manager though... so maybe doesn't matter?)
# Clean up files and dependencies (seems good enough 2022-01-25)
# get rid of camelcased functions and variables

import os
import random
from inspect import getsourcefile
from pathlib import Path
cwdfiles = f"{os.path.dirname(getsourcefile(lambda:0))}/files"


# Not MacOS Safe
# cwdfiles = f"{os.path.dirname(os.path.realpath(__file__))}/files"


def last_three_lines(file: str):
    # Display the last 3 lines of a given file at filepath
    # For displaying the last 3 saved names or wildcard words
    pass


def logic_for_wc_mgmt(user_word_to_add: str):
    pass


def manage_wildcards():
    while True:
        opt1 = input("Would you like to add to wildcards.txt? (Y/N) ").upper()
        if opt1 == 'Y':
            with open(f"{cwdfiles}/wildcards.txt", mode='a') as add_to_wild:
                word_to_add = input("Enter a word to add to your wildcard list: ")
                word_to_add = f'{word_to_add}\n'
                add_to_wild.write(word_to_add)
                print(f"Added {word_to_add}", end='')
                while True:
                    opt2 = input("Add Another? (Y/N) ").upper()
                    if opt2 == 'Y':
                        word_to_add = input("Word to add: ")
                        word_to_add = f'{word_to_add}\n'
                        add_to_wild.write(word_to_add)
                        print(f"Added {word_to_add}", end='')
                    elif opt2 == 'N':
                        break
                    else:
                        print("Stop being dumb")
                        break
                add_to_wild.close()
        elif opt1 == 'N':
            break
        else:
            print("Invalid Input...")


def init_wildcards():
    while True:
        wildcard_submenu_opt = input("You have not generated a wildcards.txt file yet, would you like to? (Y/N) ").upper()
        if wildcard_submenu_opt == 'Y':
                Path(f"{cwdfiles}/wildcards.txt").touch()
                print(f"{cwdfiles}/wildcards.txt created...")
                break      
        elif wildcard_submenu_opt == 'N':
            print(f"Wildcards.txt not created, you can create one at any time.")
            break
        else:
            print("Invalid Input... Please Enter Y or N")


def grabVerb():
    # verbs_length = 30802
    with open(f"{cwdfiles}/verbs.txt") as verbs:
        verbcontent = verbs.readlines()
        randint = random.randint(0, (len(verbcontent) - 1))
        outbound_verb = verbcontent[randint]
        return outbound_verb.strip("\n")


def grabNoun():
    # nouns_length = 90963
    with open(f"{cwdfiles}/nouns.txt") as nouns:
        noun_content = nouns.readlines()
        randint = random.randint(0, (len(noun_content) - 1))
        outbound_noun = noun_content[randint]
        return outbound_noun.strip("\n")


def grabAdj():
    # adj_length = 28479
    with open(f"{cwdfiles}/adjectives.txt") as adjectives:
        adjectives_content = adjectives.readlines()
        randint = random.randint(0, (len(adjectives_content) - 1))
        outbound_adj = adjectives_content[randint]
        return outbound_adj.strip("\n")


def grabWildcard():
    with open(f"{cwdfiles}/wildcards.txt") as wildcard:
        wildcard_content = wildcard.readlines()
        randint = random.randint(0, (len(wildcard_content) - 1))
        outbound_wildcard = wildcard_content[randint]
        return outbound_wildcard.strip("\n")


def nameGenerator():
    opt_wc_max = 9
    if Path(f"{cwdfiles}/wildcards.txt").exists():
        opt_wc_max = 12
    roller = random.randint(1, opt_wc_max)
    roller2 = random.randint(1, opt_wc_max)
    if(roller >= 1 and roller <= 3):
        firstWord = grabAdj()
        type1 = "adj"
    elif(roller >= 4 and roller <= 6):
        firstWord = grabNoun()
        type1 = "noun"
    elif(roller >= 7 and roller <= 9):
        firstWord = grabVerb()
        type1 = "verb"
    elif(roller >= 10):
        firstWord = grabWildcard()
        type1 = "wildcard"
    else:
        print(f"something broke.... rand = {roller}")

    if(roller2 >= 1 and roller2 <= 3):
        secondWord = grabAdj()
        type2 = "adj"
    elif(roller2 >= 4 and roller2 <= 6):
        secondWord = grabNoun()
        type2 = "noun"
    elif(roller2 >= 7 and roller2 <= 9):
        secondWord = grabVerb()
        type2 = "verb"
    elif(roller2 >= 10):
        secondWord = grabWildcard()
        type2 = "wildcard"
    else:
        print(f"something broke.... rand = {roller2}")

    types = f"{type1}-{type2}"
    name = f"{firstWord.upper()}-{secondWord.upper()}"
    return name, types


def save_result(name_list: list[str]):
    for names in name_list:
        while True:
            print(f"SAVE (Y/N): {names} ---> ", end='')
            y_n = input().upper()
            if y_n == 'Y':
                names = f'{names}\n'
                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                    save.write(names)
                    print(f"Saving: {names}", end='')
                    save.close()
                    break
            if y_n == 'N':
                print(f"Discarding {names}")
                break
            else:
                print("Invalid Input")


def menu():
    quicksave = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        main_option = input("1. Generate\n2. Edit wildcards.txt\n3. Exit\nOption: ")
        if main_option == '1':
            count = 0
            tempStore = []
            while count < 10:
                name, types = nameGenerator()
                print(f"{count}. {name} {types}")
                tempStore.append(name)
                count += 1
                if count == 10:
                    while True:
                        save_option = input("Save Any of the Above? (Y/N): ").upper()
                        if save_option == 'Y':
                            save_result(tempStore)
                            break
                        elif save_option == 'N' or save_option == '.':
                            break
                        elif save_option in quicksave:
                            save_option = int(save_option)
                            quick_save_name = f'{tempStore[save_option]}\n'
                            print(f"Quicksaving {tempStore[save_option]}")
                            if Path(f"{cwdfiles}/savedNames.txt").exists():                                    
                                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                                    save.write(quick_save_name)
                                    save.close()
                            else:
                                Path(f"{cwdfiles}/savedNames.txt").touch()
                                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                                    save.write(quick_save_name)
                                    save.close()
                        else:
                            print("Invalid Input")
        elif main_option == '2':
            if Path(f"{cwdfiles}/wildcards.txt").exists():
                manage_wildcards()
            else:
                init_wildcards()
                if Path(f"{cwdfiles}/wildcards.txt").exists():
                    manage_wildcards()

        elif main_option == '3':
            exit()
        else:
            print("Invalid Input")


def main():
    if Path(f"{cwdfiles}/wildcards.txt").exists():
        menu()
    else:
        init_wildcards()
        menu()



if __name__ == '__main__':
    main()
