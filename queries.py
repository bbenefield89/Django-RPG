from charactercreator.models import Character

###
 # return amount of total characters in DB
 ##
char_amount = Character.objects.all().count()
