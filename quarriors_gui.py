import csv
import random
from tkinter import tk
tkinter._test()

class Card:
  def __init__(self, type, name, sub_name, set, cost, glory, lvd):
    self.type = type
    self.name = name
    self.sub_name = sub_name
    self.set = set
    self.cost = cost
    self.glory = glory
    self.lvd = lvd

  def __str__(self):
    return f"{self.name} ({self.set})"

def load_cards_from_csv(filename):
  """
  Loads card data from a CSV file and creates a list of Card objects.

  Args:
    filename: The name of the CSV file.

  Returns:
    A list of Card objects.
  """

  cards = []
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      try:
        cost_value = int(row['Cost']) if row['Cost'] else 0
        glory_value = int(row['Glory']) if row['Glory'] else 0
      except ValueError:
        # Skip rows with non-numerical 'Cost' or 'Glory' values
        continue
      cards.append(Card(
        row['Type'],
        row['Name'],
        row['Sub Name'],
        row['Set'],
        cost_value,
        glory_value,
        row['LvD']
      ))
  return cards

def choose_cards(all_cards, desired_releases):
  chosen_spells = []
  chosen_creatures = []

  filtered_cards = [card for card in all_cards if card.release in desired_releases]

  for card in filtered_cards:
    if card.type == "Spell" and len(chosen_spells) < 3:
      rand_spell = random.choice([spell for spell in filtered_cards if spell.type == "Spell"])
      if rand_spell.name not in [spell.name for spell in chosen_spells]:
        chosen_spells.append(rand_spell)
    elif card.type == "Creature" and len(chosen_creatures) < 7:
      rand_creature = random.choice([creature for creature in filtered_cards if creature.type == "Creature"])
      if rand_creature.name not in [creature.name for creature in chosen_creatures]:
        chosen_creatures.append(rand_creature)

  return chosen_spells, chosen_creatures

def update_card_display(chosen_spells, chosen_creatures):
  # Update your GUI elements to display the chosen cards (replace with your logic)
  # Here's an example using labels (assuming you have label widgets):
  spell_label.config(text="\n".join([f"{spell.name} ({spell.sub_name})" for spell in chosen_spells]))
  creature_label.config(text="\n".join([f"{creature.name} ({creature.sub_name})" for creature in chosen_creatures]))

def handle_button_click():
  # Get desired sets from checkboxes (replace with your logic)
  desired_sets = [set_var.get() for set_var in set_checkboxes]
  chosen_spells, chosen_creatures = choose_cards(all_cards, desired_sets)
  update_card_display(chosen_spells, chosen_creatures)

# Load card data from a CSV file
filename = "quarriors_cards.csv"  # Replace with your actual filename
all_cards = load_cards_from_csv(filename)

# Create the main window
window = Tk()
window.title("Quarriors Card Selector")

# Create labels for instructions and card displays
instruction_label = Label(window, text="Select desired sets and click 'Choose Cards':")
instruction_label.pack()

# Create checkboxes for available sets (replace with your list of sets)
available_sets = ["Base Game", "Light vs Dark", "Darkness Rising"]
set_checkboxes = []
for set_name in available_sets:
  set_var = IntVar()  # Use IntVar for checkboxes
  checkbox = Checkbutton(window, text=set_name, variable=set_var)
  checkbox.pack()
  set_checkboxes.append(set_var)

# Create a button to trigger card selection
button = Button(window, text="Choose Cards", command=handle_button_click)
button.pack()

# Create labels to display chosen spells and creatures (replace with your layout)
spell