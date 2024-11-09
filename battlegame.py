WIZARD = "Wizard"
ELF = "Elf"
HUMAN = "Human"
DWARF = "Dwarf"
# Character health:
WIZARD_HP = 70
ELF_HP = 100
HUMAN_HP = 150
DWARF_HP = 100
# Character damage:
WIZARD_DAMAGE = 150
ELF_DAMAGE = 100
HUMAN_DAMAGE = 20
DWARF_DAMAGE = 50

def promptCharacterInput():
    
    while True:
        choice = input(
        "1. Wizard\n"
        "2. Elf\n"
        "3. Human\n"
        "4. Dwarf\n"
        "Choose your character: ").lower()

        if choice == 'exit':
            print("Goodbye!")
            return
        
        if choice == 'dwarf':
            character = "Dwarf"
            myHp = DWARF_HP
            myDamage = DWARF_DAMAGE
            break
        elif choice == 'wizard':
            character = "Wizard"
            myHp = WIZARD_HP
            myDamage = WIZARD_DAMAGE
            break
        elif choice == 'elf':
            character = "Elf"
            myHp = ELF_HP
            myDamage = ELF_DAMAGE
            break
        elif choice == 'human':
            character = "Human"
            myHp = HUMAN_HP
            myDamage = HUMAN_DAMAGE
            break
        else:
            print("Unknown Character")
    print(f"You have chosen: {character}!")
    print(f"Health: {myHp}\nDamage: {myDamage}")
    return (character, myHp, myDamage)

characterInput = promptCharacterInput()
if characterInput is None:
    exit()
(character, myHp, myDamage) = characterInput
dragonHp = 300
dragonDamage = 50

while True:
    dragonHp = dragonHp - myDamage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragonHp}.\n")
    if dragonHp <= 0:
        print("The Dragon has lost the battle.")
        break
    myHp = myHp - dragonDamage
    print(f"The Dragon damaged the {character}!")
    print(f"The {character}'s hitpoints are now: {myHp}.\n")
    if myHp <= 0:
        print(f"The {character} has lost the battle.")
        break
        

