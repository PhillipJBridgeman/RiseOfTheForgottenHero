import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def basic_attack(self, attacker, target):
        if attacker.stats['stamina'] >= 1:
            attacker.stats['stamina'] -= 1
            damage = attacker.stats['attack'] + random.randint(1, 5)
            print(f"{attacker.name} performs a basic attack on {target.name} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{attacker.name} does not have enough stamina to perform a basic attack.")

    def special_attack(self, attacker, target, skill, stamina_cost, mana_cost=0):
        if attacker.stats['stamina'] >= stamina_cost and attacker.stats['mana'] >= mana_cost:
            attacker.stats['stamina'] -= stamina_cost
            attacker.stats['mana'] -= mana_cost
            damage = skill(target)
            print(f"{attacker.name} uses {skill.__name__} on {target.name} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{attacker.name} does not have enough stamina or mana. Performing a basic attack instead.")
            self.basic_attack(attacker, target)

    def player_turn(self):
        print(f"It's {self.player.name}'s turn!")
        action = input("Choose an action (basic_attack, slash, fireball): ").lower()
        if action in self.player.skills:
            skill = self.player.skills[action]
            if action == 'slash':
                self.special_attack(self.player, self.enemy, skill, stamina_cost=3)
            elif action == 'fireball':
                self.special_attack(self.player, self.enemy, skill, stamina_cost=1, mana_cost=5)
            else:
                self.basic_attack(self.player, self.enemy)
        else:
            print("Invalid action. Performing a basic attack instead.")
            self.basic_attack(self.player, self.enemy)

    def enemy_turn(self):
        if self.enemy.is_alive():
            damage = random.randint(5, 10)
            print(f"{self.enemy.name} attacks {self.player.name} for {damage} damage!")
            self.player.take_damage(damage)

    def start_combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player_turn()
            if self.enemy.is_alive():
                self.enemy_turn()
            else:
                print(f"{self.enemy.name} has been defeated!")
                break
        if not self.player.is_alive():
            print(f"{self.player.name} has been defeated!")
