########################################################################################
# Web Scraping with Pandas
# https://www.youtube.com/watch?v=inGyy7rzeI4&ab_channel=FrankAndrade
########################################################################################

################
# Libraries    #
################

import pandas as pd


###############################################
# Example 1: Highest Grossing Movies          #
###############################################

highest_grossing_movies = pd.read_html('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')
type(highest_grossing_movies)
print(highest_grossing_movies)

len(highest_grossing_movies)

# Practically all the information on the website.

###############################################
# Extract the información from some tables    #
###############################################

highest_grossing_movies[0]
highest_grossing_movies[1]
highest_grossing_movies[3]


########################################################
# Example 2: fastestlaps.com/tracks/le-mans-bugatti    #
########################################################

fastestlaps_bugatti = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti')
len(fastestlaps_bugatti)
print(fastestlaps_bugatti[0].head(15))



screener = pd.read_html('https://coindar.org/en/coins/')