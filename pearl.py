from itertools import combinations


Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

name =  {'Kevin': Kevin, 'Stuart': Stuart, 'Bob': Bob, 'Edith': Edith}

minions = [Kevin,Stuart,Bob,Edith]
comb = combinations(minions,2)
comb = list(comb)

pairs = {}

for set1,set2 in comb :
  
  common = set1.intersection(set2)
  pairing = (len(common)/len(set1))*100
  if pairing>=30 :
    tup = (set1,set2)
    pairs[tup]= pairing


dj = sorted(pairs.items(), key = lambda x: x[1] , reverse = True)

for (set1,set2), percent in dj:
  set1_name = {k for k,v in name.items() if v==set1}.pop()
  set2_name = {k for k,v in name.items() if v==set2}.pop()
  print(f"{set1_name}  and {set2_name} has overlap of = {percent} %")


  
               
    
    