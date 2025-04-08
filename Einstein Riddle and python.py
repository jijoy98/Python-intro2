# Initialize the table with placeholders for the house attributes
houses = [
    {"House": 1, "Color": None, "Nationality": None, "Beverage": None, "Cigar": None, "Pet": None},
    {"House": 2, "Color": None, "Nationality": None, "Beverage": None, "Cigar": None, "Pet": None},
    {"House": 3, "Color": None, "Nationality": None, "Beverage": None, "Cigar": None, "Pet": None},
    {"House": 4, "Color": None, "Nationality": None, "Beverage": None, "Cigar": None, "Pet": None},
    {"House": 5, "Color": None, "Nationality": None, "Beverage": None, "Cigar": None, "Pet": None}
]

# Define the clues from the puzzle
clues = [
    ("Norwegian", 1, "House"),
    ("Milk", 3, "Beverage"),
    ("Green", 4, "Color"),
    ("White", 5, "Color"),
    ("Coffee", 4, "Beverage"),
    ("Blue", 2, "Color"),
    ("Brit", 3, "Nationality"),
    ("Swede", 5, "Nationality"),
    ("Danish", 2, "Nationality"),
    ("Tea", 2, "Beverage"),
    ("Pall Mall", 3, "Cigar"),
    ("Birds", 3, "Pet"),
    ("Dunhill", 1, "Cigar"),
    ("Cats", 1, "Pet"),
    ("Blends", 2, "Cigar"),
    ("Horses", 2, "Pet"),
    ("Beer", 5, "Beverage"),
    ("BlueMaster", 5, "Cigar"),
    ("Princes", 4, "Cigar"),
    ("German", 4, "Nationality"),
    ("Fish", 4, "Pet"),
    ("Blends", 2, "Cigar"),
    ("Water", 1, "Beverage")
]

# Helper function to update the house attributes
def update_house(houses, house_num, attribute, value):
    houses[house_num - 1][attribute] = value

# Apply the clues to the houses
for clue in clues:
    value, house_num, attribute = clue
    update_house(houses, house_num, attribute, value)

# Display the results
for house in houses:
    print(f"House {house['House']}: Color={house['Color']}, Nationality={house['Nationality']}, "
          f"Beverage={house['Beverage']}, Cigar={house['Cigar']}, Pet={house['Pet']}")

# Find who owns the fish
for house in houses:
    if house['Pet'] == "Fish":
        print(f"The person who owns the fish is the {house['Nationality']}.")
