# Battle function with user menu for actions
from Characters import Character, Warrior, Mage, Cleric, Influencer, EvilWizard,    create_character, clear_console
import os
import random
def battle(player, wizard):
    if player.name.lower() == "zelda" and isinstance(player, Mage):
        wizard.name = "Gannondorf"
    while wizard.health > 0 and player.health > 0:
        # Print player's turn menu
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ").strip()

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice, try again.")
            input("Press Enter to continue...")
            continue

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            # Check for Warrior's shield block
            if isinstance(player, Warrior) and player.shielded:
                print(f"{player.name} blocks the attack with their shield! No damage taken.")
                player.shielded = False  # Reset shield
            else:
                wizard.attack(player)

            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                break
        input("Press Enter to continue...")
        clear_console()  # Cross-platform console clear
    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")
