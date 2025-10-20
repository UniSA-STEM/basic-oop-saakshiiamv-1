"""
File: Rig.py
Description: The rig class represents the computer system of a hacker.
Handling capabilities of storage, upgrades, damage, and generating assets.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from typing import assert_type

from Asset import Asset
import random

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

    # generates 1 random asset at a time

    def generate_asset(self):
        asset_types = [
            ("CryptoToken", "A digital currency that acquires or repairs rig"),
            ("Data Spike", "Hacking tool used in battles"),
            ("Removable Drive", "Extraction device found in rigs"),
            ("Security Chip", "Encryption and decryption tool for assets"),
            ("Hardware Patch", "Component to upgrade rigs")
        ]

        name, description = random.choice(asset_types)
        new_asset = Asset(name, description)

        # if there is space available adds to storage
        if self.store_asset(new_asset):
            print(f"{self.name} generated: {new_asset}")

        else:
            print(f"{self.name} generated {new_asset}, however storage full.")

        return new_asset

    # get a description of rig's current condition
    def rig_condition(self):
        if self.broken_state:
            return f"Broken - level {self.upgrade_level}."

        else:
            return f"Pristine - level {self.upgrade_level}."

    # stores asset into rig storage
    def store_asset(self, asset):

        # if assets are encrypted cannot store
        if asset.is_encrypted:
            print(f"{asset.name} is encrypted, therefore cannot be stored.")
            return False

        # calculate maximum storage capacity
        # then checks if storage is full
        max_storage = 3 + self.upgrade_level * 2

        if len(self.storage) >= max_storage:
            print(f"{self.name} storage full, can't store asset: {asset.name}".)
            return False

        # adding to storage list
        self.storage.append(asset)
        print(f"{asset.name} stored in {self.name}.")
        return True

    def release_asset(self, asset_name):
        for i, asset in enumerate(self.storage):
            if asset.name == asset_name and not asset.encrypted:
                released_asset = self.storage.pop(i)
                print(f"{asset_name} has been released from {self.name}.")
                return released_asset

        # error reporting - if asset is encrypted or not found
        if any(asset.name == asset_name for asset in self.storage):
            print(f"Asset {asset_name} is encrypted and cannot be released.")
        else:
            print(f"Asset {asset_name} not found.")

        return None

    def __str__(self):
        pass