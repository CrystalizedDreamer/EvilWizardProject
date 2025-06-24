# Base Character class
import os
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

            
    def special_ability(self, opponent):
        print("No special ability for this character.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 30
        total_Heal = self.health + heal_amount
        if total_Heal > self.max_health:
            self.health = self.max_health
            print(f"{self.name} heals to maximum health: {self.max_health}!")
        else:
            self.health += heal_amount
            print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.shielded = False  # Track if shield block is active

    def Power_Strike(self, opponent):
        opponent.health -= self.attack_power * 2  # Double damage for power strike
        print(f"{self.name} does a power strike on {opponent.name} for {self.attack_power * 2} damage!")

    def Shield_Block(self):
        self.shielded = True
        print(f"{self.name} raises their shield, preparing to block the next attack!")
    
    def special_ability(self, opponent):
        print("1. Power Strike\n2. Shield Block")
        choice = input("Choose a special ability: ")
        if choice == '1':
            self.Power_Strike(opponent)
        elif choice == '2':
            self.Shield_Block()
        else:
            print("Invalid special ability choice.")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def Ice_Spear(self, opponent):
        opponent.health -= 60  # Double damage for power strike
        print(f"{self.name} casts an ICE SPEAR at {opponent.name} for {60} damage!")

    def Insight(self, opponent):
        print(f"{self.name} has revealed {opponent.name}'s health: {opponent.health}/{opponent.max_health}")
    def special_ability(self, opponent):
        print("1. Ice Spear\n2. Insight")
        choice = input("Choose a special ability: ")
        if choice == '1':
            self.Ice_Spear(opponent)
        elif choice == '2':
            self.Insight(opponent)
        else:
            print("Invalid special ability choice.")

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=20)  # Boost
    
    def baptism(self, opponent):
        opponent.health -= opponent.health / 2
        print(f"{self.name} performs an involuntary baptism on {opponent.name}, reducing their health by half!")
    
    def exorcism(self, opponent):
        if opponent.health < opponent.max_health / 2:
            opponent.health = 0
            print(f"{self.name} successfully exorcises {opponent.name}, banishing their soul!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{self.name} attempts an exorcism on {opponent.name}, but they haven't been weakened enough yet!")
    
    def special_ability(self, opponent):
        print("1. Baptism\n2. Exorcism")
        choice = input("Choose a special ability: ")
        if choice == '1':
            self.baptism(opponent)
        elif choice == '2':
            self.exorcism(opponent)
        else:
            print("Invalid special ability choice.")
            
class Influencer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=1)
        self.viral_challenge_used = False  # Track if the viral challenge has been used
    
    def Cancellation (self, opponent):
        if not self.viral_challenge_used:
            print(f"{self.name} can't cancel someone without a followng first, babe!")
            return
        opponent.health -= opponent.health  # Cancels opponent's health
        print(f"{self.name} cancelled {opponent.name} on social media, ending their career!")
    
    def ViralChallenge(self, opponent):
        import random
        self.viral_challenge_used = True  # Mark the viral challenge as used
        result = random.randint(1, 10)
        if result > 5:
            opponent.health -= 20
            print(f"{opponent.name} injured themselves in {self.name}'s viral challenge!")
            print(f"{self.name} and {opponent.name} have gone VIRAL!")
        elif result ==5:
            self.health -= 10
            opponent.health -= 10
            print(f"{self.name}'s viral challenge injured both parties!")
            print(f"{self.name} and {opponent.name} have gone VIRAL!")
        else:
            self.health -= 20
            print(f"{self.name} injured themselves in their own challenge!")
            print(f"{self.name} and {opponent.name} have gone VIRAL!")
    def special_ability(self, opponent):
        print("1. Viral Challenge\n2. Cancellation")
        choice = input("Choose a special ability: ")
        if choice == '1':
            self.ViralChallenge(opponent)
        elif choice == '2':
            self.Cancellation(opponent)
        else:
            print("Invalid special ability choice.")
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Cleric")  
    print("4. Influencer")  
    
    class_choice = input("Enter the number of your class choice: ") #Console Clearing on Windows Devices, Linux to come later.
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Cleric(name) 
    elif class_choice == '4':
        return Influencer(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    
    
# Battle function with user menu for actions
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
        os.system('cls')  # Clear console at the end of the turn for readability
    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

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