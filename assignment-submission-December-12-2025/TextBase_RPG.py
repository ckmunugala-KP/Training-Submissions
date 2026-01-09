import random

# ------------------ Inventory (Composition) ------------------
class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(f"{item} added to inventory.")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            return True
        print("Item not found.")
        return False

    def show_items(self):
        if not self.__items:
            print("Inventory is empty.")
        else:
            print("Inventory:", ", ".join(self.__items))


# ------------------ Character Base Class ------------------
class Character:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.inventory = Inventory()  # Composition

    # Encapsulation (Getters)
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def is_alive(self):
        return self.__health > 0

    # Combat logic
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.__attack)
        print(f"{self.__name} attacks {enemy.get_name()} for {damage} damage!")
        enemy.take_damage(damage)


# ------------------ Character Classes ------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack=15)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=25)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=18)


# ------------------ Enemy ------------------
class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack=12)


# ------------------ Character Selection ------------------
def choose_character(name):
    print("\nChoose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# ------------------ Combat System ------------------
def combat(player, enemy):
    print(f"\n⚔️ Combat Started: {player.get_name()} vs {enemy.get_name()} ⚔️")

    while True:
        if not player.is_alive():
            print("\n💀 You were defeated!")
            break

        if not enemy.is_alive():
            print("\n🎉 You defeated the enemy!")
            break

        print(f"\n{player.get_name()} Health: {player.get_health()}")
        print(f"{enemy.get_name()} Health: {enemy.get_health()}")

        print("\nActions:")
        print("1. Attack")
        print("2. Use Potion")
        print("3. View Inventory")
        print("4. Exit Game")

        action = input("Choose action: ")

        if action == "1":
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_enemy(player)

        elif action == "2":
            if player.inventory.remove_item("Potion"):
                print("You healed 20 HP!")
            if enemy.is_alive():
                enemy.attack_enemy(player)

        elif action == "3":
            player.inventory.show_items()
            continue

        elif action == "4":
            print("\n👋 Exiting game. Thanks for playing!")
            break

        else:
            print("Invalid action. Try again.")


# ------------------ Main Game ------------------
def main():
    print("🗡️ Welcome to the Text-Based RPG 🗡️")

    name = input("Enter your character name: ")
    player = choose_character(name)

    # Starter items
    player.inventory.add_item("Potion")
    player.inventory.add_item("Potion")

    enemy = Enemy("Goblin")

    combat(player, enemy)

    print("\nGame Over.")


# ------------------ Program Entry ------------------
if __name__ == "__main__":
    main()
