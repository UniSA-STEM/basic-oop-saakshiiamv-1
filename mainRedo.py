"""
File: main.py
Description: All classes test code running here. Simulating battles, upgrades,
             encryption, trace management, and etc.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from rigRedo import Rig
from hackerRedo import Hacker

print("=" * 85)
print("PHASE 1. Testing base class creations")
print("=" * 85)

# creating assets
crypto = Asset("CryptoToken", "A digital currency that acquires or repairs rig")
data_spike = Asset("Data Spike", "Hacking tool used in battles")
print(f"Successfully Created Assets \n    {crypto} \n    {data_spike}")

# test rig class creation with starting assets
print("\n1.1 Testing Rig Class:")
rig = Rig("testerRig1")
print(f"Successfully Created Rig: {rig.name}")
print(f"Starter Assets: {[asset.name for asset in rig.storage]}")
print(f"Condition: {rig.rig_condition()}")

# hacker creation and rig acquisition
print("\n1.2 Hacker Class and Rig Acquisition:")
hacker = Hacker("Cyberhacker")
print(f"Hacker: {hacker.name}")
print(f"Starter Inventory: {[asset.name for asset in hacker.inventory]}")

acquisition_res = hacker.acquire_rig()
print(f"\n      Rig Acquisition Success: {acquisition_res}")
if hacker.rig:
    print(f"      Rig Name: {hacker.rig.name}")
    print(f"      Inventory after Acquisition:"
          f" {[asset.name for asset in hacker.inventory]}")

print("\nPHASE 1 TESTS COMPLETED: Testing base class creations")
print("\n" + "="*85)

def test_combat_trace_system():
    print("PHASE 2: Combat System & Trace Management")
    print("="*85)

    attacker = Hacker("Attacker")
    target = Hacker("Target")
    attacker.acquire_rig()
    target.acquire_rig(Rig("TargetMachine"))

    print("\ntest 2.1: before Combat")
    print(f"Attacker Trace: {attacker.trace_level}")
    print(f"Target Condition: {target.rig.rig_condition()}")
    print(f"Attacker data spikes: {
    sum(1 for a in attacker.rig.storage if a.name == "Data Spike")
    }")

    print("\ntest 2.2: Combat sequence")
    attack1 = attacker.launch_attack(target.rig)
    print(f"- First Attack: {"Success" if attack1 else "Failed"}")
    print(f"- Attacker Trace: {attacker.trace_level}")
    print(f"- Target Damage: {target.rig.damage_count}")

    attack2 = attacker.launch_attack(target.rig)
    print(f"- Second Attack: {"Success" if attack2 else "Failed"}")
    print(f"- Attacker Trace: {attacker.trace_level}")
    print(f"- Target Damage: {target.rig.damage_count}")

    print("\nPHASE 2 TESTS COMPLETED: Combat System & Trace Management")
    print("\n" + "=" * 85)
    return attacker, target

def test_asset_extraction():
    print("PHASE 3: Extracting Assets System")
    print("="*85)

    extractor = Hacker("Villain Extractor")
    victim = Hacker("Helpless Victim")
    extractor.acquire_rig()
    victim.acquire_rig(Rig("Machine"))

    # breaking victim's rig and adding assets
    victim.rig.take_hits()
    victim.rig.take_hits()
    victim.rig.storage.append(Asset("CryptoToken", "A digital currency that acquires or repairs rig"))
    victim.rig.storage.append(Asset("Data Spike", "Hacking tool used in battles"))

    print(f"test 3.1: Pre-extraction")
    print(f"- Victim's Rig State: Broken? {victim.rig.broken_state}")
    print(f"- Victim's Assets: {[a.name for a in victim.rig.storage]}")
    print(f"- Removable Drives: {sum(1 for a in extractor.rig.storage if a.name == "Removable Drive")}")
    
    # extracting test
    extract_res = extractor.extract_asset(victim.rig)
    print(f"\ntest 3.2: Extraction Result = {extract_res}")
    print(f"- Victim Assets after: {[a.name for a in victim.rig.storage]}")
    print(f"- Extractor Assets after: {[a.name for a in extractor.rig.storage]}")

    print("PHASE 3 COMPLETED: Extracting Assets System")

test_combat_trace_system()
test_asset_extraction()



