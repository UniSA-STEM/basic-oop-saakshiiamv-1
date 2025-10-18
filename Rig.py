"""
File: Rig.py
Description: The rig class represents the computer system of a hacker.
Handling capabilities of storage, upgrades, damage, and generating assets.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_count = 0 # current damage level
        self.broken_state = False # is the rig functioning?
        self.storage = [] # storage for assets
        self.upgrade_level = 0

    # every rig starts with a starting asset of

    # todo
    # append asset from storage

    # takes damage from data spikes attack and increases the damage counter
    # if the damage threshold is reached the rig breaks.

    def take_hits(self):
        if self.broken_state:
            print(f"{self.name} is already broken.")
            return

        # increase damage count from level 0 to 1
        # rig breaks at level 2 damage
        self.damage_count += 1

        damage_threshold = max(2 - self.upgrade_level, 1)

        print(f"{self.name} took a hit! \n Damage: {self.damage_count}/{damage_threshold}")

        # checking if rig breaks
        if self.damage_count >= damage_threshold:

            # change default
            self.broken_state = True
            print(f"{self.name} is broken.")

    # repairs the rig using a cryptoToken

    def repair(self, crypto_token):
        if not self.broken_state:
            print(f"{self.name} repair not required, rig is still functional.")
            return False

        if crypto_token.name == "cryptoToken":
            self.damage_count = 0
            self.broken_state = False
            print(f"{self.name} is repaired!!")
            return True

        else:
            print("Requires cryptoToken for repair")
            return False

    # upgrades rig using a hardware patch
    def upgrade(self, hardware_patch):
        if hardware_patch.name == "Hardware Patch":
            self.upgrade_level += 1
            print(f"{self.name} upgraded to level {self.upgrade_level}.")
            return True

        else:
            print("Can't upgrade, requires a hardware patch.")
            return False




