print("Thank you for choosing Sapphy's Pizzaria!")

size = input("What size pizza would you like today? Please choose S, M, or L. :").upper()
pepperoni = input("Would you like pepporoni? Please choose Y or N. :").upper()
cheese = input("Would you like extra cheese? Please choose Y or N. :").upper()

bill = 0
size_choice = "NA"
pepperoni_choice = "NA"
cheese_choice = "NA"

if size == 'S':
  bill = 10
elif size == 'M':
  bill = 14
elif size == 'L':
  bill = 18

if pepperoni == 'Y':
  if size == 'S':
    bill += 1
  if size in ['M', 'L']:
    bill += 2

if cheese == 'Y':
  bill += 1

if size =="S":
  size_choice = 'small'
elif size == "M":
  size_choice = "medium"
elif size == "L":
  size_choice = "large"

if pepperoni == "Y":
  pepperoni_choice = "with pepperoni"
elif pepperoni == "N":
  pepperoni_choice = "without pepperoni"

if cheese == "Y":
  cheese_choice = "with extra cheese"
elif cheese == "N":
  cheese_choice = "without extra cheese"

print(f"You have ordered a {size_choice} pizza {pepperoni_choice} and {cheese_choice}.")
print(f"Your final bill is: £{bill}.")
