# IMDB_Trailers
Gets a trailer for movies in IMDB. If there is a trailer for the movie, its will return the link, otherwise returns not found.

Python sends requests to the movie search page and opens each movie in the result.
If the trailer element exists, it opens the page of the movie trailer and returns the link to the best quality trailer link that was found.
If the trailer element does not exists, it will return "${movie_name} has no trailer"
