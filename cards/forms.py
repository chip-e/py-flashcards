# cards/forms.py
# To send POST requests containing a form to back end, telling app whether user knew answer or not

from django import forms

# form schema containing two fields:
# card_id: primary key of card being checked
# solved: boolean value depending on whether user knows the answer
# with "required" argument to define if field needs to contain data to make form valid
class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
