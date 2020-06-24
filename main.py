import re
import random

counter = 0
compwoordenlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]                        
hetwoord = random.choice(compwoordenlist)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("goedemorguuuh welkom bij galgje, probeer het woord te raden maar let op je hebt maar 5 pogingen!")
print("het woord heeft " + str(lengtewoord) + " letters")

while True:
  userguess = (input(": "))
  match = re.search(userguess, hetwoord)
  if userguess == hetwoord: 
    print('je heb het woord ' + '"' + hetwoord + '"' + " geraden")
    break
  
  elif match: 
    print("Goed geraden")
    for i in range(0, lengtewoord):
      if userguess == hetwoord[i]:
        temp = temp[:i] + userguess +temp[i+1:]
    print(temp)
        
  