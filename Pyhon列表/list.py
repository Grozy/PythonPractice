movies = ["The Holy Grail",
          "The Life of Brain",
          "The Meaning of Life"]
print (movies)
print movies[1]
#print lenght
print ("\narr's lenght is:"+str(len(movies)))
#add an item
movies.append("Gilliam")
print("\nmovies.append(\"Gilliam\")"+str(movies))
print ("\narr's lenght is:"+str(len(movies)))
#pop an item
movies.pop()
print("\nmovies.pop()"+str(movies))
#append an array
movies.extend(["Gilliam","Chapman"])
print("\nmovies.extend([\"Gilliam\",\"Chapman\"])"+str(movies))
#remove an item
movies.remove("Gilliam")
print("\nmovies.remove(\"Gilliam\")"+str(movies))
movies.pop(1)
print("\nmovies.pop(1)"+str(movies))
movies.insert(1,"Gilliam")
print(movies)