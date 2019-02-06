# Modules
import random
import os
import time
import textwrap

# Functions that don't need classes.

def clear_screen():
  time.sleep(2)
  print ("\n" * 100)

def FirstCutScene():
  clear_screen()
  print(textwrap.fill(f"Welcome to the Country of Entarc. \nHere, the lands are separated mostly by water. One needs a boat to get to any island. \n{player_name} sails into the ports of one of its islands. They disembark and find a little village upon the foot of a mountain. It towers way above the seas.", 70))
  first_act= ""
  check_sail=['check', 'sail']
  while first_act not in check_sail:
    first_act = input("Sail away or check the house? ")
    if first_act.lower() == "check":
      break
    elif first_act.lower() == "sail":
      print(f"{player_name} got back in their boat and sailed off.")
      time.sleep(1)
      print("...")
      time.sleep(1)
      print(textwrap.fill(f"But days went on and {player_name} failed to find any islands. They ran out of resources, and starved..."))
      time.sleep(5)
      player_one.Death("starvation")

def SecondCutScene():
  clear_screen()
  print(textwrap.fill(f"{player_name} moves towards the house, but was stopped by a tall figure. He seemed built with dark, excessively stylized hair. Behind him was a shorter figure. This one had tealish hair, and seemed to be wearing way too little for the weather. Like even this chilly weather was too cool.", 70))
  second_act= ""
  run_fight= ['run', 'fight']
  while second_act not in run_fight:
    second_act = input("Run or Fight? ")
    if second_act.lower() == "fight":
      print(textwrap.fill(f"You don't have much, but you try to swing at the taller one. Though he stops your fist, the shorter one seems to grasp his necklace.", 70))
      break
    elif second_act.lower() == "run":
      print(textwrap.fill(f"{player_name} attempts to escape, but the taller one raises his hand. A strange orange glow grows around it before engulfing you in a painful blaze of glory"))
      time.sleep(5)
      player_one.Death("fire magic")
      break

def ThirdCutScene():
  #  clear_screen()
  print(textwrap.fill(f"You can confront the shorter one, or focus on the taller one.", 70))
  third_act= ""
  short_tall= ['taller', 'shorter']
  deebee_hurt = ""
  while third_act not in short_tall:
    third_act = input("Fight the Tall one or Short one? ")
    if third_act.lower() == "short":
      deebee_hurt = True
      print(textwrap.fill(f"He panics as {player_name} attacks. They snatch it, and it seems like there's a powerful, freezing cold aura from it. By the time {player_name} has taken note, he's run off into the dark. But there's a blueish glow around him, causing him to screech in pain as he ran.", 70))
      time.sleep(8)
      clear_screen()
      break
    elif third_act.lower() == "tall":
      deebee_hurt = False
      print(textwrap.fill(f"He's pretty powerful! While trying to overpower you, his shorter minion tries to attack as well. The taller one stops paying heed to you in order to smack the smaller one's hand down in annoyance.\n\n\"I didn't tell you that you could do that!\" He snapped."))
      time.sleep(8)
      clear_screen()
      break


class Entity(object):
  def __init__ (self, ent_name, ent_health):
    self.ent_name = ent_name
    self.ent_health = ent_health

class Player(Entity):
  def __init__ (self, ent_name, ent_health, play_str, play_def):
    Entity.__init__(self,ent_name, ent_health)
    self.play_str = play_str
    self.play_def = play_def

  # Create a Hurt and Death Function.
  def Death(self, cause):
    clear_screen()
    time.sleep(2)
    print(f"{self.ent_name} succumbed to {cause}.")
    exit(1)


print("Type Your Name.")
player_name = input("My name is... ")
player_health = 20
player_str = (random.randint(1, 10))
player_def = (random.randint(1, 10))
gold= 0
print(f"{player_name}'s strength is {player_str}. Their defense is {player_def}.")


# End Engine!!
player_one= Player(player_name, 50, player_str, player_def)
clear_screen()
FirstCutScene()
SecondCutScene()
ThirdCutScene()
print(textwrap.fill(f"Story's still a work in progress. Thanks for reading this so far."))
exit(1)
