#take two words, slam them together, create a new name for something that you'd prefer to keep context away from.
# TODO:
    # Make an alliteration mode
    # Make a mode for specific combinations (verb-noun only, noun-adj only, etc)
    # Make a mode for Syllables


from pathlib import Path
# Add proper pathing functions in at some point. Hardcoding is bad and you should feel bad

import random
seed = random.seed()
cwdfiles = Path('./files/')

# Deprecated abspaths:
    # C:/Users/Patrick/Documents/VSCODE/personal-python/files/verbs.txt
    # C:/Users/Patrick/Documents/VSCODE/personal-python/files/nouns.txt
    # C:/Users/Patrick/Documents/VSCODE/personal-python/files/adjectives.txt
    # C:/Users/Patrick/Documents/VSCODE/personal-python/files/wildcards.txt
def grabVerb():
    verbs_length = 30802
    with open(f"{cwdfiles}/verbs.txt") as verbs:
        verbcontent = verbs.readlines()
        randint = random.randint(0, (len(verbcontent) - 1))
        # randint = random.randint(0, verbs_length)
        # print(f"verbs RandInt = {randint}")
        # print(f"verb = {verbs.readline(100)}")
        outbound_verb = verbcontent[randint]
        return outbound_verb.strip("\n")

def grabNoun():
    nouns_length = 90963
    with open(f"{cwdfiles}/nouns.txt") as nouns:
        noun_content = nouns.readlines()
        randint = random.randint(0, (len(noun_content) - 1))
        # randint = random.randint(0, nouns_length)
        # print(f"nouns RandInt = {randint}")
        # print(f"noun = {nouns.readline(100)}")
        outbound_noun = noun_content[randint]
        return outbound_noun.strip("\n")

def grabAdj():
    adj_length = 28479
    with open(f"{cwdfiles}/adjectives.txt") as adjectives:
        adjectives_content = adjectives.readlines()
        randint = random.randint(0, (len(adjectives_content) - 1))
        # randint = random.randint(0, adj_length)
        # print(f"adjectives RandInt = {randint}")
        # print(f"adjective = {adjectives.readline(100)}")
        outbound_adj = adjectives_content[randint]
        return outbound_adj.strip("\n")

def grabWildcard():
    with open(f"{cwdfiles}/wildcards.txt") as wildcard:
        wildcard_content = wildcard.readlines()
        randint = random.randint(0, (len(wildcard_content) - 1))
        # print(f"adjectives RandInt = {randint}")
        # print(f"adjective = {adjectives.readline(100)}")
        # print(f"DEBUG - WILDCARD {randint} {len(wildcard_content)} {wildcard_content[254]}")
        outbound_wildcard = wildcard_content[randint]
        return outbound_wildcard.strip("\n")

def nameGenerator():
    roller = random.randint(1, 9)
    roller2 = random.randint(1, 9)
    wildcard = random.randint(1, 30)
    # print(roller, roller2)
    if(roller >= 0 and roller < 3):
        firstWord = grabAdj()
        type1 = "adj"
    elif(roller >= 3 and roller < 6):
        firstWord = grabNoun()
        type1 = "noun"
    elif(roller >= 6):
        firstWord = grabVerb()
        type1 = "verb"
    else:
        print(f"something broke.... rand = {roller}")
    
    if(roller2 >= 0 and roller2 < 3):
        secondWord = grabAdj()
        type2 = "adj"
    elif(roller2 >= 3 and roller2 < 6):
        secondWord = grabNoun()
        type2 = "noun"
    elif(roller2 >= 6):
        secondWord = grabVerb()
        type2 = "verb"
    else:
        print(f"something broke.... rand = {roller2}")
    if(wildcard >= 11 and wildcard <= 14):
        firstWord = grabWildcard()
        type1 = "wildcard"
    elif(wildcard >= 21 and wildcard <= 24):
        secondWord = grabWildcard()
        type2 = "wildcard"
    elif(wildcard == 1):
        firstWord = grabWildcard()
        secondWord = grabWildcard()
        type1 = "wildcard"
        type2 = "wildcard"
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
                with open("C:/Users/Patrick/Documents/VSCODE/personal-python/files/genSaved.txt", mode='a') as save:
                    save.write(names)
                    save.close()
                    break
            if y_n == 'N':
                print(f"Discarding {names}")
                break
            else:
                print("Invalid Input")

def menu():
    # print("Enter number and enter to save to nameSaves.txt")
    quicksave = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        main_option = input("1. Generate\n2. Exit\nOption: ")
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
                        elif save_option == 'N' or save_option == '.':
                            break
                        elif save_option in quicksave:
                            save_option = int(save_option)
                            quick_save_name = f'{tempStore[save_option]}\n'
                            print(f"Quicksaving {tempStore[save_option]}")
                            with open("C:/Users/Patrick/Documents/VSCODE/personal-python/files/genSaved.txt", mode='a') as save:
                                save.write(quick_save_name)
                                save.close()
                        else:
                            print("Invalid Input")
        elif main_option == '2':
            exit()
        else:
            print("Invalid Input")



def __main__():
    menu()



if __name__=='__main__':
     __main__()