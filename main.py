

def intro():
  
  itemnum = 0
  print("Welcome to the Great Variety marketplace")
  category = input("What will you be shopping for today?"+ "\n A- Video games, B- Clothes, C- Food, D- Collectibles, or E- miscellaneous ").lower()
  director(category)
  itemnum = input("What item would you like to view? 1, 2, 3, 4 ").lower()
  pricelister(category, itemnum)
  
  purchase(itemnum)








def anotheritem():
  addtocart = input("Another item? ")
  if addtocart == "yes":
    intro()
  if addtocart == "no":
    print("Come again soon!")
    exit()












print("Welcome to the Great Variety marketplace")
category = input("What will you be shopping for today?"+ "\n A- Video games, B- Clothes, C- Food, D- Collectibles, or E- miscellaneous ").lower()
VideoGames = ["Apex legends", "Super Smash Bros", "Super Mario Bros", "Pacman arcade Machine"]
Clothes = ["Jeans size 32", "Size M shirt", "Size M hoodie", "Size L sweatpants"]
Food = ["Kit Kat", "Cookies", "Pizza", "Pasta"]
Collectibles = ["Super bowl ring", "Watch", "Movie posters", "Figurines"]
Miscellaneous = ["Cooking set", "Grill spices", "Lego sets", "Sports gear"]

def director(category):
  if category == "a":
    print("Here is what we have today " + str(VideoGames))
  if category == "b":
    print("Here is what we have today " + str(Clothes))
  if category == "c":
    print("Here is what we have today " + str(Food))
  if category == "d":
    print("Here is what we have today " + str(Collectibles))
  if category == "e":
    print("Here is what we have today " + str(Miscellaneous))

director(category) 

itemnum = input("What item would you like to view? 1, 2, 3, 4 ").lower()

def pricelister(category, itemnum):
  while category == "a":
    if itemnum == "1":
      print(VideoGames[0] + " is $60")
      break
    if itemnum == "2":
      print(VideoGames[1] + " is $60")
      break
    if itemnum == "3":
      print(VideoGames[2] + " is $60")
      break
    if itemnum == "4":
      print(VideoGames[3] + " is $60")
      break
  while category == "b":
    if itemnum == "1":
      print(Clothes[0] + " is $80")
      break
    if itemnum == "2":
      print(Clothes[1] + " is $60")
      break
    if itemnum == "3":
      print(Clothes[2] + " is $40")
      break
    if itemnum == "4":
      print(Clothes[3] + " is $30")
      break
  while category == "c":
    if itemnum == "1":
      print(Food[0] + " is $2")
      break
    if itemnum == "2":
      print(Food[1] + " is $5")
      break
    if itemnum == "3":
      print(Food[2] + " is $10")
      break
    if itemnum == "4":
      print(Food[3] + " is $10")
      break
  while category == "d":
    if itemnum == "1":
      print(Collectibles[0] + " is $1,500")
      break
    if itemnum == "2":
      print(Collectibles[1] + " is $1,000")
      break
    if itemnum == "3":
      print(Collectibles[2] + " is $15")
      break
    if itemnum == "4":
      print(Collectibles[3] + " is $10")
      break
  while category == "e":
    if itemnum == "1":
      print(Miscellaneous[0] + " is $45")
      break
    if itemnum == "2":
      print(Miscellaneous[1] + " is $10")
      break
    if itemnum == "3":
      print(Miscellaneous[2] + " is $250")
      break
    if itemnum == "4":
      print(Miscellaneous[3] + " is $80")
      break

pricelister(category, itemnum)

def purchase(itemnum):
  transaction = input("Would you like to purchase? ").lower()
  if transaction == "yes":
    email = input("What is your email? ")
    verifyemail = input(email + " is your email, correct? ").lower()
    if verifyemail == "yes":
      print("Congratualtions on your brand new item! Shipping and recipts will be sent to your email at" + email)
      anotheritem()

    while verifyemail == "no":
      email = input("Enter it again please ")
      verifyemail = input(email + " is your email, correct? ").lower()
      if verifyemail == "yes":
        print("Congratualtions on your brand new item! Shipping and recipts will be sent to your email at" + email)
        anotheritem()

  
      

  if transaction == "no":
    askuser = input("Would you like to see another item? ").lower()
    if askuser == "yes":
      intro()
    if askuser == "no":
      print("Come again Soon!")
      exit()

purchase(itemnum)







  