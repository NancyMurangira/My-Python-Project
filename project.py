name = input("Enter your name;")
print(f"Hello, {name}!")
print("")
print("Welcome to Unguka Book Library")
print("")
print("Please select your preferred genre:")
print("")
print("1. True Crime")
print("2. Women Fiction ")
print("3. Romantic")
print("4. Self Help")
print("5. Fairy Tale")

genre = input()
while genre <1 or genre >5:
    print("Invalid selection, please select your preferred genre again")
if genre == 1:  
    print(f"Books available in True Crime:")
    print("1. In Cold Blood: Four members of the Clutter family, who owned a farm in Kansas, were shot to death in their home.")
    print(" 2. My Dark Places:When James Ellroy was 10 years old, his mother was murdered.")
    print(" 3. The Stranger Beside Me: In the 1970s, aspiring crime novelist Ann Rule worked at a suicide hotline with Ted Bundy ")
    print(" 4. Midnight in Mexico: Alfredo Corchado spent his life building a career as a reporter. ")
    print("5. Killers of the Flower Moon: The richest people per capita in the world were members of the Osage Nation.")

elif genre == 2:  
    print(f"Books available in Women Fiction:")
    print("1. Between you and Us: A grieving woman must choose between the husband she loves and the daughter she lost")
    print("2. The ball at versailles: Captivating tale of four young women and one life-changing night.")
    print("3. Happily Never After: When Sophie finds out right before getting married that she has been cheated on (again!)")
    print("4. The Hidden life of Cecily Larson : A family secret, a DNA test, a journey as rich and early-day circus itself.")
    print("5. How to be good: Wwhen David stops being the angriest man and begins to be good with the help of his spiritual healer.")
elif genre == 3:  
    print(f"Books available in Romantic:")
    print("1. Seven days in June: Seven days to fall in love, fifteen years to forget, and seven days to get it all back again")
    print("2. Me before you: Louisa Clark takes a job as a caregiver for a wealthy banker who has become paralyzed ")
    print("3. Heartless: Working as a nanny for a single dad should have been simple. Except I can't keep my eyes off him.")
    print("4. Eclipse:It continues the story of Bella Swan and her vampire love, Edward Cullen")
    print("5. Icebreaker: An ice skater and the hockey captain she hates as they're forced to share a rink.")
elif genre == 4:  
    print(f"Books available in Self Help Books:")
    print("1. The 48 laws of Power: Show you what power looks like, how you can get it, what to do to defend yourself ")
    print("2. Atomic Habits: Guide to breaking bad behaviors and adopting good ones in four steps.")
    print("3. The 5AM club: Morning routine that has helped his clients maximize their productivity, activate their best health")
    print("4. Outliers;  Gladwell examines the factors that contribute to high levels of success.")
    print("5. Girl, wash your face: Inspires women to take their lives into their own hands and make their dreams happen")
elif genre == 5:
    print(f"Books available in Fairy Tale:")
    print("1. The tortoise and the hare: The account of a race between unequal partners has attracted conflicting interpretations")
    print("2. Scarlet: When Scarlet encounters Wolf, a street fighter who may have information as to her")
    print("3. The princess and the pea: a princess who is tested to become wife to a lonely prince.")
    print("4. 12 dancing princesses: A king suspects that his twelve daughters go dancing every night and gave a challenge to a prince.")
    print("5. The snow queen: The story centers on the struggle between good and evil")
else:
    print("Please select your preferred genre again:")

choice = input("Would you like to select another genre?(yes/no)").lower()
if choice == "yes":
    print("Thank you for using Unguka Book Library. See you next time!")
     








