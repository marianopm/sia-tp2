from enum import Enum
import math

class CharacterType(Enum):
    WARRIOR = 'WARRIOR'
    ARCHER = 'ARCHER'
    DEFENDER = 'DEFENDER'
    INFILTRATOR = 'INFILTRATOR'

"""    properties
        type
        height
        strength
        agility
        expertise
        resistance
        life
        
"""
class Character():
    def __init__(self, type, height, strength_i, agility_i, expertise_i, resistance_i, life_i):
        self.type = type
        self.height = height                                # Specify Character's height.
        self.strength = 100 * math.tanh(strength_i/100)     # Specify Character's strength.
        self.agility = math.tanh(agility_i/100)             # Specify Character's agility.
        self.expertise = 6 * math.tanh(expertise_i/100)     # Specify Character's expertise.
        self.resistance = math.tanh(resistance_i/100)       # Specify Character's resistance.
        self.life = 100 * math.tanh(life_i/100)             # Specify Character's life.

    
    @property
    def attack_aptitude(self):
        # This function establish attack hability for the character.
        # Attack modifier:
        atm = 5 - (3 * self.height - 5)**4 + (3 * self.height - 5)**2 + self.height/2
        # Attack aptitude:
        return (self.agility + self.expertise) * self.strength * atm
    
    @property
    def defense_aptitude(self):
        # This function establish defense hability for self.
        # Defense modifier:
        dem = 2 + (3*self.height - 5)**4 - (3*self.height - 5)**2 - self.height/2
        # Defense aptitude:
        return (self.resistance + self.expertise)*self.life*dem
    
    @property
    def performance(self):
        # This function qualifies the performance of obj.
        attack = self.attack_aptitude
        defense = self.defense_aptitude
        # Performance (objective function):
        if self.type == CharacterType.WARRIOR:
            return  0.6 * attack + 0.4 * defense
        elif self.type == CharacterType.ARCHER:
            return  0.9 * attack + 0.1 * defense
        elif self.type == CharacterType.DEFENDER:
            return  0.1 * attack + 0.9 * defense
        elif self.type == CharacterType.INFILTRATOR:
            return  0.8 * attack + 0.3 * defense
