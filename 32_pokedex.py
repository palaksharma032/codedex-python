''' Challenge: Pokedex

Objective: Practice inheritance or complex class structures by creating a system that stores and displays traits of different characters or entities. '''
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = int(entry)
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        # Output the Pokémon's name twice!
        print(f"{self.name} {self.name}")

    def display_details(self):
        # Show formatted details
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")


# Creating three Pokémon objects with sample data
pikachu = Pokemon(
    entry=25,
    name="Pikachu",
    types=["Electric"],
    description="It has small electric sacs on both its cheeks. If threatened, it loses electric charges from the sacs.",
    is_caught=True
)

bulbasaur = Pokemon(
    entry=1,
    name="Bulbasaur",
    types=["Grass", "Poison"],
    description="A strange seed was planted on its back at birth. The seed slowly grows larger.",
    is_caught=False
)

charmander = Pokemon(
    entry=4,
    name="Charmander",
    types=["Fire"],
    description="The flame that burns at the tip of its tail is an indication of its emotions.",
    is_caught=True
)

# Using methods on each object
pikachu.speak()
pikachu.display_details()

print("\n") # Just for separation

bulbasaur.speak()
bulbasaur.display_details()

print("\n")

charmander.speak()
charmander.display_details()