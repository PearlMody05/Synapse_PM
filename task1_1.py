from itertools import combinations


Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicki Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "The Weeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "The Weeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicki Minaj", "Kanye West", "Coldplay"}


djs = {'Kevin': Kevin, 'Stuart': Stuart, 'Bob': Bob, 'Edith': Edith}

valid_pairs = []


for (dj1, artists1), (dj2, artists2) in combinations(djs.items(), 2):
    common_artists = artists1.intersection(artists2)
    overlap1 = (len(common_artists) / len(artists1)) * 100
    overlap2 = (len(common_artists) / len(artists2)) * 100
  
    if overlap1 >= 30 and overlap2 >= 30:
        average_overlap = (overlap1 + overlap2) / 2
        valid_pairs.append(((dj1, dj2), average_overlap))


valid_pairs.sort(key=lambda x: x[1], reverse=True)


for (dj1, dj2), overlap in valid_pairs:
    print(f"{dj1} and {dj2} have an average overlap of {overlap:.2f}% in their music preferences.")



  
               
    
    