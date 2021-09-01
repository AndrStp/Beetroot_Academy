# A simple function.

# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
# The function should then print “My favorite movie is named {name}”.

def simple_func(movie_name: str) -> str:
    """Returns your favourite movie"""
    return f'My favorite movie is named {movie_name}'

name = input('Enter your favourite movie name: ')

print(simple_func(name))