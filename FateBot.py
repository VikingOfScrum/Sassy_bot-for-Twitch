#dice roller
#objective tempt fate
# roll 1d20
'''
This is my wifes game she made back while I was taking cs 160. I wanted to surprise her by incorporating her game.
I made a few adjustments just to get it to work with sassy_bot
'''
import random





def Fate_Bot():
    
    

    dice = random.randint (1,20)
    

    if dice == 1:
        dice_message = "the Fates find your mere existence an insult and destroy all you love befoyre your eyes"

    if dice == 2:
        dice_message = "the Fates hand you a moldy sandwhich!"

    if dice == 3:
        dice_message = "the Fates curse you with warm beer everytime you order a drink."

    if dice == 4:
        dice_message = "the Fates curse to feel like you are constantly walking through spider webs."

    if dice == 5:
        dice_message = "the Fates decide to remove 1 kidney"

    if dice == 6:
        dice_message = "the Fates decide to burn your eyebrows off"

    if dice == 7:
        dice_message = "the Fates knock your salt shaker off the table, causing the lid to fall off and salting your entire floor."

    if dice == 8:
        dice_message = "the Fates remove all the toilet paper from your house and replace it with sandpaper."

    if dice == 9:
        dice_message = "the Fates hand you body temp warm soda and fade away."

    if dice == 10:
        dice_message = "the Fates shake your hand and fade away"

    if dice == 11:
        dice_message = "the fates hand you a cheeseburger and disappear"

    if dice == 12:
        dice_message = "the Fates hand you a satchel of your favourite snack."

    if dice == 13:
        dice_message = "the Fates hand you several flagons of high quality mead."

    if dice == 14:
        dice_message = "the Fates decide to pitty you and present you with high quality linen clothes."

    if dice == 15:
        dice_message = "the Fates give you a map leading to a possible treasure chest and reward."

    if dice == 16:
        dice_message = "the Fates bless you with a Ring of Protection +2."

    if dice == 17:
        dice_message = "the Fate give you a bag of rare gems."

    if dice == 18:
        dice_message = "the Fates grant you enchanted armor."

    if dice == 19:
        dice_message = "the Fates give you a large chest of Gold and rare treasures."

    if dice == 20:
        dice_message = "the Fates shower you infinite gifts and magical tokens, making your far richer and more powerful than any mortal on the planet."

    

    
    return dice, dice_message
   
       

