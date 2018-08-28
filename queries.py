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


###
 # return how many items are weapons and how many are not
 ##
weapon_amount = Weapon.objects.all().count()
not_weapon_amount = Item.objects.all().count()


###
 # get avaerage number of items each character holds
 ##
total_items_held = 0
all_chars = Character.objects.all()

for i in range(char_amount):
    total_items_held += all_chars.inventory.count()


average_amount_of_items_held = total_items_held / char_amount