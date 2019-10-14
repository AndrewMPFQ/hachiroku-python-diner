
# Hachiroku Diner

import time
import random

main_menu = {
	'Ramen': 10.99,
	'Hamburger': 11.99,
	'Sushi': 12.99,
	'Steak': 13.99,
} 

sides_menu = {
	'French Fries': 1.45,
	'Salad': 1.99,
	'Soup': 2.45,
	'Baked Potato': 2.99,
} 

waitress_comments_entree = [
  '\nGreat choice!',
  '\nExcellent choice!',
]

waitress_comments_sides = [
  '\nExcellent we will get all that started for you right away',
  '\nThank you for ordering with us, we will start your order right away',
]

waitress_negative = '\nSorry, we do not serve that. Please choose between the listed options of Hambuger, Steak, Sushi or Ramen.'

waitress_negative2 = '\nSorry, that is not a side we serve. Please choose between French Fries, Salad, Soup, or Baked potato.'

main_total = list(main_menu.items())

sides_total = list(sides_menu.items())

user_selection = []

def hachiroku_diner(main = main_total, user_selection = user_selection, sides = sides_total):
  	print ("\nWelcome to Hachiroku Diner!\n")
  	time.sleep(1)
  	welcome()


def welcome():
  
	  the_menu = input("Would you like to see our menu?  ")

	  if the_menu == "yes":
	    print("\nHere is what we have to choose from.\n")
	    the_main_menu()

	  elif the_menu == "no":
	    print("Okay, goodbye")
	    quit()

	  else:
	    print("\nPlease enter yes or no")
	    welcome()


def the_main_menu():
	  time.sleep(2)
	  print('~~ Dinner Menu ~~\n')
	  for keys, values in main_menu.items():
	    print(f"{keys}: ${str(values)}")
	  main_menu_selection(user_selection)



def main_menu_selection(user_selection):
	  time.sleep(2)
	  main_choice = input("\nWhat would you like? \n")
	  main_choice = main_choice.title()

	  if main_choice == 'Hamburger':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(main_choice)
	    hamburger_options()

	  elif main_choice == 'Steak':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(main_choice)
	    steak_options()

	  elif main_choice == 'Sushi':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(main_choice)
	    sushi_options()

	  elif main_choice == 'Ramen':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(main_choice)
	    ramen_options()

	  else:
	    print(waitress_negative)
	    main_menu_selection(user_selection)



def hamburger_options():
	  time.sleep(1)
	  print('\nHere is our options for sides')
	  time.sleep(1)
	  print('You can choose up to two sides')
	  time.sleep(2)
	  print('\n~~ Sides Menu ~~\n')
	  
	  for keys, values in sides_menu.items():
	    print(f"{keys}: ${str(values)}")
	  sides_menu_selection(user_selection)



def steak_options():
	  time.sleep(1)
	  print('\nHere is our options for sides')
	  time.sleep(1)
	  print('You can choose up to two sides')
	  time.sleep(2)
	  print('\n~~ Sides Menu ~~\n')
	  
	  for keys, values in sides_menu.items():
	    print(f"{keys}: ${str(values)}")
	  sides_menu_selection(user_selection)



def sushi_options():
	  time.sleep(1)
	  print('\nHere is our options for sides')
	  time.sleep(1)
	  print('You can choose up to two sides')
	  time.sleep(2)
	  print('\n~~ Sides Menu ~~\n')
	  
	  for keys, values in sides_menu.items():
	    print(f"{keys}: ${str(values)}")
	  sides_menu_selection(user_selection)



def ramen_options():
	  time.sleep(1)
	  print('\nHere is our options for sides')
	  time.sleep(1)
	  print('You can choose up to two sides')
	  time.sleep(2)
	  print('\n~~ Sides Menu ~~\n')
	  
	  for keys, values in sides_menu.items():
	    print(f"{keys}: ${str(values)}")
	  sides_menu_selection(user_selection)


def sides_menu_selection(user_selection):
	  time.sleep(2)
	  sides_menu_choices = input('\nWhich sides would you like? \n')
	  sides_menu_choices = sides_menu_choices.title()
	  
	  if sides_menu_choices == 'French Fries':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(sides_menu_choices)
	    sides_menu_selection2(user_selection)
	  
	  elif sides_menu_choices == 'Salad':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(sides_menu_choices)
	    sides_menu_selection2(user_selection)

	  elif sides_menu_choices == 'Soup':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(sides_menu_choices)
	    sides_menu_selection2(user_selection)
	  
	  elif sides_menu_choices == 'Baked Potato':
	    print(random.choice(waitress_comments_entree))
	    user_selection.append(sides_menu_choices)
	    sides_menu_selection2(user_selection)

	  else:
	    print(waitress_negative2)
	    sides_menu_selection(user_selection)



def sides_menu_selection2(user_selection):
	  time.sleep(1)
	  sides_menu_choices2 = input('\nand for your second side? \n')
	  sides_menu_choices2 = sides_menu_choices2.title()

	  if sides_menu_choices2 == 'French Fries':
	    print(random.choice(waitress_comments_sides))
	    user_selection.append(sides_menu_choices2)
	    final_total(user_selection)
	  
	  elif sides_menu_choices2 == 'Salad':
	    print(random.choice(waitress_comments_sides))
	    user_selection.append(sides_menu_choices2)
	    final_total(user_selection)

	  elif sides_menu_choices2 == 'Soup':
	    print(random.choice(waitress_comments_sides))
	    user_selection.append(sides_menu_choices2)
	    final_total(user_selection)

	  elif sides_menu_choices2 == 'Baked Potato':
	    print(random.choice(waitress_comments_sides))
	    user_selection.append(sides_menu_choices2)
	    final_total(user_selection)

	  else:
	    print(waitress_negative2)
	    sides_menu_selection2(user_selection)


def final_total(user_selection, main = main_total, sides = sides_total):
	  time.sleep(3)
	  user_selection_total = 0
	  for key, value in main:
	    for ordered_item in user_selection:
	      if key == ordered_item:
	        user_selection_total += value
	  
	  for key, value in sides:
	    for ordered_item in user_selection:
	      if key == ordered_item:
	        user_selection_total += value
	  
	  print(f'\nYour total will be: ${user_selection_total}')


hachiroku_diner()