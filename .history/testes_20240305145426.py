#
# 
# This is a small demonstration of how to use an api
# Here I used the IMDb Api from Rapid Api this is where you get an api key
# https://rapidapi.com/apidojo/api/imdb8/
# This program fetches movies associated with a search term and prints their 
# movie title and cover image url
#
# 1/27/2022 - Drayton Lavender
# Feel free to use this code however you like!
#

import requests
import json

# Base url that connects us to the server where the movie info is located
url = "https://imdb8.p.rapidapi.com/auto-complete"

# These headers are used to authenticate your connection
headers = {
	"X-RapidAPI-Key": "40d79ce6f4msh6893b4dcc8e3457p188914jsn0bb67db95879",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

# These are my keywords I'd like to search for
searchTerms = ["la la land", "the handmaiden", "scream", "poor things"]

# I store all the responses in a list
responses = []

# Here I loop through the search terms
for x in range(len(searchTerms)):
  # Update the searchterm in the url parameters
  querystring = {"q": searchTerms[x]}

  # Query the API and save the result
  response = requests.request("GET", url, headers=headers, params=querystring)

  # Turn the json text from the response into a useful json python object
  data = json.loads(response.text)

  # Format the json to be more readable this is mostly for viewing raw
  # response data when debugging
  formattedData = json.dumps(data, indent=4)
  # Uncomment the following line to see the raw response from the api
  # print(formattedData)

  # Load the json data into a dictionary
  dataDict = json.loads(formattedData)

  # Save the most important data in our list
  responses.append(dataDict["d"])

# Print out the results
for x in range(len(searchTerms)):
  print("\n\nSearch Term: \"" + str(searchTerms[x]) + "\"")
  for movie in responses[x]:
    print(movie)
    # I used try/except here to keep going just incase a movie doesn't have
    # the data I'm asking for. 
    try:
      print("Title: " + movie["l"])
      print("Image: " + movie["i"]["imageUrl"])
      print("Year: " + movie["y"])
      
    except:
      pass

