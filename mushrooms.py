def determine_mushroom():
    # First question: Does the mushroom have gills?
    gills = input("Does your mushroom have gills? (yes/no): ").strip().lower()
    
    if gills == "no":
        # If the mushroom does not have gills, it must be Cepe de Bordeaux
        print("Your mushroom is: Cepe de Bordeaux")
        return
    
    # If the mushroom has gills, we proceed to the second question.
    
    # Second question: Does the mushroom grow in a forest?
    forest = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()
    
    if forest == "no":
        # If it doesn't grow in a forest, it must be one of the mushrooms that grow in a meadow:
        # Agaric jaunissant or Coprin chevelu
        # Third question: Does the mushroom have a ring?
        ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
        
        if ring == "yes":
            print("Your mushroom is: Coprin chevelu")
        else:
            print("Your mushroom is: Agaric jaunissant")
        return
    
    # If the mushroom grows in a forest, we proceed to the third question.
    
    # Third question: Does the mushroom have a ring?
    ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
    
    if ring == "yes":
        # If the mushroom has a ring, it could be:
        # Amanite tue-mouche or Coprin chevelu
        # Fourth question: Does your mushroom have a convex cup?
        convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()
        
        if convex_cup == "yes":
            print("Your mushroom is: Amanite tue-mouche")
        else:
            print("Your mushroom is: Coprin chevelu")
    else:
        # If it doesn't have a ring, it could be either:
        # Girolle or Pied Bleu
        # Fourth question: Does your mushroom have a convex cup?
        convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()
        
        if convex_cup == "yes":
            print("Your mushroom is: Pied Bleu")
        else:
            print("Your mushroom is: Girolle")

# Start the decision process
determine_mushroom()