GL=set()
print("Groceries list")
def adding():
  item=input("Enter the item you want to add: ").lower()
  GL.add(item)
  return f"{item},has been added to the list"
def removing():
  item=input("Enter the item you want to remove: ").lower()
  if item not in GL:
    return f"{item} is not in the list"
  else:
    GL.discard(item)
    return f"{item},has been removed from the list"
def viewing():
  if GL:
    print("Your list is")
    for i in GL:
      print(i)
  else:
    print("Your list is empty")
def quit():
  return "Goodbye"
while True:
  print("\n\nSelect the options you want")
  print("1. Add an item")
  print("2. Remove an item")
  print("3. View the list")
  print("4. Exit")
  choice=int(input("Enter your choice: "))
  if choice==1:
    addlist=adding()
    print(addlist)
  elif choice==2:
    remove=removing()
    print(remove)
  elif choice==3:
    view=viewing()
  else:
    quits=quit()
    break
    
  
    
  