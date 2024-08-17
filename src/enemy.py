import random

class Enemy:
    def __init__(self, player_level, is_boss=False, type_override=None):
        self.type = type_override if type_override else self.enemy_type(player_level)
        self.name = self.type
        self.level = self.enemy_level(player_level)
        self.is_boss = is_boss
        self.stats = self.initialize_stats()
        self.skills = self.enemy_skills()
        self.loot = self.enemy_loot()
        self.gold = self.gold_drop()
        self.experience_reward = self.enemy_experience_reward()

    def enemy_type(self, player_level):
        possible_enemies = {
            1: "rat",
            2: "goblin",
            3: "skeleton",
            4: "zombie",
            5: "orc",
            6: "troll",
            7: "ogre",
            8: "Dark Wizard",
            9: "Vampire",
            10: "Ghost",
            11: "Dragon"
        }

        if player_level > 5:
            possible_enemies = {k: v for k, v in possible_enemies.items() if k > 2}

        return random.choice(list(possible_enemies.values()))

    def enemy_level(self, player_level):
        if self.type == "Dragon":
            return 20
        return random.randint(max(1, player_level - 2), player_level + 2)

    def initialize_stats(self):
        base_stats = {
            "health": 50 + self.level * 10,
            "attack": 5 + self.level * 2,
            "defense": 5 + self.level * 2,
            "stamina": 20 + self.level * 2,
            "mana": 0 if self.type in ["rat", "goblin"] else 10 + self.level * 2,
            "intelligence": 5 if self.type in ["Dark Wizard", "Vampire"] else 2
        }

        if self.type == "Dragon":
            for key in base_stats:
                base_stats[key] += 50
            self.is_boss = True

        if self.is_boss:
            for key in base_stats:
                base_stats[key] *= 1.5

        return base_stats

    def enemy_skills(self):
        skills = {
            "rat": {"Bite": 5},
            "goblin": {"Slash": 10},
            "skeleton": {"Bone Throw": 8},
            "zombie": {"Bite": 7, "Rot": 5},
            "orc": {"Smash": 12},
            "troll": {"Regenerate": 10},
            "ogre": {"Crush": 15},
            "Dark Wizard": {"Fireball": 20, "Curse": 10},
            "Vampire": {"Drain Life": 18, "Bat Form": 12},
            "Ghost": {"Haunt": 10, "Phantom Strike": 12},
            "Dragon": {"Fire Breath": 30, "Tail Swipe": 25, "Roar": 20}
        }
        return skills.get(self.type, {"Bite": 5})

    def enemy_loot(self):
        loot_table = {
            "rat": ["Rat Tail"],
            "goblin": ["Goblin Dagger"],
            "skeleton": ["Bone Fragment", "Rusty Sword"],
            "zombie": ["Rotten Flesh", "Torn Clothes"],
            "orc": ["Orcish Axe"],
            "troll": ["Troll Fat"],
            "ogre": ["Ogre Club"],
            "Dark Wizard": ["Magic Staff", "Dark Robes"],
            "Vampire": ["Vampire Fangs", "Blood Potion"],
            "Ghost": ["Ectoplasm"],
            "Dragon": ["Dragon Scale", "Dragon Claw", "Legendary Sword"]
        }
        loot = loot_table.get(self.type, [])
        return random.choice(loot) if loot else None

    def gold_drop(self):
        gold_table = {
            "rat": 20,
            "goblin": 30,
            "skeleton": 25,
            "zombie": 15,
            "orc": 50,
            "troll": 70,
            "ogre": 80,
            "Dark Wizard": 100,
            "Vampire": 120,
            "Ghost": 40,
            "Dragon": 500
        }
        return gold_table.get(self.type, 0)

    def enemy_experience_reward(self):
        level_ranges = [
            (5, 50),
            (10, 40),
            (15, 30),
            (20, 20),
            (25, 10),
            (30, 5),
            (35, 2),
            (40, 1)
        ]

        if self.is_boss:
            return 500 * self.level

        for max_level, multiplier in level_ranges:
            if self.level <= max_level:
                return multiplier * self.level

        return self.level

    def take_damage(self, damage):
        self.stats['health'] -= damage
        if self.stats['health'] <= 0:
            print(f"{self.type} has been defeated!")
        else:
            print(f"{self.type} takes {damage} damage! Health is now {self.stats['health']}.")

    def is_alive(self):
        return self.stats['health'] > 0

    def perform_attack(self, attack_name, target):
        if attack_name in self.skills:
            damage = self.skills[attack_name]
            print(f"{self.type} uses {attack_name} on {target.name} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{self.type} tries to attack, but fails!")