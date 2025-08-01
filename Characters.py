#Characters
# This lovely piece of work controls the characters in the game.
# It defines the base Character class and subclasses for specific character types.
# Base Character class
import os
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        rand = random.uniform(0, 2)
        base_damage = self.attack_power

        if rand < 0.3:
            print(f"{self.name} attacks but MISSES!")
            damage = 0
            #MISS
        elif rand >= 0.3 and rand < 1:
            print(f"{self.name} hits {opponent.name} for {base_damage} damage!")
            damage = base_damage
            #Normal hit
        elif rand >= 1 and rand < 1.5:
            scaled_damage = int(base_damage * rand)
            print(f"{self.name} lands a strong hit! {opponent.name} takes {scaled_damage} damage!")
            damage = scaled_damage
            #Scaled hit
        else:
            double_damage = base_damage * 2
            print(f"CRITICAL! {self.name} deals DOUBLE DAMAGE: {double_damage} to {opponent.name}!")
            damage = double_damage
            # DEALING DULY DEVIOUS DOUBLE DAMAGE DAAARLIN'

        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0

            
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
            print(f"{self.name} can't cancel someone without a following first, babe!")
            return
        opponent.health = 0  # Cancels opponent's health
        print(f"{self.name} cancelled {opponent.name} on social media, ending their career!")
    
    def ViralChallenge(self, opponent):
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


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Cleric")  
    print("4. Influencer")  
    
    while True:
        class_choice = input("Enter the number of your class choice: ").strip()
        if class_choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Cleric(name) 
    elif class_choice == '4':
        return Influencer(name)
