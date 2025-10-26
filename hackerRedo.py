"""
File: Hacker.py
Description: This class handles all hacker actions such as attacks, encryption, upgrades, and etc.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from rigRedo import Rig

class Hacker:
    def __init__(self, name):
        self.name = name
        self.inventory = [] # hacker's assets
        self.rig = None # as default the hacker has no computer rigs
        self.trace_level = 0 # default level
        self.trace_threshold = 5 # level at which hacker is exposed

        # begins with a basic inventory containing a single CyrptoToken
        self.inventory.append(Asset("CryptoToken", "A digital currency that acquires or repairs rig"))
        print(f"Initialise hacker {self.name} with basic inventory.")

    # acquire rig with a CryptoToken, either using an existing one or creating a new rig
    # returns a true or false boolean output
    def acquire_rig(self, rig=None):

        # checking if rig already has a CryptoToken
        if self.rig:
            print(f"Rig {self.rig.name} already belongs to {self.name}.")
            return False

        # now finds cryptoToken in inventory, removes it and acquires a rig successfully
        crypto_token = None
        for asset in self.inventory:
            if asset.name == "CryptoToken" and not asset.is_encrypted:
                crypto_token = asset

        if not crypto_token:
            print(f"In order to acquire a rig, {self.name} needs a CryptoToken.")
            return False

        self.inventory.remove(crypto_token)

        if rig:
            self.rig = rig
        else:
            self.rig = Rig(f"Rig belongs to {self.name}.")

        print(f"{self.name} has successfully acquired {self.rig.name}!")
        return True


    # launch data spikes on another rig, increasing its trace level and consuming one spike.
    def launch_attack(self, target):

        # checking prior to attack - no rig found, broken rig, or if trace level is at max
        if not self.rig:
            print(f"{self.name} has no rig for launching an attack!")
            return False

        if self.rig.broken_state:
            print(f"Can't attack a broken rig {self.rig.name}!!")
            return False

        if self.trace_level >= self.trace_threshold:
            print(f"Can't attack, trace level is too high!!!")
            return False

        # find data spike from rig storage
        data_spike = None
        for asset in self.rig.storage:
            if asset.name == "Data Spike" and not asset.encrypted:
                data_spike = asset

        # data spike found if not returns false
        if not data_spike:
            print(f"{self.rig.name} has no available Data Spikes.")
            return False

        # remove data spike from storage to execute attack
        self.rig.storage.remove(data_spike)
        self.trace_level += 1 # increasing trace level

        print(f"{self.name} launched Data Spike attack at {target.name}.\n"
              f"New Trace Level: {self.trace_level}")
        target.take_hit()
        return True


    # method to extract unsecured assets from a broken rig
    def extract_asset(self, target):

        # since extraction action can only be performed on a broken system
        # checking if the target has been comprimised
        if not target.broken_state:
            print(f"{target.name} can't be extracted, rig is not broken.")
            return False

        # searching for removable drive in rig storage
        # conditions: drive must exist and not be encrypted
        removable_drive = None
        for asset in self.rig.storage:
            if asset.name == "Removable Drive" and not asset.encrypted:
                removable_drive = asset

        # removable drive found if not returns false
        if not removable_drive:
            print(f"Could not find Removable Drive in storage!\n"
                  f"Can't perform extraction.")
            return False

        # begin extraction of unencrypted assets
        self.rig.storage.remove(removable_drive)

        # tracks number of successful extractions
        extract_count = 0

        # iterate through original list using [:]
        # only extracts assets that are not encrypted and removes them from the storage
        for asset in target.storage[:]:
            if not asset.encrypted:
                target.storage.remove(asset)

                # transfers assets to the hacker's rig storage
                self.rig.store_asset(asset)
                extract_count += 1

        print(f"{extract_count} unencrypted assets successfully extracted from {target.name}")
        return extract_count > 0

    # method to encrypt a target asset using a security chip from a specific location.
    def encrypt_asset(self, asset, location):

        # checking if the target asset is already encrypted
        if asset.encrypted:
            print(f"{asset.name} is already encrypted.")
            return False

        # searches for security chip in a specified location
        # conditions: chip must exist and not be encrypted
        security_chip = None
        search_location = self.inventory if location == "inventory" else self.rig.storage
        for item in search_location:
            if item.name == "Security Chip" and not item.encrypted:
                security_chip = item

        # security chip found if not returns False
        if not security_chip:
            print(f"There is no security chip in the {location}.")
            return False

        # apply encryption to the target asset
        search_location.remove(security_chip)
        asset.encrypted = True
        print(f"{asset.name} successfully encrypted.")
        return True

    # decryption method
    def decrypt_asset(self, asset, location):

        # checking that the target asset is not encrypted
        if not asset.encrypted:
            print(f"{asset.name} is not encrypted.")
            return False

        # searches for security chip in a specified location
        # conditions: chip must exist and not be encrypted
        security_chip = None
        search_location = self.inventory if location == "inventory" else self.rig.storage
        for item in search_location:
            if item.name == "Security Chip" and not item.encrypted:
                security_chip = item

        # security chip found if not returns False
        if not security_chip:
            print(f"There is no security chip in the {location}.")
            return False

        # apply encryption to the target asset
        search_location.remove(security_chip)
        asset.encrypted = True
        print(f"{asset.name} successfully encrypted.")
        return True

    # update a hacker's rig using a hardware patch
    def upgrade_rig(self):

        # checks if the hacker has a rig to even upgrade
        if not self.rig:
            print(f"Can't update if {self.name} has no rig.")
            return False

        # searches inventory for hardware patch
        hardware_patch = None
        for asset in self.inventory:
            if asset.name == "Hardware Patch" and not asset.encrypted:
                hardware_patch = asset

        # hardware patch found if not returns False
        if not hardware_patch:
            print(f"Inventory has no hardware patch.")
            return False

        self.inventory.remove(hardware_patch)

        # increases the rig's upgrade level with this call
        upgraded = self.rig.upgrade(hardware_patch)
        return upgraded

    # method to store assets in the inventory and rig's storage.
    def store_asset(self, asset_name):
        # checks if the hacker has a rig to even upgrade
        if not self.rig:
            print(f"Can't update if {self.name} has no rig.")
            return False

        #
        if asset_name:
            asset_storing = None
            for asset in self.inventory:
                if asset.name == asset_name and not asset.encrypted:
                    asset_storing = asset

            if asset_storing:
                if self.rig.store_asset(asset_storing):
                    self.inventory.remove(asset_storing)
                    print(f"{asset_name} successfully stored to {self.rig.name}.")
                    return True

            else:
                print(f"{asset_name} was not found in the inventory or is not encrypted.")
                return False

        else:
            # tracks number of successfully stored unencrypted assets
            store_count = 0

            # iterate through original list using [:]
            # only extracts assets that are not encrypted and removes them from the storage
            for asset in self.inventory[:]:
                if not asset.encrypted:

                    # transfers assets to the hacker's rig storage
                    if self.rig.store_asset(asset):
                        self.inventory.remove(asset)
                    target.storage.remove(asset)

                    store_count += 1

            print(f"{store_count} unencrypted assets successfully stored to {self.rig.name}")
            return store_count > 0

    # method to retrieve assets from rig storage to hacker's inventory.
    def retrieve_asset(self, asset_name):
        # checks if the hacker has a rig to even upgrade
        if not self.rig:
            print(f"{self.name} has no rig.")
            return False

        # retrieve specific asset from rig storage, use the rig's release method to extract the asset
        if asset_name:
            to_retrieve = self.rig.release(asset_name)

            # if successfully retrieve, adds the retrieved asset to the hacker's inventory
            if to_retrieve:
                self.inventory.append(to_retrieve)
                print(f"{asset_name} retrieved from {self.rig.name}.")
                return True
            return False

        else:
            # tracks number of successfully retrieved assets
            retrieve_count = 0

            # iterate through original list using [:]
            # only extracts assets that are not encrypte
            for asset in self.rig.storage[:]:
                if not asset.encrypted:

                    # release the assets from the rig storage
                    release_asset = self.rig.release(asset.name)

                    # add released asset to inventory and increment counter
                    if release_asset:
                        self.inventory.append(release_asset)
                        retrieve_count += 1

            print(f"{retrieve_count} assets retrieved from {self.rig.name}.")
            return retrieve_count > 0

    # scan hacker's inventory for a specific asset
    def scan_inventory(self, asset_name):

        # searching for asset in inventory to remove it
        for i, asset in enumerate(self.inventory):
            if asset.name == asset_name and not asset.encrypted:
                asset_found = self.inventory.pop(i)
                print(f"{asset_name} asset found and removed.")
                return asset_found

        print(f"{asset_name} asset not found or is encrypted in inventory.")
        return None

    def __str__(self):
        if self.rig:
            info = f"{self.rig.name} | Level: {self.rig.upgrade} | Damage: {self.rig.damage}/2"
        else:
            info = "None"

        return (f"------------{self.name}------------\n"
                f"Rig:           {info}\n"
                f"Trace Level:   {self.trace_level}/{self.trace_threshold}\n"
                f"Inventory:     {','.join(asset.name for asset in self.inventory)
                if self.inventory else "empty"}\n")