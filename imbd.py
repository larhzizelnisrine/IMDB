import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the IMDb webpage
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the movie titles and ratings
movies = soup.select('td.titleColumn')
titles = []
ratings = []

# Extract the titles and ratings, handling cases where ratings are missing
for movie in movies:
    title = movie.find('a').text
    titles.append(title)

    rating_element = movie.find('strong')
    rating = float(rating_element.text) if rating_element else None
    ratings.append(rating)

# Print the top 10 movies
for i in range(10):
    print(f'{i + 1}. {titles[i]} ({ratings[i]})')

import plotly.express as px
import pandas as pd
# Create a DataFrame with the scraped data
data = {'Movie': titles, 'Rating': ratings}
df = pd.DataFrame(data)

# Create a bar chart using Plotly Express
fig = px.bar(df, x='Movie', y='Rating', title='Top 10 Movies on IMDb',
             labels={'Movie': 'Movie Title', 'Rating': 'Rating'})

# Display the chart
fig.show()



