

movie_name:str = "interstellar"
movie_rate:int = 3
movie_popularity:float = 72.65

if movie_rate >= 4 and movie_popularity > 80 :
    print("Highly recommended")
elif movie_rate >= 4 and movie_popularity > 70 :
    print("I recommended it, it's good")
elif movie_rate <= 2 and movie_popularity > 60 :
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")











