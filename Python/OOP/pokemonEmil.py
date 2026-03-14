class Pokemon:
    def __init__(self, name, level, max_hp):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.current_hp = max_hp

    def summary(self):
        return f"{self.name} (Lvl {self.level}) HP: {self.current_hp}/{self.max_hp}"

    def take_damage(self, amount):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} took {amount} damage! HP is now {self.current_hp}/{self.max_hp}")

    def is_fainted(self):
        return self.current_hp == 0

    def attack(self, other):
        """Generic attack – subclasses can override this."""
        base_damage = 10 + self.level
        print(f"{self.name} attacks {other.name} and deals {base_damage} damage!")
        other.take_damage(base_damage)


class FirePokemon(Pokemon):
    def __init__(self, name, level, max_hp):
        # Use parent constructor with super()
        super().__init__(name, level, max_hp)
        self.type = "Fire"

    def attack(self, other):
        # Override attack to add fire bonus
        base_damage = 10 + self.level
        bonus = 5
        total_damage = base_damage + bonus
        print(f"{self.name} uses a fire attack on {other.name}!")
        print(f"Base damage: {base_damage}, fire bonus: {bonus}")
        other.take_damage(total_damage)


class WaterPokemon(Pokemon):
    def __init__(self, name, level, max_hp):
        super().__init__(name, level, max_hp)
        self.type = "Water"

    def attack(self, other):
        # Simple example with type advantage vs FirePokemon
        base_damage = 10 + self.level
        if isinstance(other, FirePokemon):
            multiplier = 2
            total_damage = base_damage * multiplier
            print(f"{self.name} uses a water attack on {other.name}  it's super effective!")
            print(f"Base damage: {base_damage}, multiplier: {multiplier}x")
        else:
            total_damage = base_damage
            print(f"{self.name} attacks {other.name} with a water attack.")
        other.take_damage(total_damage)


# ---------- Example usage (objects) ----------

charmander = FirePokemon("Charmander", level=5, max_hp=39)
squirtle = WaterPokemon("Squirtle", level=5, max_hp=44)
pikachu = Pokemon("Pikachu", level=5, max_hp=35)

print(charmander.summary())
print(squirtle.summary())
print(pikachu.summary())
print()

# Battle examples
charmander.attack(pikachu)   # Uses FirePokemon.attack()
print()

squirtle.attack(charmander)  # Type advantage vs FirePokemon
print()

pikachu.attack(squirtle)     # Uses base class Pokemon.attack()
print()

print("Fainted?")
print(charmander.name, "fainted:", charmander.is_fainted())
print(squirtle.name, "fainted:", squirtle.is_fainted())
print(pikachu.name, "fainted:", pikachu.is_fainted())