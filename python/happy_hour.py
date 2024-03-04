import random

nature = ["Boulevard Park",
        "Discovery Park",
        "Lincoln Park",
        "Chuckanut Mountains",
        "Cougar Mountain"]

activity = ["Dodge Ball",
          "Volleyball",
          "Basketball",
          "Football",
          "Tennis",
          "Badmitten"]

random_nature = random.choice(nature)
random_activity_one = random.choice(activity)

print(f"How about we go to {random_nature} and bring {random_activity_one}?")
