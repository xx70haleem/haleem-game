import sys
import random as r
import winsound
import time
import msvcrt
import subprocess
from pathlib import Path
import threading
import os
import colorama 
from colorama import Fore, Back, Style, init
init(autoreset=True)


wending_grace_unlocked = False

def resource_path(file_name):

    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / file_name
#menu
def main_menu():
    while True:
        print_menu("     ELDEN RING RIP OFF WITH HALEEM LORE GAME         ")
        print_menu("     1- Start game")
        print_menu("     2- instructions")
        print_menu("     3- exit")
        print_menu("     Made by: author of haleem lore Mohammad Alsuwailan ")
        menu_choice = input(">>>")


        if menu_choice == "1":
            return

        elif menu_choice == "2":

            print_menu("\n========== HOW TO PLAY ==========")

            print("\n- Choose between Samurai, Vagabond, or Mage.")
            print("- Every class has different stats, weapons, armor, and special moves.")

            print("\n========== STATS ==========")

            print("- STR increases your physical damage.")
            print("- DEX increases your critical hit chance.")
            print("- VIG increases your maximum HP.")
            print("- MIND increases your maximum FP.")
            print("- DEFENCE reduces damage taken from enemy attacks.")

            print("\n========== COMBAT ==========")

            print("- Attack enemies using normal attacks or special moves.")
            print("- Special moves are stronger but consume FP.")
            print("- Healing uses flasks. You only have a limited amount.")
           

            print("\n========== DODGING ==========")

            print("- When DODGE appears, react before the timer runs out.")
            print("- 1 = UP")
            print("- 2 = RIGHT")
            print("- 3 = DOWN")
            print("- 4 = LEFT")
            print("- Choose a safe direction or you will get hit.")

            print("\n========== LOOT ==========")

            print("- Defeating bosses rewards weapons, armor, and runes.")
            print("- Loot has different rarities.")
            print("- Better weapons increase damage.")
            print("- Better armor increases defence.")
            print("- Some bosses may even drop bonus loot.")
            print("- Equip new gear through your inventory.")

            print("\n========== REST POINTS ==========")

            print("- Between boss fights you will reach rest points.")
            print("- Spend runes to level up your stats.")
            print("- Check your character and prepare before continuing.")
            print("- Random events may occur during your journey.")

            print("\n========== THE RUN ==========")

            print("- Bosses become stronger as you progress.")
            print("- Build your character using loot and level-ups.")
            print("- Your equipment and choices determine how strong you become.")
            print("- Survive every boss and reach the final battle against HALEEM.")

            print("\n- Press ESC during cutscenes to skip them.")
            print("- If you die... skill issue.")

            print()
            print()
            print()
            print()
            print()

        elif menu_choice == "3":
            sys.exit()
    

def print_boss(text):
    print(Fore.RED + Style.BRIGHT + text)

def print_good(text):
    print(Fore.GREEN + text)

def print_magic(text):
    print(Fore.CYAN + text)

def print_reward(text):
    print(Fore.YELLOW + Style.BRIGHT + text)

def print_menu(text):
    print(Fore.LIGHTBLUE_EX + Style.DIM + text)  
def print_class(text):
    print(Fore.LIGHTBLUE_EX + Style.DIM + text)

def print_black(text):
    print(Fore.LIGHTBLACK_EX + Style.BRIGHT + text)  

def print_darkyellow(text):
    print(Fore.LIGHTYELLOW_EX + Style.DIM + text) 




def rarity_color(rarity):
    colors = {
        "common": Fore.LIGHTBLACK_EX,
        
        "rare": Fore.BLUE,
        
        "legendary": Fore.YELLOW + Style.BRIGHT
    }

    return colors.get(rarity.lower(), Fore.WHITE)

def print_loot(text, rarity):
    print(rarity_color(rarity) + str(text))










def choose_class():
    while True:
        print()
        print_class("Pick your class Tarnished " \
        "\n 1- samurai  " \
        "\n 2- vagabond " \
        "\n 3- mage")


        print()
        print_class("enter choice here:")
        picked_class = input()

        if picked_class == "1":
            class_name = "samurai"
            flasks = 5
            
            weapon = "uchikatana"
            armor = "reeds armor"
            weapon_dmg = 10
            defence = 15
            special1 = "Quickdraw Slash"
            special2 = "Blood Moon Slash"
            special3 = "Thousand Cuts"
            special1_fp = 20
            special2_fp = 30
            special3_fp = 40
            speical1_dmg = (25,35)
            speical2_dmg = (35,45)
            speical3_dmg = (50,70)
            specials = special1, special2, special3
            specials_fp = special1_fp, special2_fp, special3_fp
            specials_dmg = speical1_dmg, speical2_dmg, speical3_dmg
            class_lore = class_lore = """
            SAMURAI

            A swordsman from the eastern lands,
            trained from childhood to master discipline, patience,
            and the sacred art of pretending everything is under control.

            His clan was once feared across the region.

            Then Haleem visited.

            Nobody knows why.

            By sunrise, half the dojo was gone,
            three masters had retired,
            and Haleem had somehow been promoted to honorary sensei.

            The Samurai refused to accept this humiliation.

            He sharpened his blade, left his homeland,
            and swore to restore his clan's honor.

            Mostly by beating Haleem's ass.
            """
    
            print_class("great another samurai wow...")
            time.sleep(3)
            print()
            strength = 17
            dexterity = 28
            vigor = 23
            mind = 10
            main_stat = dexterity // 2
            print_magic("STATS:")
            print_magic(f"str: {strength}")
            print_magic(f"dex: {dexterity}")
            print_magic(f"vig: {vigor}")
            print_magic(f"mind: {mind}")
            print()
            print_darkyellow(f"starting set: \n" \
            f"weapon: {weapon} damage: {weapon_dmg} \n" \
            f"armor: {armor} defence: {defence}")
            break
        elif picked_class == "2":
            class_name = "vagabond"
            flasks = 5
            
            weapon = "claymore"
            armor = "knight armor"
            weapon_dmg = 15
            defence = 25
            special1 = "Shield Breaker"
            special2 = "Knee of Bad Intentions"
            special3 = "Lion's Claw"
            special1_fp = 20
            special2_fp = 30
            special3_fp = 40
            speical1_dmg = (25,35)
            speical2_dmg = (35,45)
            speical3_dmg = (50,70)
            specials = special1, special2, special3
            specials_fp = special1_fp, special2_fp, special3_fp
            specials_dmg = speical1_dmg, speical2_dmg, speical3_dmg
            class_lore = """
                VAGABOND

                A disgraced warrior from a kingdom destroyed
                after its king challenged Haleem to an arm wrestle.

                Nobody knows exactly what happened.

                The castle is gone.
                The king is missing.
                Haleem claims it was "light work."

                The Vagabond survived only because he was outside
                buying bread when the kingdom fell.

                Now armed with a worn blade, questionable armor,
                and unresolved anger, he wanders the land searching
                for Haleem.

                Not for revenge.

                He just really wants to know what happened to the bread.
                """
            print_class("ah a tank build bro thinks he's raider")
            time.sleep(3)
            print()
            strength = 28
            dexterity = 11
            vigor = 30
            mind = 8
            main_stat = strength // 2
            print_magic("STATS:")
            print_magic(f"str: {strength}")
            print_magic(f"dex: {dexterity}")
            print_magic(f"vig: {vigor}")
            print_magic(f"mind: {mind}")
            print()
            print_darkyellow(f"starting set: \n" \
            f"weapon: {weapon} damage: {weapon_dmg}  \n" \
            f"armor: {armor} defence: {defence} ")
            break
        elif picked_class == "3":
            class_name = "mage"
            flasks = 5
            
            weapon = "staff of nature"
            armor = "cloak of dirt"
            weapon_dmg = 3
            defence = 10
            special1 = "Glintstone Bolt"
            special2 = "Comet"
            special3 = "Meteor Shower"
            special1_fp = 20
            special2_fp = 30
            special3_fp = 40
            speical1_dmg = (25,35)
            speical2_dmg = (35,45)
            speical3_dmg = (50,70)
            specials = special1, special2, special3
            specials_fp = special1_fp, special2_fp, special3_fp
            specials_dmg = speical1_dmg, speical2_dmg, speical3_dmg
            class_lore =  class_lore = """
            MAGE

            Once a respected scholar of forbidden magic,
            the Mage dedicated his life to discovering
            the greatest power in existence.

            After years of research, he found an ancient tablet.

            It contained only four words:

            "HALEEM WAS HERE FIRST."

            He laughed.

            Then the tablet laughed back.

            Since that day, the Mage has studied every spell,
            curse, forbidden ritual, and illegal PDF he can find
            in preparation for the inevitable battle.

            He believes magic can defeat Haleem.

            Nobody has had the heart to tell him otherwise.
            """
            
            print_class("ah youre a wizard harry")
            time.sleep(3)
            print()
            strength = 9
            dexterity = 13
            vigor = 13
            mind = 40
            main_stat = mind // 2
            print_magic("STATS:")
            print_magic(f"str: {strength}")
            print_magic(f"dex: {dexterity}")
            print_magic(f"vig: {vigor}")
            print_magic(f"mind: {mind}")
            print()
            print_darkyellow(f"starting set: \n" \
            f"weapon: {weapon} damage: {weapon_dmg}  \n" \
            f"armor: {armor} defence: {defence} ")
            break
    
    
        else:
            print("Pick and actual class bro dont write random shit i didnt code")
            continue

    return(class_name, weapon, armor, weapon_dmg, defence, strength, dexterity, vigor, mind, class_lore, specials_dmg, specials_fp, specials, main_stat, flasks)




def character_menu(
    class_name,
    class_lore,
    specials,
    special_fp,
    special_damage,
    weapon,
    weapon_dmg,
    armor,
    defence,
    strength,
    dexterity,
    vigor,
    mind,
    flasks
):

    while True:

        print_class("\n===== CHARACTER MENU =====")
        print_class("1- Continue")
        print_class("2- Character Lore")
        print_class("3- Special Moves")
        print_class("4- Inventory")
        print_class("5- Stats")

        choice = input(">>> ")

        if choice == "1":
            return weapon, weapon_dmg, armor, defence

        elif choice == "2":
            print_class(f"\n{class_name.upper()} LORE")
            print_class(class_lore)

        elif choice == "3":
            print("\nSPECIAL MOVES")

            print_magic(
                f"1- {specials[0]} | "
                f"FP: {special_fp[0]} | "
                f"Damage: {special_damage[0][0]}-{special_damage[0][1]}"
            )

            print_magic(
                f"2- {specials[1]} | "
                f"FP: {special_fp[1]} | "
                f"Damage: {special_damage[1][0]}-{special_damage[1][1]}"
            )

            print_magic(
                f"3- {specials[2]} | "
                f"FP: {special_fp[2]} | "
                f"Damage: {special_damage[2][0]}-{special_damage[2][1]}"
            )

        elif choice == "4":
            weapon, weapon_dmg, armor, defence = inventory_menu(
            inventory,
            weapon,
            weapon_dmg,
            armor,
            defence
            )

        elif choice == "5":
            print_magic("\nSTATS")
            print_magic("STR:", strength)
            print_magic("DEX:", dexterity)
            print_magic("VIG:", vigor)
            print_magic("MIND:", mind)

        else:
            print("did not code that just stick to the instructons bruh")
            continue







#attacks
def attack(weapon_dmg, strenght):
    damage = r.randint(10,20)
    damage += weapon_dmg
    damage += strenght // 3
    return(damage)

def specials_function(specials, specials_fp, specials_dmg, fp, weapon_dmg, main_stat):

    print_magic("\n SPECIAL MOVES")
    print_magic(f"1 - {specials[0]} | fp = {specials_fp[0]} | dmg = {specials_dmg[0]}")
    print_magic(f"2 - {specials[1]} | fp = {specials_fp[1]} | dmg = {specials_dmg[1]}")
    print_magic(f"3 - {specials[2]} | fp = {specials_fp[2]} | dmg = {specials_dmg[2]}")
    print_magic("4- exit menu")
    special_choice = input(">>>")
    if special_choice == "1":
        special_index = 0

    elif special_choice == "2":
        special_index = 1

    elif special_choice == "3":
        special_index = 2

    elif special_choice == "4":
        return None, fp, "back"

    else:
        print("I DIDNT CODE THAT DUMBASS")
        return None, fp, "back"

    fp_cost = specials_fp[special_index]
    if fp < fp_cost:
        return None, fp, None
    fp -= fp_cost
    


    min_dmg = specials_dmg[special_index][0]
    max_dmg = specials_dmg[special_index][1]
    damage = r.randint(min_dmg,max_dmg)
    damage += weapon_dmg
    damage += main_stat
    return(damage, fp, specials[special_index])

#dodge
directions = {
    "1": "up",
    "2": "right",
    "3": "down",
    "4": "left"
}


def dodge_attack(hit_zones, time_limit=2.2):

    print_reward("\nDODGE!")
    print_reward("1 = UP")
    print_reward("2 = RIGHT")
    print_reward("3 = DOWN")
    print_reward("4 = LEFT")
    print()
    print()

    start_time = time.monotonic()

    while time.monotonic() - start_time < time_limit:

        if msvcrt.kbhit():

            key = msvcrt.getwch()

            if key in directions:

                chosen_direction = directions[key]

                if chosen_direction in hit_zones:
                    print_boss("YOU GOT HIT!")
                    return False

                else:
                    
                    return True

    print_boss("TOO SLOW!")
    return False

#crit
def crit(dexterity):
    crit_chance = 20 + (dexterity * 0.2)

    if crit_chance > 47:
        crit_chance = 47

    crit_roll = r.uniform(0, 100)

    if crit_roll <= crit_chance:
        return True
    else:
        return False

#boss pools
tier1_bosses = {
    "boss1":{
        "name":"BIG FOOT OF THE FART GUARD",
        "hp": 200, 
        "loot_bonus": 0,
        "runes": 2000,
        "attacks": {"FART OF THE BIGGEST":{
                    "damage": [15,25],
                    "hit_zones": ["left","right","up"]},
                     "GUARD FORM OF THE FART DIVINITY":{
                    "damage": [25,30],
                    "hit_zones": ["up"]},
                    
                      "FART CANNON OF DOOM AND FEET":{
                      "damage": [30,40],
                      "hit_zones": ["left","right","up"]}
                    }

        },

    

    "boss2":{
        "name":"MR.BOBIN JERKMATE CHAMPION",
        "hp": 240,
        "loot_bonus": 5,
        "runes": 2500,
        "attacks": {"SCREAM OF THE CHAMPION":{
                    "damage": [20,25],
                    "hit_zones": ["left","right","up"]},
                     "JERK OFF OF LEGENDS":{
                         "damage":[30,35],
                         "hit_zones": ["left","right"]},
                      "CUMSHOT OF VICTORY":{
                          "damage":[40,50],
                          "hit_zones": ["down","up"]},
                      }

    },

    "boss3":{
        "name": "sun deep graceful blade of kfc",
        "hp": 270,
        "loot_bonus" : 10,
        "runes": 3000,
        "attacks" :{ "graceful slash":{
            "damage" : [30,35],
            "hit_zones": ["left","right"]},
         "thurst of a thousand spicy fries":{
            "damage":[35,40],
            "hit_zones": ["down","up"]},
            "oilfoul dance":{
                "damage":[50,70],
                "hit_zones": ["left","up","right"]},
            }
    }
}

tier3_bosses = {
    "boss1":{
        "name":"DRAGON YOUSEF",
        "hp": 750, 
        "loot_bonus": 25,
        "runes": 8000,
        "attacks": {"BREATH OF DOOM AND DISGUST":{
                    "damage": [110,120],
                    "hit_zones": ["left","right","up"]},
                     "CLAW OF 5NZERA":{
                    "damage": [120,130],
                    "hit_zones": ["left","right"]},
                    
                      "BELLY FLOP OF TIREDNESS AND DESPAIR":{
                      "damage": [140,150],
                      "hit_zones": ["left","right","up"]}
                    }

        },

    

    "boss2":{
        "name":"DRAGON QUEEN MESHAAL",
        "hp": 900,
        "loot_bonus": 30,
        "runes": 9000,
        "attacks": {"BREATH OF PURFUME":{
                    "damage": [120,130],
                    "hit_zones": ["left","right","up"]},
                     "FINGER OF DISCIPLINE":{
                         "damage":[130,140],
                         "hit_zones": ["up","down"]},
                      "THEFT OF ALL FOOD":{
                          "damage":[140,150],
                          "hit_zones": ["right","up","left"]},
                      }

    },

    "boss3":{
        "name": "WORLD EATER MUBARAK",
        "hp": 1000,
        "loot_bonus" : 35,
        "runes": 10000,
        "attacks" :{ "EATS OF DOOM AND ENDING":{
            "damage" : [130,140],
            "hit_zones": ["left","right","up"]},
         "BREATH OF THE WORLD EATER":{
            "damage":[140,150],
            "hit_zones": ["down","up"]},
            "WORLD EATER":{
                "damage":[150,160],
                "hit_zones": ["left","up","right"]},
            }
    }
}
tier2_bosses = {
    "boss1":{
        "name":"HABEEB OF THE LIGHT",
        "hp": 450, 
        "loot_bonus": 5,
        "runes": 4000,
        "attacks": {"LIGHT OF THE BLESSED ONE":{
                    "damage": [30,40],
                    "hit_zones": ["left","right","up"]},
                     "GRAB OF THE IMMOVABLE":{
                    "damage": [50,60],
                    "hit_zones": ["up"]},
                    
                      "CHILDREN OF HABEEB":{
                      "damage": [60,70],
                      "hit_zones": ["left","right","up"]}
                    }

        },

    

    "boss2":{
        "name":"EVIL HABEEB OF THE DARK",
        "hp": 550,
        "loot_bonus": 15,
        "runes": 4500,
        "attacks": {"SHADOW OF THE DARK":{
                    "damage": [50,60],
                    "hit_zones": ["left","right","up"]},
                     "MIND PENETRATION":{
                         "damage":[60,70],
                         "hit_zones": ["up","down"]},
                      "DARK CHILDREN OF EVIL HABEEB":{
                          "damage":[80,90],
                          "hit_zones": ["right","up","left"]},
                      }

    },

    "boss3":{
        "name": "mysterious thirteen",
        "hp": 650,
        "loot_bonus" : 20,
        "runes": 5500,
        "attacks" :{ "thousand hand grab of torture":{
            "damage" : [70,80],
            "hit_zones": ["left","right","up"]},
         "thousand hand pull into the abyss":{
            "damage":[80,90],
            "hit_zones": ["down","up"]},
            "gangbang":{
                "damage":[90,100],
                "hit_zones": ["left","up","right"]},
            }
    }
}


#boss_picker
def choose_boss(boss_pool):
    boss = r.choice(list(boss_pool.values()))
    return boss

current_boss = choose_boss(tier1_bosses)
boss_name = current_boss["name"]
boss_hp = current_boss["hp"]
boss_attacks = current_boss["attacks"]
loot_bonus = current_boss["loot_bonus"]


#loot
tier1_loot = {"commonwpn": {"Rusted Longsword" : 17,
"Bent Spear": 18,
"Cracked Battle Axe": 19,
"Worn Uchigatana": 18,
"Iron Mace": 20,
"Old Claymore": 21,
"Chipped Twinblade": 19,
"Soldier's Halberd": 21,
"Tarnished Dagger": 17,
"Broken Greatsword": 22},

"rarewpn" : {"Fart Guard's Greatclub": 25,
"Cannon of the Fart Guard": 27,
"Bobin's Champion Blade": 26,
"Jerkmate Cleaver": 28,
"Spicy Fry Katana": 27,
"Oilfoul Twinblade": 29},

"legendarywpn" : {"Blade of Fart Divinity": 34,
"Sun Deep's Graceful Blade": 37},

"commonarmor": {"Worn Soldier Armor": 20,
"Old Samurai Armor": 21,
"Rusty Chainmail Armor": 22,
"Leather Battle Armor": 20,
"Faded Guard Armor": 23,
"Cracked Knight Armor": 25,
"Abandoned Mercenary Armor": 24,
"Damaged Royal Armor": 26,
"Heavy Iron Armor": 28,
"Traveler's Armor": 21,},


"rarearmor" : {"Fart Guard Armor": 30,
"Divine Fart Guard Armor": 32,
"Bobin Champion Armor": 31,
"Jerkmate Victory Armor": 33,
"Spicy Fry Armor": 32,
"Oilfoul Dancer Armor": 34,},

"legendaryarmor" : {"Sun Deep's Graceful Armor": 42},

 }

tier2_loot = {"commonwpn": {"Reinforced Longsword": 30,
"Steel War Axe": 31,
"Knight's Spear": 32,
"Black Iron Katana": 31,
"Heavy War Mace": 33,
"Tempered Claymore": 34,
"Mercenary Twinblade": 32,
"Royal Halberd": 35,
"Assassin's Dagger": 30,
"Executioner's Greatsword": 36,
"Warrior's Scimitar": 33,
"Reinforced Great Hammer": 35},

"rarewpn" : {"Blade of the Blessed Light": 39,
"Habeeb's Holy Spear": 41,
"Dark Habeeb's Shadow Blade": 42,
"Mind Penetrator": 43,
"Thirteen's Torture Scythe": 44,
"Abyssal Hand Blade": 45,
"Children of Light Greatsword": 41,
"Dark Children Twinblade": 43},

"legendarywpn" : {"Habeeb's Divine Light": 54,
"Blade of Eternal Darkness": 58,
"Thirteen Hands of the Abyss": 62},

"commonarmor": {"Reinforced Soldier Armor": 35,
"Black Iron Armor": 36,
"Knight Commander Armor": 37,
"Tempered Samurai Armor": 36,
"Heavy Mercenary Armor": 38,
"Royal Guard Armor": 39,
"Steel Battle Armor": 37,
"Executioner's Armor": 40,
"Abyss Traveler Armor": 38,
"Fortified Chain Armor": 39,
"Veteran Warrior Armor": 40,
"Heavy Greatplate Armor": 41},


"rarearmor" : {"Habeeb's Blessed Armor": 45,
"Armor of the Holy Light": 47,
"Evil Habeeb's Shadow Armor": 48,
"Armor of Mind Penetration": 49,
"Thirteen's Torture Armor": 50,
"Abyssal Hand Armor": 51,
"Children of Light Armor": 47,
"Dark Children Armor": 49},

"legendaryarmor" : {"Habeeb's Divine Armor": 59,
"Armor of Eternal Darkness": 63},

 }


tier3_loot = {"commonwpn": {"Dragonsteel Longsword": 46,
"Obsidian War Axe": 47,
"Ancient Dragon Spear": 48,
"Crimson Katana": 47,
"Colossal Iron Mace": 49,
"Dragonbone Claymore": 50,
"Royal Twinblade": 48,
"Blacksteel Halberd": 51,
"Worldborn Dagger": 46,
"Colossal Greatsword": 52,
"Dragon Hunter Scimitar": 49,
"Ancient Great Hammer": 53,
"Burning Warblade": 51,
"Worldbreaker Axe": 54},

"rarewpn" : {"Yousef's Dragonfang Blade": 58,
"Breath of Doom Greatsword": 60,
"Claw of 5NZERA": 61,
"Meshaal's Perfumed Katana": 62,
"Finger of Discipline Spear": 63,
"Queen's Royal Dragonblade": 64,
"Mubarak's World Eater Axe": 65,
"Breath of the World Eater": 66,
"Dragon Belly Crusher": 67,
"Maw of the World Eater": 68},

"legendarywpn" : {"Yousef's Doomfang": 78,
"Meshaal's Blade of Discipline": 82,
"Mubarak's World Devourer": 87,
"End of All Worlds": 92},

"commonarmor": {"Dragonsteel Armor": 52,
"Obsidian Knight Armor": 53,
"Ancient Dragon Armor": 54,
"Crimson Samurai Armor": 53,
"Colossal Iron Armor": 55,
"Dragonbone Armor": 56,
"Royal Dragon Guard Armor": 54,
"Blacksteel Armor": 57,
"Worldborn Armor": 52,
"Colossal Greatplate Armor": 58,
"Dragon Hunter Armor": 55,
"Ancient War Armor": 59,
"Burning Battle Armor": 57,
"Worldbreaker Armor": 60},


"rarearmor" : {"Yousef's Dragon Armor": 65,
"Armor of Doom and Disgust": 67,
"5NZERA Dragonplate Armor": 68,
"Meshaal's Royal Dragon Armor": 69,
"Armor of Discipline": 70,
"Perfumed Dragon Queen Armor": 71,
"Mubarak's World Eater Armor": 72,
"Armor of the World Eater's Breath": 73,
"Dragon Belly Armor": 74,
"Maw of the World Eater Armor": 75},

"legendaryarmor" : {"Yousef's Doom Dragon Armor": 86,
"Meshaal's Armor of Discipline": 91,
"Armor of the End of All Worlds": 102},

 }


#loot roll
def loot_roll(loot_pool, loot_bonus, forced_type=None):


    roll = r.randint(1, 100)

    legendary_chance = 5 + loot_bonus // 5
    rare_chance = 20 + loot_bonus // 2

    if roll <= legendary_chance:
        rarity = "legendary"

    elif roll <= rare_chance:
        rarity = "rare"

    else:
        rarity = "common"

    if forced_type == None:
        loot_type = r.choice(["wpn", "armor"])
    else:
        loot_type = forced_type

    



    category = rarity + loot_type

    item_name = r.choice(list(loot_pool[category].keys()))
    item_stat = loot_pool[category][item_name]

    return item_name, item_stat, loot_type, rarity


#level up menu
def level_up(
    runes,
    strength,
    dexterity,
    vigor,
    mind,
    max_hp,
    player_hp,
    max_fp,
    fp,
    class_name
):

    upgrade_cost = 750

    while True:

        print_magic("\n===== LEVEL UP =====")
        print_magic(f"Runes: {runes}")
        print_magic(f"Each upgrade costs {upgrade_cost} runes")
        print()
        print_magic(f"1- STR: {strength}")
        print_magic(f"2- DEX: {dexterity}")
        print_magic(f"3- VIG: {vigor}")
        print_magic(f"4- MIND: {mind}")
        print_magic("5- Back")

        choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + ">>> ")

        if choice == "5":
            break
    

        if runes < upgrade_cost:
            print_boss("Not enough runes!")
            continue

        if choice == "1":


            if strength >= 100:
                print_boss("STR is already maxed!")
                continue







            runes -= upgrade_cost
            strength = min(100, strength + 5)
            print_good(f"STR increased to {strength}!")

        elif choice == "2":



            if dexterity >= 100:
                print_boss("DEX is already maxed!")
                continue






            runes -= upgrade_cost
            dexterity = min(100, dexterity + 5)
            print_good(f"DEX increased to {dexterity}!")

        elif choice == "3":


            if vigor >= 100:
                print_boss("VIG is already maxed!")
                continue





            runes -= upgrade_cost
            vigor = min(100, vigor + 5)

            old_max_hp = max_hp
            max_hp = 100 + vigor // 1.1

            hp_gained = max_hp - old_max_hp
            player_hp += hp_gained

            print_good(f"VIG increased to {vigor}!")
            print_good(f"Max HP increased to {max_hp}!")

        elif choice == "4":


            if mind >= 100:
                print_boss("MIND is already maxed!")
                continue






            runes -= upgrade_cost
            mind = min(100, mind + 5)

            old_max_fp = max_fp
            max_fp = 80 + mind

            fp_gained = max_fp - old_max_fp
            fp += fp_gained

            print_good(f"MIND increased to {mind}!")
            print_good(f"Max FP increased to {max_fp}!")

        else:
            print("pick an actual option bro")
            continue

    if class_name == "samurai":
        main_stat = dexterity // 2

    elif class_name == "vagabond":
        main_stat = strength // 2

    else:
        main_stat = mind // 2

    return (
    runes,
    strength,
    dexterity,
    vigor,
    mind,
    max_hp,
    player_hp,
    max_fp,
    fp,
    main_stat
    )



import subprocess

def play_cutscene(file_name):
    try:
        video_path = resource_path(file_name)
        player_path = resource_path("assets/tools/ffplay.exe")

        if not video_path.exists():
            print(f"Cutscene not found: {file_name}")
            return

        if not player_path.exists():
            print("ffplay.exe not found.")
            return

        subprocess.run([
            str(player_path),
            "-autoexit",
            "-fs",
            "-loglevel", "quiet",
            str(video_path)
        ])

    except Exception as e:
        print(f"Cutscene failed: {e}")


def play_music(file_name):

    winsound.PlaySound(None, 0)

    music = resource_path(f"assets/sound/{file_name}")

    winsound.PlaySound(
        str(music),
        winsound.SND_FILENAME |
        winsound.SND_ASYNC |
        winsound.SND_LOOP
    )


def stop_music():
    winsound.PlaySound(None, 0)







def delayed_rest_music(stop_event):

    if not stop_event.wait(4):
        play_music("breaksound.wav")





def take_damage(player_hp, damage, grace_available):

    if player_hp - damage <= 0 and grace_available:
        print()
        print(Fore.YELLOW + Style.BRIGHT + "WENDING GRACE ACTIVATES")
        print(Fore.YELLOW + "Death refuses to claim you.")

        player_hp = 1
        grace_available = False

    else:
        player_hp -= damage

    return player_hp, grace_available










#haleem attack
def boss_attack(phase_two):
    if phase_two == False:
         attack_choice = r.randint(1, 7)

         if attack_choice <= 2:
          damage = r.randint(100, 110)
          hit_zones = ["left", "right"]
          print_boss("G.H.ISHAK uses BACKHAND OF DISRESPECT")
          print()
          print()
          print_boss("habibi what is this talk very gingal ina now")
          print()
          time.sleep(2)

         elif attack_choice <= 5:
              damage = r.randint(120, 130)
              hit_zones = ["up", "down"]
              print_boss("G.H.ISHAK uses BLANK STARE")
              print()
              print()
              print_boss(".......")
              print()
              time.sleep(2)
         elif attack_choice > 6:
             damage = r.randint(140,160)
             hit_zones = ["down"]
             print_boss("G.H.ISHAK uses SWEATY ARMPIT LIFT")
             print()
             print()
             print_boss("*yawns*")
             print()
             time.sleep(2)
    
    

         else:
          damage = r.randint(150,170 )
          hit_zones = ["up", "right"]
          print_boss("G.H.ISHAK uses WRATH OF THE ONE BELOW ALL")
          print()
          print()
          print_boss("*scratches belly button*")
          print()
          time.sleep(2)
    else:
         second_attack_choice = r.randint(1,5)

         if second_attack_choice <= 2:
          damage = r.randint(130,140)
          hit_zones = ["left", "right"]
          print_boss("Evolved Haleem uses FART AND POOP")
          print()
          print()
          
         elif second_attack_choice < 4:
          damage = r.randint(150,160)
          hit_zones = ["up", "down"]
          print_boss("Evolved Haleem uses SWEAT CANNON OF DOOM AND DESPAIR")
          print()
          print()
         else:
          damage = r.randint(200,250)
          hit_zones = ["down"]
          print_boss("Evolved Haleem uses WORLD ENDER MUBARAK")
          print()
          print()

  

    return damage, hit_zones



#break screen
def break_screen(
    class_name,
    class_lore,
    specials,
    specials_fp,
    specials_dmg,
    weapon,
    weapon_dmg,
    armor,
    defence,
    strength,
    dexterity,
    vigor,
    mind,
    flasks,
    runes,
    max_hp,
    player_hp,
    max_fp,
    fp,
    main_stat
):
    rest_music_stop = threading.Event()

    threading.Thread(
    target=delayed_rest_music,
    args=(rest_music_stop,),
    daemon=True
    ).start()
   
    
    event_roll = r.randint(1, 100)

    if event_roll <= 5:
        iron_tormenter_event(inventory)

    elif event_roll <= 10 and not wending_grace_unlocked:
        jose_event()

    #rest
    player_hp = max_hp
    fp = max_fp
    flasks = 5

    while True:

        print_class("\n========================")
        print_class("       REST POINT")
        print_class("========================")
        print_class(f"Runes: {runes}")
        print()
        print_class("1- Level Up")
        print_class("2- Character Menu")
        print_class("3- Continue Journey")

        choice = input(">>> ")
        
       

        if choice == "1":
            print_class("\nLEVEL UP")
            
            (
            runes,
            strength,
            dexterity,
            vigor,
            mind,
            max_hp,
            player_hp,
            max_fp,
            fp,
            main_stat
            ) = level_up(
                runes,
                strength,
                dexterity,
                vigor,
                mind,
                max_hp,
                player_hp,
                max_fp,
                fp,
                class_name
            )

            

        elif choice == "2":
           weapon, weapon_dmg, armor, defence = character_menu(
        class_name,
        class_lore,
        specials,
        specials_fp,
        specials_dmg,
        weapon,
        weapon_dmg,
        armor,
        defence,
        strength,
        dexterity,
        vigor,
        mind,
        flasks
    )

        elif choice == "3":

            rest_music_stop.set()
            stop_music()
            print_black("\nYou leave the rest point...")
            time.sleep(2.2)

            return (
                    runes,
                    strength,
                    dexterity,
                    vigor,
                    mind,
                    max_hp,
                    player_hp,
                    max_fp,
                    fp,
                    main_stat,
                    weapon,
                    weapon_dmg,
                    armor,
                    defence,
                    flasks
                )

        else:
            print("pick an actual option bro")


#inventory


def inventory_menu(inventory, weapon, weapon_dmg, armor, defence):

    while True:
        print_darkyellow("\n===== INVENTORY =====")
        print_darkyellow(f"Equipped Weapon: {weapon} | Damage: {weapon_dmg}")
        print_darkyellow(f"Equipped Armor: {armor} | Defence: {defence}")
        print()
        print_darkyellow("1- Weapons")
        print_darkyellow("2- Armor")
        print_darkyellow("3- Back")

        choice = input(">>> ")

        if choice == "1":

            weapons = list(inventory["weapons"].items())

            print_darkyellow("\n===== WEAPONS =====")

            for number, item in enumerate(weapons, 1):
                name = item[0]
                damage = item[1]

                if name == weapon:
                    print_darkyellow(f"{number}- {name} | Damage: {damage} | EQUIPPED")
                else:
                    print_darkyellow(f"{number}- {name} | Damage: {damage}")

            equip_choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\nChoose weapon number or type back: ")

            if equip_choice.lower() == "back":
                continue

            if equip_choice.isdigit():
                equip_choice = int(equip_choice)

                if 1 <= equip_choice <= len(weapons):
                    weapon = weapons[equip_choice - 1][0]
                    weapon_dmg = weapons[equip_choice - 1][1]

                    print_darkyellow(f"\nEquipped {weapon}!")

        elif choice == "2":

            armors = list(inventory["armor"].items())

            print_darkyellow("\n===== ARMOR =====")

            for number, item in enumerate(armors, 1):
                name = item[0]
                armor_defence = item[1]

                if name == armor:
                    print_darkyellow(f"{number}- {name} | Defence: {armor_defence} | EQUIPPED")
                else:
                    print_darkyellow(f"{number}- {name} | Defence: {armor_defence}")

            equip_choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\nChoose armor number or type back: ")

            if equip_choice.lower() == "back":
                continue

            if equip_choice.isdigit():
                equip_choice = int(equip_choice)

                if 1 <= equip_choice <= len(armors):
                    armor = armors[equip_choice - 1][0]
                    defence = armors[equip_choice - 1][1]

                    print_darkyellow(f"\nEquipped {armor}!")

        elif choice == "3":
            return weapon, weapon_dmg, armor, defence

        else:
            print("fuck you")


#mosab event
def iron_tormenter_event(inventory):

    print_reward("\n===== SOMEONE APPROACHES =====")
    time.sleep(2)

    print_reward("\nIRON TORMENTER: DID YOU PRAY TODAY?")
    time.sleep(1)

    print_reward("IRON TORMENTER: DID YOU PRAY TODAY?")
    time.sleep(1)

    print_reward("IRON TORMENTER: DID YOU PRAY TODAY?")
    time.sleep(1)

    print_boss("\nIRON TORMENTER IS ABOUT TO RUN!")
    print_reward("PRESS 1 TO KILL HIM!")
    time.sleep(1)

    # clear any old keyboard presses
    while msvcrt.kbhit():
        msvcrt.getwch()

    start_time = time.monotonic()

    while time.monotonic() - start_time < 1:

        if msvcrt.kbhit():

            key = msvcrt.getwch()

            if key == "1":

                print_good("\nYOU KILLED IRON TORMENTER!")
                print_reward("LEGENDARY LOOT!")
                print_reward("Iron Tormenter's Bow")
                print_magic("Damage: 150")

                inventory["weapons"]["Iron Tormenter's Bow"] = 150

                return

    print_boss("\nTOO SLOW!")
    print_boss("Iron Tormenter ran away...")

#jose event
def jose_event():
    global wending_grace_unlocked

    if wending_grace_unlocked:
        return

    print()
    print_black( "A strange man blocks your path...")
    time.sleep(2)

    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\nBALANCER JOSE:")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"You have defeated warriors, monsters, and creatures beyond comprehension."')
    time.sleep(2)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"But none of that matters."')
    time.sleep(2)

    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"There is only one true measure of strength."')
    time.sleep(3)

    print_boss('"Chess."')
    time.sleep(2)

    print_black("\nJose places a chessboard before you.")
    time.sleep(2)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"BALANCER JOSE: Where is the mate in this position?"')

    chess_image = resource_path("assets/image/jose_chess.png")

    try:
        os.startfile(str(chess_image))
    except Exception:
        print("Could not open the chess position.")

    answer = input(Fore.LIGHTBLACK_EX + Style.BRIGHT +"\nYour answer: ").strip().lower()

    correct_answer = "and in this postion he resigns"

    if answer == correct_answer:
        print()
        print_black( "Jose stares at you silently.")
        time.sleep(1.5)

        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"True"')
        time.sleep(1)

        print_reward("\nYOU HAVE RECEIVED:")
        print_reward("WENDING GRACE")
        time.sleep(2)

        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n BALANCER JOSE: Death itself will reject you once during every boss battle.")
        time.sleep(2)

        wending_grace_unlocked = True

    else:
        print()
        print_boss(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"BALANCER JOSE: Wrong."')
        time.sleep(2)

        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '"BALANCER JOSE: Haleem would have found mate in three seconds."')
        time.sleep(2)

        print_black("\nJose disappears without elaborating.")
        time.sleep(3)
        print()
        print()


#game start here




while True:
    play_music("main_menu.wav")
    main_menu()


    class_name, weapon, armor, weapon_dmg, defence, strength, dexterity, vigor, mind, class_lore, specials_dmg, specials_fp, specials, main_stat, flasks = choose_class()


    inventory = {
    "weapons": {
        weapon: weapon_dmg
    },
    "armor": {
        armor: defence
    }
}










    character_menu(
    class_name,
    class_lore,
    specials,
    specials_fp,
    specials_dmg,
    weapon,
    weapon_dmg,
    armor,
    defence,
    strength,
    dexterity,
    vigor,
    mind,
    flasks
)

    stop_music()
    #playerinfo
    player_hp = 100 + vigor // 1.1
    max_hp = player_hp
    flasks = 5
    max_fp = 80 + mind  
    fp = max_fp
    runes = 0

   

    
    # TIER 1 ENCOUNTER
    current_boss = choose_boss(tier1_bosses)

    boss_name = current_boss["name"]
    boss_hp = current_boss["hp"]
    boss_attacks = current_boss["attacks"]
    loot_bonus = current_boss["loot_bonus"]
    grace_available = wending_grace_unlocked
    

    print_black("\n You hear Something approach...")
    time.sleep(2)
    print_black("\n ...")
    time.sleep(1)
    print_black("\n ..")
    time.sleep(1)
    print_black("\n .")
    time.sleep(2)

    print()
    print_boss(f"{boss_name} HAS APPEARED!")
    play_music("bossmusic.wav")
    print()
    print()
    
    time.sleep(3)
    
    
    

    #combat boss 1
    while player_hp > 0 and boss_hp > 0:
    
                print_good(f"your HP {player_hp}/{max_hp}")
                print_magic(f"your FP: {fp}")
                print_boss(f"{boss_name} HP: {boss_hp}")
    
                choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\n1- attack\n2- special moves\n3- heal\n> ")
    
    
    
    
    
        #attack block
                if choice == "1":
                    damage = attack(weapon_dmg, strength)
                    if crit(dexterity):
                        damage *= 1.5
                        print()
                        print_good("CRITICAL HIT!")
                        print()
                
                    
    
                    boss_hp -= damage
                    print()
                    print_good(f"you dealt {damage} damage!")
                    print()
                    time.sleep(2.6)
    
                elif choice == "2":
                    damage, fp, move_used = specials_function(specials, specials_fp, specials_dmg, fp, weapon_dmg, main_stat)
                    if move_used == "back":
                        continue
    
    
    
    
    
    
                    if damage is None:
                        print_boss("not enough FP!")
                        print()
                        continue
    
                    boss_hp -= damage
                
                    print()
                    print_magic(f"You used {move_used}")
                    print_good(f"you dealt {damage} damage!")
                    print()
                    time.sleep(2.6)
        
            
    
                    
        #healing block
                elif choice == "3": 
                    if flasks > 0:
                        missing_hp = max_hp - player_hp
                        if missing_hp <= 0:
                            print_boss("your HP is already full!")
                            print()
                            continue
                        healing = r.randint(40,60)
    
                        if healing > missing_hp:
                            healing = missing_hp
                        player_hp += healing
                        flasks -= 1
    
                        print()
                        print_good(f"you healed {healing} HP")
                        print_good(f"your HP {player_hp}/{max_hp}")
                        print_good(f"remaining flasks: {flasks}")
                        print()
                        time.sleep(2.6)
                    else:
                        print()
                        print_boss("no flasks remaining!")
                        time.sleep(2.6)
                        
            
                    
                    
    
                else:
                    print("dude really did you missclick?")
                    time.sleep(2.6)
                    continue
                if boss_hp <= 0:
                    break
    

                attack_name = r.choice(list(boss_attacks.keys()))

                attack_data = boss_attacks[attack_name]

                damage_range = attack_data["damage"]
                hit_zones = attack_data["hit_zones"]

                damage = r.randint(damage_range[0], damage_range[1])
                damage = max(1, int(damage * (100 / (100 + defence * 2))))

                print(f"{boss_name} uses {attack_name}!")

                dodged = dodge_attack(hit_zones, 2.2)

                if dodged:
                    print_good("YOU DODGED!")
                    print()
                    time.sleep(2.6)

                else:
                    player_hp, grace_available = take_damage(
                                        player_hp,
                                        damage,
                                        grace_available
                                        )
                    print_boss(f"you took {damage} damage!")
                    print()
                    time.sleep(2.6)
            
    
                
    
    if boss_hp <= 0:
        winsound.PlaySound(None, 0)

        win_sound = resource_path("assets/sound/winsound.wav")

        winsound.PlaySound(
            str(win_sound),
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

        print_reward("\nENEMY FELLED")
        time.sleep(5)

        #loot and rune drop
        item_name, item_stat, loot_type, rarity = loot_roll(tier1_loot, loot_bonus)

        if loot_type == "wpn":
            inventory["weapons"][item_name] = item_stat
        else:
            inventory["armor"][item_name] = item_stat


        #print normal loot
        print_loot(f"\n{rarity.upper()} LOOT!", rarity)

        if loot_type == "wpn":
            print_loot(item_name, rarity)
            print_loot(f"Damage: {item_stat}", rarity)
        else:
            print_loot(item_name, rarity)
            print_loot(f"Damage: {item_stat}", rarity)


        #double drop
        double_drop = r.randint(1, 100)

        if double_drop <= 20:

            if loot_type == "wpn":
                second_type = "armor"
            else:
                second_type = "wpn"

            second_name, second_stat, second_type, second_rarity = loot_roll(
                tier1_loot,
                loot_bonus,
                second_type
            )

            print_loot(f"\n{second_rarity.upper()} BONUS LOOT!", second_rarity)

            if second_type == "wpn":
                inventory["weapons"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Damage: {second_stat}", second_rarity)

            else:
                inventory["armor"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Defence: {second_stat}", second_rarity)


        #runes
        rune_drop = current_boss["runes"]
        runes += rune_drop

        print_reward(f"\nYou gained {rune_drop} runes!")
        print_reward(f"Total runes: {runes}")
        time.sleep(5)


        #break
        
        (
        runes,
        strength,
        dexterity,
        vigor,
        mind,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat,
        weapon,
        weapon_dmg,
        armor,
        defence,
        flasks
        ) = break_screen(
        class_name,
        class_lore,
        specials,
        specials_fp,
        specials_dmg,
        weapon,
        weapon_dmg,
        armor,
        defence,
        strength,
        dexterity,
        vigor,
        mind,
        flasks,
        runes,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat
        )
        

    else:
        winsound.PlaySound(None, 0)

        winsound.PlaySound(None, 0)
        lose_sound = resource_path("assets/sound/defeatsound.wav")
        
        winsound.PlaySound(
                        str(lose_sound),
                        winsound.SND_FILENAME | winsound.SND_ASYNC
                    )

        print_boss("\nYOU DIED")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        time.sleep(8)
        continue

        #tier 2 encounter
    current_boss = choose_boss(tier2_bosses)

    boss_name = current_boss["name"]
    boss_hp = current_boss["hp"]
    boss_attacks = current_boss["attacks"]
    loot_bonus = current_boss["loot_bonus"]
    grace_available = wending_grace_unlocked

    print_black("\nYou continue deeper into the cursed lands...")
    time.sleep(2)

    print_black("\nYou hear something approaching...")
    time.sleep(2)

    print_boss(f"\n{boss_name} HAS APPEARED!")
    play_music("bossmusic2.wav")
    print()
    print()
    
    time.sleep(3)


    #combat boss 2
    while player_hp > 0 and boss_hp > 0:

        print_good(f"\nyour HP {player_hp}/{max_hp}")
        print_magic(f"your FP: {fp}/{max_fp}")
        print_boss(f"{boss_name} HP: {boss_hp}")

        choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\n1- attack\n2- special moves\n3- heal\n> ")


        #attack block
        if choice == "1":
            damage = attack(weapon_dmg, strength)

            if crit(dexterity):
                damage *= 1.5
                print()
                print_good("CRITICAL HIT!")
                print()

            boss_hp -= damage

            print()
            print_good(f"you dealt {damage} damage!")
            print()
            time.sleep(2.6)


        elif choice == "2":
            damage, fp, move_used = specials_function(
                specials,
                specials_fp,
                specials_dmg,
                fp,
                weapon_dmg,
                main_stat
            )

            if move_used == "back":
                continue

            if damage is None:
                print_boss("not enough FP!")
                print()
                continue

            boss_hp -= damage

            print()
            print_magic(f"You used {move_used}")
            print_good(f"you dealt {damage} damage!")
            print()
            time.sleep(2.6)


        #healing block
        elif choice == "3":
            if flasks > 0:
                missing_hp = max_hp - player_hp

                if missing_hp <= 0:
                    print_boss("your HP is already full!")
                    print()
                    continue

                healing = r.randint(40, 60)

                if healing > missing_hp:
                    healing = missing_hp

                player_hp += healing
                flasks -= 1

                print()
                print_good(f"you healed {healing} HP")
                print_good(f"your HP {player_hp}/{max_hp}")
                print_good(f"remaining flasks: {flasks}")
                print()
                time.sleep(2.6)

            else:
                print()
                print_boss("no flasks remaining!")
                print()
                time.sleep(2.6)
                continue


       


        else:
            print("dude really did you missclick?")
            time.sleep(2.6)
            continue


        if boss_hp <= 0:
            break


        #boss attack
        attack_name = r.choice(list(boss_attacks.keys()))

        attack_data = boss_attacks[attack_name]

        damage_range = attack_data["damage"]
        hit_zones = attack_data["hit_zones"]

        damage = r.randint(damage_range[0], damage_range[1])
        damage = max(1, int(damage * (100 / (100 + defence))))

        print(f"\n{boss_name} uses {attack_name}!")

        dodged = dodge_attack(hit_zones, 2.2)

        if dodged:
            print_good("YOU DODGED!")
            print()
            time.sleep(2.6)

        else:
            player_hp, grace_available = take_damage(
                                player_hp,
                                damage,
                                grace_available
                                )
            print_boss(f"you took {damage} damage!")
            print()
            time.sleep(2.6)


#win/lose
    if boss_hp <= 0:
        winsound.PlaySound(None, 0)

        win_sound = resource_path("assets/sound/winsound.wav")

        winsound.PlaySound(
            str(win_sound),
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )






        print_reward("\nLEGENDARY BEING FELLED")
        time.sleep(5)


                #loot and rune drop
        item_name, item_stat, loot_type, rarity = loot_roll(tier2_loot, loot_bonus)

        if loot_type == "wpn":
            inventory["weapons"][item_name] = item_stat
        else:
            inventory["armor"][item_name] = item_stat


        #print normal loot
        print_loot(f"\n{rarity.upper()} LOOT!", rarity)

        if loot_type == "wpn":
            print_loot(item_name, rarity)
            print_loot(f"Damage: {item_stat}", rarity)
        else:
            print_loot(item_name, rarity)
            print_loot(f"Defence: {item_stat}", rarity)


        #double drop
        double_drop = r.randint(1, 100)

        if double_drop <= 20:

            if loot_type == "wpn":
                second_type = "armor"
            else:
                second_type = "wpn"

            second_name, second_stat, second_type, second_rarity = loot_roll(
                tier2_loot,
                loot_bonus,
                second_type
            )

            print_loot(f"\n{second_rarity.upper()} BONUS LOOT!", second_rarity)

            if second_type == "wpn":
                inventory["weapons"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Damage: {second_stat}", second_rarity)

            else:
                inventory["armor"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Defence: {second_stat}", second_rarity)


        #runes
        rune_drop = current_boss["runes"]
        runes += rune_drop

        print_reward(f"\nYou gained {rune_drop} runes!")
        print_reward(f"Total runes: {runes}")
        time.sleep(5)


            #break
        (
        runes,
        strength,
        dexterity,
        vigor,
        mind,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat,
        weapon,
        weapon_dmg,
        armor,
        defence,
        flasks
        ) = break_screen(
        class_name,
        class_lore,
        specials,
        specials_fp,
        specials_dmg,
        weapon,
        weapon_dmg,
        armor,
        defence,
        strength,
        dexterity,
        vigor,
        mind,
        flasks,
        runes,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat
        )


    else:
        winsound.PlaySound(None, 0)

        winsound.PlaySound(None, 0)
        lose_sound = resource_path("assets/sound/defeatsound.wav")
        
        winsound.PlaySound(
                        str(lose_sound),
                        winsound.SND_FILENAME | winsound.SND_ASYNC
                    )

        print_boss("\nYOU DIED")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        time.sleep(8)
        continue


     #tier 3 encounter
    current_boss = choose_boss(tier3_bosses)

    boss_name = current_boss["name"]
    boss_hp = current_boss["hp"]
    boss_attacks = current_boss["attacks"]
    loot_bonus = current_boss["loot_bonus"]
    grace_available = wending_grace_unlocked

    print_black("\nYou move closer and closer to your goal...")
    time.sleep(2)

    print_black("\nYou hear something big apporach...")
    time.sleep(2)

    print_boss(f"\n{boss_name} HAS APPEARED!")
    play_music("bossmusic3.wav")
    print()
    print()
    
    time.sleep(3)


    #combat boss 3
    while player_hp > 0 and boss_hp > 0:

        print_good(f"\nyour HP {player_hp}/{max_hp}")
        print_magic(f"your FP: {fp}/{max_fp}")
        print_boss(f"{boss_name} HP: {boss_hp}")

        choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\n1- attack\n2- special moves\n3- heal\n> ")


        #attack block
        if choice == "1":
            damage = attack(weapon_dmg, strength)

            if crit(dexterity):
                damage *= 1.5
                print()
                print_good("CRITICAL HIT!")
                print()

            boss_hp -= damage

            print()
            print_good(f"you dealt {damage} damage!")
            print()
            time.sleep(2.6)


        elif choice == "2":
            damage, fp, move_used = specials_function(
                specials,
                specials_fp,
                specials_dmg,
                fp,
                weapon_dmg,
                main_stat
            )

            if move_used == "back":
                continue

            if damage is None:
                print_boss("not enough FP!")
                print()
                continue

            boss_hp -= damage

            print()
            print_magic(f"You used {move_used}")
            print_good(f"you dealt {damage} damage!")
            print()
            time.sleep(2.6)


        #healing block
        elif choice == "3":
            if flasks > 0:
                missing_hp = max_hp - player_hp

                if missing_hp <= 0:
                    print_boss("your HP is already full!")
                    print()
                    continue

                healing = r.randint(40, 60)

                if healing > missing_hp:
                    healing = missing_hp

                player_hp += healing
                flasks -= 1

                print()
                print_good(f"you healed {healing} HP")
                print_good(f"your HP {player_hp}/{max_hp}")
                print_good(f"remaining flasks: {flasks}")
                print()
                time.sleep(2.6)

            else:
                print()
                print_boss("no flasks remaining!")
                print()
                time.sleep(2.6)
                continue


       


        else:
            print("dude really did you missclick?")
            time.sleep(2.6)
            continue


        if boss_hp <= 0:
            break


        #boss attack
        attack_name = r.choice(list(boss_attacks.keys()))

        attack_data = boss_attacks[attack_name]

        damage_range = attack_data["damage"]
        hit_zones = attack_data["hit_zones"]

        damage = r.randint(damage_range[0], damage_range[1])
        damage = max(1, int(damage * (100 / (100 + defence))))

        print(f"\n{boss_name} uses {attack_name}!")

        dodged = dodge_attack(hit_zones, 2.2)

        if dodged:
            print_good("YOU DODGED!")
            print()
            time.sleep(2.6)

        else:
            player_hp, grace_available = take_damage(
                                player_hp,
                                damage,
                                grace_available
                                )
            print_boss(f"you took {damage} damage!")
            print()
            time.sleep(2.6)


#win/lose
    if boss_hp <= 0:
        winsound.PlaySound(None, 0)

        win_sound = resource_path("assets/sound/winsound.wav")

        winsound.PlaySound(
            str(win_sound),
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )







        print(Fore.MAGENTA + Style.DIM +"\nCOSMIC BEING FELLED")
        time.sleep(5)


                #loot and rune drop
        item_name, item_stat, loot_type, rarity = loot_roll(tier3_loot, loot_bonus)

        if loot_type == "wpn":
            inventory["weapons"][item_name] = item_stat
        else:
            inventory["armor"][item_name] = item_stat


        #print normal loot
        print_loot(f"\n{rarity.upper()} LOOT!", rarity)

        if loot_type == "wpn":
            print_loot(item_name, rarity)
            print_loot(f"Damage: {item_stat}", rarity)
        else:
            print_loot(item_name, rarity)
            print_loot(f"Defence: {item_stat}", rarity)


        #double drop
        double_drop = r.randint(1, 100)

        if double_drop <= 20:

            if loot_type == "wpn":
                second_type = "armor"
            else:
                second_type = "wpn"

            second_name, second_stat, second_type, second_rarity = loot_roll(
                tier2_loot,
                loot_bonus,
                second_type
            )

            print_reward(f"\n{second_rarity.upper()} BONUS LOOT!")

            if second_type == "wpn":
                inventory["weapons"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Damage: {second_stat}", second_rarity)

            else:
                inventory["armor"][second_name] = second_stat
                print_loot(second_name, second_rarity)
                print_loot(f"Defence: {second_stat}", second_rarity)


        #runes
        rune_drop = current_boss["runes"]
        runes += rune_drop

        print_reward(f"\nYou gained {rune_drop} runes!")
        print_reward(f"Total runes: {runes}")
        time.sleep(5)


            #break
        (
        runes,
        strength,
        dexterity,
        vigor,
        mind,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat,
        weapon,
        weapon_dmg,
        armor,
        defence,
        flasks
        ) = break_screen(
        class_name,
        class_lore,
        specials,
        specials_fp,
        specials_dmg,
        weapon,
        weapon_dmg,
        armor,
        defence,
        strength,
        dexterity,
        vigor,
        mind,
        flasks,
        runes,
        max_hp,
        player_hp,
        max_fp,
        fp,
        main_stat
        )


    else:
                winsound.PlaySound(None, 0)

                winsound.PlaySound(None, 0)
                lose_sound = resource_path("assets/sound/defeatsound.wav")
                
                winsound.PlaySound(
                                str(lose_sound),
                                winsound.SND_FILENAME | winsound.SND_ASYNC
                            )

                print_boss("\nYOU DIED")
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                time.sleep(8)
                continue
            
        



    
    

    



    
#haleem info
    boss_name = "G.H.ISHAK the one below all"
    print()
    print()
    print_black("You walk towards the dark smelly ominous room..")
    print()
    time.sleep(2)
    print_black("you feel the dark aura of haleem..")
    print()
    time.sleep(2)
    print_black("you are sure he is in there..")
    print()
    time.sleep(2)
    print_black("you steel yourself and take the step foward")
    print()
    time.sleep(2)
    play_cutscene("assets/cutscenes/haleem_intro.mp4")
    print()
    print()
    print()
    

    time.sleep(3)






    #outer loop
    while True:




    #thememusic
        play_music("haleemsong.wav")



    #player/boss info
        player_hp = 100 + vigor // 1.1
        boss_hp = 1500
        fp = 80 + mind  
        phase_two = False
        grace_available = wending_grace_unlocked








    #inner loop
        while player_hp > 0 and boss_hp > 0:

            print_good(f"your HP {player_hp}/{max_hp}")
            print_magic(f"your FP: {fp}/{max_fp}")
            print_boss(f"{boss_name} HP: {boss_hp}")

            choice = input(Fore.LIGHTBLACK_EX + Style.BRIGHT + "\n1- attack\n2- special moves\n3- heal\n> ")





    #attack block
            if choice == "1":
                damage = attack(weapon_dmg, strength)
                if crit(dexterity):
                    damage *= 1.5
                    print()
                    print_good("CRITICAL HIT!")
                    print()
                    time.sleep(2.6)
                

                boss_hp -= damage
                print()
                print_good(f"you dealt {damage} damage!")
                print()
                time.sleep(2.6)

            elif choice == "2":
                damage, fp, move_used = specials_function(specials, specials_fp, specials_dmg, fp, weapon_dmg, main_stat)
                if move_used == "back":
                    continue






                if damage is None:
                    print_boss("not enough FP!")
                    print()
                    time.sleep(2.6)
                    continue

                boss_hp -= damage
            
                print()
                print_magic(f"You used {move_used}")
                print_good(f"you dealt {damage} damage!")
                print()
                time.sleep(2.6)
    
        

                
    #healing block
            elif choice == "3": 
                if flasks > 0:
                    missing_hp = max_hp - player_hp
                    if missing_hp <= 0:
                        print_boss("your HP is already full!")
                        print()
                        time.sleep(2.6)
                        continue
                    healing = r.randint(40,60)

                    if healing > missing_hp:
                        healing = missing_hp
                    player_hp += healing
                    flasks -= 1

                    print()
                    print_good(f"you healed {healing} HP")
                    print_good(f"your HP {player_hp}/{max_hp}")
                    print_good(f"remaining flasks: {flasks}")
                    print()
                    time.sleep(2.6)
                else:
                    print()
                    print_boss("no flasks remaining!")
                    print()
                    time.sleep(2.6)
                    
        
                
                

            else:
                print("dude really did you missclick?")
                time.sleep(2.6)
                continue

            if boss_hp <= 0:
                break




        #phase two
            if boss_hp <= 750 and phase_two == False:
                phase_two = True
                print_boss("ay bayi me very GINGAL!!!\n *haleem gets into the push up postion and does one REP*")
                time.sleep(3)
                print()
                print_boss("Haleem has Evolved\n phase two has begun!")
                time.sleep(3)
                print()
                print()
            




    #boss attack
            damage, hit_zones = boss_attack(phase_two)
            dodged = dodge_attack(hit_zones, 2.2)
            if dodged == True:
                print_good("you DODGED!")
                time.sleep(2.6)
                print()
            else:
                player_hp, grace_available = take_damage(
                    player_hp,
                    damage,
                    grace_available
                    )
                print_boss(f"you took {damage} damage!")
                time.sleep(2.6)
                
                print()

            
        

        if boss_hp <= 0:
            winsound.PlaySound(None, 0)
            win_sound = resource_path("assets/sound/winsound.wav")

            winsound.PlaySound(
                str(win_sound),
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )





            
            print_reward("\nCELESTAIL BEING CONTAINED")
            time.sleep(7)
            winsound.PlaySound(None, 0)
            time.sleep(4)
            play_cutscene("assets/cutscenes/end_cutscene.mp4")
            print_black("you did it tarnished")
            time.sleep(3)
            print_black("you have fought long and hard")
            time.sleep(3)
            print_black("farewell...")
            time.sleep(3)
            break
        else:
            winsound.PlaySound(None, 0)
            lose_sound = resource_path("assets/sound/defeatsound.wav")

            winsound.PlaySound(
                str(lose_sound),
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )





            print_boss("\nYOU DIED")
            print()
            print()
            print()
            print()
            print()
            print()
            print()

        
            time.sleep(8)
            break

        


    