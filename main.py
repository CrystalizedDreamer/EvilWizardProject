import random
from Characters import Character, Warrior, Mage, Cleric, Influencer, EvilWizard, create_character, clear_console
from Battle import battle
# Main function to handle the flow of the game

def main():
    while True:
        # Character creation phase
        player = create_character()

        # Evil Wizard is created
        wizard = EvilWizard("The Dark Wizard")

        # Start the battle
        battle(player, wizard)

        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    #Idea section:
    #Refactor the code to place specials into the superclass and then override them in the subclasses