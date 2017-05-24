import fresh_tomatoes
import media

#This section is used to initialize the values in the Movie Class in the Media Module for each movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "Marine on the alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
avatar.show_trailer()
                     

finding_nemo = media.Movie("Finding Nemo",
                           "A story of Fish (Nemo) lost in the sea and finding his way out connect with his dad again.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

#"import fresh_tomatoes" allows to turn this code into a movie website by using function "open_movies_page"  
#The "open_movies_page" function takes a list or array of movies, then outputs or creates and opens
#an html webpage or website that shows those movies
movies = [toy_story,avatar,finding_nemo]
fresh_tomatoes.open_movies_page(movies)
