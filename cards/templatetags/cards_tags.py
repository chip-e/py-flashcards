# cards/templatetags/cards_tags.py

# imports template module
from django import template

# imports Card model and BOXES variables 
from cards.models import BOXES, Card

# creates instance of Library used for registering template tags
register = template.Library()

# uses Library instances'.inclusion_tag() as decorator, adding functionality to existing function, by wrapping it in another function
@register.inclusion_tag("cards/box_links.html")
# looping over BOXES, defines card_count to keep track # of cards in current box
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
# Append dictionary with box number as key and # of cards in the box as value to boxes list
        boxes.append({"number": box_num, "card_count": card_count})
# returns dictionary with boxes data
    return {"boxes": boxes}

