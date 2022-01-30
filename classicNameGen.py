
# TODO:
# Aliteration (sort of added 2022-01-28)
# More Granular Generation (custom generation added 2022-01-27)
# Syllables
# Add input validation to wildcards.txt (can be bypassed regardless in a file manager though... so maybe doesn't matter?)
# Clean up files and dependencies (seems good enough 2022-01-25)
# get rid of camelcased functions and variables

import re
import os
import random
from inspect import getsourcefile
from pathlib import Path
cwdfiles = f"{os.path.dirname(getsourcefile(lambda:0))}/files"
set_alliteration = False
output_count = 10


# Not MacOS Safe
# cwdfiles = f"{os.path.dirname(os.path.realpath(__file__))}/files"

# Quite the mess of nested menues here ---- > fixed 2022-01-30
def global_settings():
    global set_alliteration
    global output_count
    while True:
        print(f"""Global Settings
        1. Toggle simple alliteration for all outputs? (Currently: {set_alliteration})
        2. Change output count (Currently: {output_count})
        3. Return """)
        opt = input("Option: ")
        if opt == '1':
            if set_alliteration == False:
                while True:
                    subopt = input("Turn Alliteration On? (Y/ N) ").upper()
                    if subopt == 'Y' or subopt == '1':
                        set_alliteration = True
                        print(f"Alliteration mode is now set to {set_alliteration}")
                        break
                    elif subopt == 'N' or subopt == '2':
                        print(f"Alliteration mode will remain set to {set_alliteration}")
                        break
                    else:
                        print(f"Invalid Input")
                break
            elif set_alliteration == True:
                while True:
                    subopt = input("Turn Alliteration Off? (Y/ N) ").upper()
                    if subopt == 'Y' or subopt == '1':
                        set_alliteration = False
                        print(f"Alliteration mode is now set to {set_alliteration}")
                        break
                    elif subopt == 'N' or subopt == '2':
                        print(f"Alliteration mode will remain set to {set_alliteration}")
                        break
                    else:
                        print(f"Invalid Input")
                break
        elif opt == '2':
            print(f"Edit output count? Currently set to {output_count}. ")
            while True:
                opt2 = input("Option (Y/N): ").upper()
                if opt2 == 'Y' or opt2 == '1':
                    print(f"Enter a number between 1 and 25 (note that larger numbers make for a noisy output) ")
                    while True:
                        subopt = input("Set output count: ")
                        if subopt.isdigit():
                            if int(subopt) <= 25 and int(subopt) > 0:
                                output_count = int(subopt)
                                print(f"Output Count set to {output_count}")
                                break
                            else:
                                print(f"Invalid Input, enter an integer 25 or lower")
                        else:
                            print(f"Invalid Input, not a valid number.")
                    break
                elif opt2 == 'N' or opt2 == '2':
                    print(f"Output count will remain set to: {output_count}")
                    break
                else:
                    print("Invalid Input")
        elif opt == '3' or opt == '.':
            print("Returning to Menu")
            break
        else:
            print("Invalid Input")
            

def display_help():
    print(f"""How to use:
    You can navigate this program with your keyboard or just your numpad.
    Menu Controls:
        Y / N is not case sensitive.
        1 / 2 can substitute Y and N respectively.
        All Exit Options can be accessed with '.'
    
    Notes on outputs:
    Default configuration will display the type of each name generated following the name.
    If Alliteration is set to ON, the number following the name is the attempts it took to find an alliterated match.""")

# Still in testing --> Needs refinement but is functional
# This function is for testing alliteration functionality, not to be used in main.
# As of 2022-01-30 Needs to be actually implemented.
def alliteration():
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    while True:
        test1 = grabNoun()
        test2 = grabNoun()
        allit1 = [L for i, L in enumerate(test1) if i < 2]
        allit2 = [L for i, L in enumerate(test2) if i < 2]
        # if test1[0] == test2[0]:
        #     print(test1, test2)
        #     print(allit1, allit2)
        #     print(F"This took {count} Tries")
        #     break
        if allit1 == allit2:
            print(test1, test2)
            print(allit1, allit2)
            print(F"This took {count} Tries (if)")
            break
        elif (allit1[0] == allit2[0]) and ((allit1[1] and allit2[1]) in vowels):
            print(test1, test2)
            print(allit1, allit2)
            print(F"This took {count} Tries (elif)")
            break
        count += 1


def manage_wildcards():
    while True:
        opt1 = input("Would you like to add to wildcards.txt? (Y/N) ").upper()
        if opt1 == 'Y' or opt1 == '1':
            with open(f"{cwdfiles}/wildcards.txt", mode='a') as add_to_wild:
                word_to_add = input("Enter a word to add to your wildcard list: ")
                word_to_add = f'{word_to_add}\n'
                add_to_wild.write(word_to_add)
                print(f"Added {word_to_add}", end='')
                while True:
                    opt2 = input("Add Another? (Y/N) ").upper()
                    if opt2 == 'Y' or opt2 == '1':
                        word_to_add = input("Word to add: ")
                        word_to_add = f'{word_to_add}\n'
                        add_to_wild.write(word_to_add)
                        print(f"Added {word_to_add}", end='')
                    elif opt2 == 'N' or opt2 == '2':
                        break
                    else:
                        print("Stop being dumb")
                        break
                add_to_wild.close()
        elif opt1 == 'N' or opt1 == '2':
            break
        else:
            print("Invalid Input...")


def init_wildcards():
    while True:
        wildcard_submenu_opt = input("You have not generated a wildcards.txt file yet, would you like to? (Y/N) ").upper()
        if wildcard_submenu_opt == 'Y' or wildcard_submenu_opt == '1':
                Path(f"{cwdfiles}/wildcards.txt").touch()
                print(f"{cwdfiles}/wildcards.txt created...")
                break      
        elif wildcard_submenu_opt == 'N' or wildcard_submenu_opt == '2':
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


def default_name_generation() -> (str):
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

# Deprecated
def quicksave_logic(name_list: list[str]):
    while True:
        save_option = input("Save Any of the Above? (Y/N): ").upper()
        if save_option == 'Y':
            long_save_logic(temp_store_list)
            break

        else:
            print("Invalid Input")

# Deprecated
def long_save_logic(name_list: list[str]):
    for names in name_list:
        while True:
            print(f"SAVE (Y/N): {names} ---> ", end='')
            y_n = input().upper()
            if y_n == 'Y' or y_n == '1':
                names = f'{names}\n'
                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                    save.write(names)
                    print(f"Saving: {names}", end='')
                    save.close()
                    break
            if y_n == 'N' or y_n == '2':
                print(f"Discarding {names}")
                break
            else:
                print("Invalid Input")


def save_logic(name_list: list[str]):
    quicksave = [str(i) for i in range(0, output_count)]
    print(f"Type the index and hit enter to save, N or '.' to return: ", end='')
    
    while True:
        save_opt = input()
        if save_opt in quicksave:
            save_opt = int(save_opt)
            quick_save_name = f'{name_list[save_opt]}\n'
            print(f"Saving {name_list[save_opt]} to {cwdfiles}/savedNames.txt.\nIndex to save another, N to exit: ", end='')
            
            if Path(f"{cwdfiles}/savedNames.txt").exists():                                    
                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                    save.write(quick_save_name)
                    save.close()
            else:
                Path(f"{cwdfiles}/savedNames.txt").touch()
                with open(f"{cwdfiles}/savedNames.txt", mode='a') as save:
                    save.write(quick_save_name)
                    save.close()
        elif save_opt == 'N' or save_opt == '.':
            break
        else:
            print("Invalid Input")


def output_logic(default: bool):
    temp_store_list = []
    if default == True:
        for i in range(0, output_count):
            name, types = default_name_generation()
            print(f"{i}. {name} {types}")
            temp_store_list.append(name)
        save_logic(temp_store_list)
    elif default == False:
        settings = set_custom_settings()
        print(f"Generating with custom setting: {settings}")
        custom_repeater(settings, temp_store_list)
        while True:
            print(f"Run again with settings {settings}? (Y/N) ", end='')
            opt = input().upper()
            if opt == 'Y' or opt == '1':
                custom_repeater(settings, temp_store_list)
            elif opt == 'N' or opt == '2':
                break
            else:
                print("Invalid Input")             


def set_custom_settings() -> tuple():
    opts = ['1', '2', '3', '4', '5']
    print(f"""Set options for words 1 and 2
    1. Verb (random example verb: {grabVerb().upper()})
    2. Adjective (random example adjective: {grabAdj().upper()})
    3. Noun (random example noun: {grabNoun().upper()})
    4. Wildcard (random example wildcard: {grabWildcard().upper()})
    5. Random (default)
    """)
    while True:
        opt = input("Word 1 setting: ")
        if opt == '1':
            print("Word 1 Set to Verb")
            word1 = 'verb'
        elif opt == '2':
            print("Word 1 set to adjective")
            word1 = 'adj'
        elif opt == '3':
            print("Word 1 set to noun")
            word1 = 'noun'
        elif opt == '4':
            print("Word 1 set to wildcard")
            word1 = 'wild'
        elif opt == '5':
            print("Word 1 set to random")
            word1 = 'rand'
        else:
            print("Invalid Input")
        
        if opt in opts:
            break
    while True:
        opt = input("Word 2 setting: ")
        if opt == '1':
            print("Word 2 Set to Verb")
            word2 = 'verb'
        elif opt == '2':
            print("Word 2 set to adjective")
            word2 = 'adj'
        elif opt == '3':
            print("Word 2 set to noun")
            word2 = 'noun'
        elif opt == '4':
            print("Word 2 set to wildcard")
            word2 = 'wild'
        elif opt == '5':
            print("Word 2 set to random")
            word2 = 'rand'
        else:
            print("Invalid Input")

        if opt in opts:
            return (word1, word2)


def custom_name_generation(settings: tuple) -> str:
    for index, setting in enumerate(settings):
        if index == 0:
            if setting == 'verb':
                word1 = grabVerb()
            elif setting == 'adj':
                word1 = grabAdj()
            elif setting == 'noun':
                word1 = grabNoun()
            elif setting == 'wild':
                word1 = grabWildcard()
            elif setting == 'rand':
                roller = random.randint(1, 12)
                if(roller >= 1 and roller <= 3):
                    word1 = grabAdj()
                elif(roller >= 4 and roller <= 6):
                    word1 = grabNoun()
                elif(roller >= 7 and roller <= 9):
                    word1 = grabVerb()
                elif(roller >= 10):
                    word1 = grabWildcard()
        elif index == 1:
            if setting == 'verb':
                word2 = grabVerb()
            elif setting == 'adj':
                word2 = grabAdj()
            elif setting == 'noun':
                word2 = grabNoun()
            elif setting == 'wild':
                word2 = grabWildcard()
            elif setting == 'rand':
                roller = random.randint(1, 12)
                if(roller >= 1 and roller <= 3):
                    word2 = grabAdj()
                elif(roller >= 4 and roller <= 6):
                    word2 = grabNoun()
                elif(roller >= 7 and roller <= 9):
                    word2 = grabVerb()
                elif(roller >= 10):
                    word2 = grabWildcard()
    return f'{word1.upper()}-{word2.upper()}'      


def custom_repeater(settings: tuple, temp_store_list: list):
    for i in range(0, output_count):
        name = custom_name_generation(settings)
        print(f"{i}. {name}")
        temp_store_list.append(name)
    save_logic(temp_store_list)


def menu():
    while True:
        main_option = input("MAIN MENU\n1. Generate\n2. Edit wildcards.txt\n3. Settings\n4. Exit\n5. Help\nOption: ")
        if main_option == '1':
            if set_alliteration == True:
                print(f"WARNING: Alliteration is ON! Program may take some time to run.")
            while True:
                subopt1 = input("1. Default Generation\n2. Custom Generation\n3. Exit\nOption: ")
                if subopt1 == '1':
                    output_logic(True)
                elif subopt1 == '2':
                    output_logic(False)
                elif subopt1 == '3':
                    break
                else:
                    print("Invalid Input...")

        elif main_option == '2':
            if Path(f"{cwdfiles}/wildcards.txt").exists():
                manage_wildcards()
            else:
                init_wildcards()
                if Path(f"{cwdfiles}/wildcards.txt").exists():
                    manage_wildcards()

        elif main_option == '3':
            global_settings()

        elif main_option == '4':
            exit()
        elif main_option == '5':
            display_help()
        else:
            print("Invalid Input")


def main():
    # # For testing only # #
    # print(set_alliteration)
    # alliteration()
    # #
    if Path(f"{cwdfiles}/wildcards.txt").exists():
        menu()
    else:
        init_wildcards()
        menu()


if __name__ == '__main__':
    main()
