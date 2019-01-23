import random

from flask import Blueprint, render_template

blueprint = Blueprint('frontend', __name__)

# I grabbed this list from https://nameberry.com/unisex-names. If I get to
# building a name-input dialog than we'll switch, but I kinda like just randomly
# giving people a name.
GENDER_NEUTRAL_NAMES = [
    "Alexis",
    "Amari",
    "Angel",
    "Ariel",
    "Avery",
    "Blake",
    "Charlie",
    "Dakota",
    "Dallas",
    "Eden",
    "Elliot",
    "Elliott",
    "Emerson",
    "Emery",
    "Finley",
    "Harley",
    "Hayden",
    "Jordan",
    "Karter",
    "Kendall",
    "London",
    "Marley",
    "Morgan",
    "Parker",
    "Payton",
    "Peyton",
    "Phoenix",
    "Quinn",
    "Reese",
    "Remington",
    "Riley",
    "River",
    "Rowan",
    "Rylan",
    "Sawyer",
    "Taylor",
    "Zion",
]


@blueprint.route('/', methods=['GET'])
def get_index():
    random_username = random.choice(GENDER_NEUTRAL_NAMES)

    return render_template('index.html', random_username=random_username)
