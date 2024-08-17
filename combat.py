import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self, attacker, target, damage, description):
        print(f"{attacker.name} {description} {target.name} for {damage} damage!")
        target.take_damage(damage)

    def basic_attack(self, attacker, target):
        if attacker.stats['stamina'] >= 1:
            attacker.stats['stamina'] -= 1
            damage = attacker.stats['attack'] + random.randint(1, 5)
            self.attack(attacker, target, damage, "performs a basic attack on")
        else:
            print(f"{attacker.name} does not have enough stamina to perform a basic attack.")

    def special_attack(self, attacker, target, skill_name, stamina_cost, mana_cost=0):
        if attacker.stats['stamina'] >= stamina_cost and attacker.stats['mana'] >= mana_cost:
            attacker.stats['stamina'] -= stamina_cost
            attacker.stats['mana'] -= mana_cost
            skill, _, _, _ = attacker.skills[skill_name]  # Extract the skill function from the tuple
            damage = skill(target)
            self.attack(attacker, target, damage, f"uses {skill_name} on")
            self.regenerate_resources(attacker, stamina_cost, mana_cost)
        else:
            print(f"{attacker.name} does not have enough stamina or mana. Performing a basic attack instead.")
            self.basic_attack(attacker, target)

    def regenerate_resources(self, attacker, stamina_spent, mana_spent):
        stamina_regen = stamina_spent // 2
        mana_regen = mana_spent // 2
        attacker.stats['stamina'] += stamina_regen
        attacker.stats['mana'] += mana_regen
        print(f"{attacker.name} regenerates {stamina_regen} stamina and {mana_regen} mana.")
        print("-------")

    def player_turn(self):
        print(f"It's {self.player.name}'s turn!")
        available_actions = ', '.join([f"{name} (Cost: {cost[0]} stamina, {cost[1]} mana)" for name, cost in self.get_skill_costs().items()])
        action = input(f"Choose an action ({available_actions}): ").lower()

        if action in self.player.skills:
            cost = self.get_skill_costs().get(action, (1, 0))
            self.special_attack(self.player, self.enemy, action, stamina_cost=cost[0], mana_cost=cost[1])
        else:
            print("Invalid action. Performing a basic attack instead.")
            self.basic_attack(self.player, self.enemy)

    def get_skill_costs(self):
        # Return the stamina and mana costs for each skill based on the player's class
        return {name: (stamina_cost, mana_cost) for name, (skill, stamina_cost, mana_cost, description) in self.player.skills.items()}

    def enemy_turn(self):
        if self.enemy.is_alive():
            damage = random.randint(5, 10)
            self.attack(self.enemy, self.player, damage, "attacks")
        print("-------")

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