animales = ['dog', 'cat', 'best friend']

found = False
for animal in animales:
    if animal == "best friend":
        print("We found the animal:", animal)
        found = True
        break
if not found:
    print("No animal found.")
