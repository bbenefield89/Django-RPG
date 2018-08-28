from charactercreator.models import Character
from armory.models import Item, Weapon

###
 # return amount of total characters in DB
 ##
char_amount = Character.objects.all().count()

###
 # return total amount of items in DB
 ##
items_amount = Item.objects.all().count() + Weapon.objects.all().count()