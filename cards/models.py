#cards/models.py

from django.db import models

# Create your models here.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

# To evaluate whether card is moved to higher boxes or back to 1
# "solved" is True when answer is correct and False when incorrect
# "new_box" is current box num plus one if answer is correct, goes back to 1(BOX[0]) if incorrect
    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

# To prevent new_box from going over 5, only saves self.box new new_box is 1-5
        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self


