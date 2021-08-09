print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Choose your own adventure!")
print("Your mission is to survive.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_choice = input("You're lost and Google Maps is down. At the next road do you turn LEFT or RIGHT?\n").lower()
if first_choice == "left":
  second_choice = input("You ended up at the Jersey Shore. Do you SWIM far away, or WAIT for a boat?\n").lower()
  if second_choice == "wait":
    third_choice = input("A yacht pulls up. Do you trust them enough to get on the YACHT, WAIT, or RUN?\n").lower()
    if third_choice == "yacht":
      print("The yacht is being driven by Danny DeVito and is well stocked with plenty of rum hams. You Win!")
    elif third_choice == "wait":
      print("The sight of fake tans and sound of Pitbull drive you to insanity while you continue waiting. Game Over.")
    elif third_choice == "run":
      print("You run until you can't anymore. You end up in New York City, where you decide to settle down and start a future. The rent is 5x what you were paying and you live in a closet with 6 roommates. You can't drive anywhere and subway feels and smells like sardine cans. All of the sports teams are awful and nobody will stop telling you that its the water that makes the bagels good. A beer cost $9 and a Philly 'Cheesesteak' comes out of a grocery store box with ketchup. You insist to all of your friends and family its the greatest city in the world at least a dozen times at every family reunion, but they started a private Facebook group so they could talk about how annoying you've become. Several decades later you come to terms that New York wasn't that great on your deathbed and wish you would've swam. Game Over.")
  elif second_choice == "swim":
    print("You almost made it to Europe but failed. Game Over.")
elif first_choice == "right": 
  print("You found out you're actually using Apple Maps and it led you into a lake. Game Over.")
