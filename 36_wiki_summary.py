''' Challenge: Wikipedia API

Objective: Demonstrate the installation and usage of third-party packages via PIP to fetch and summarize real-world data from the Wikipedia API. '''

pip3 install wikipedia

import wikipedia  # Import the wikipedia package

# Search for a topic
search_term = "Python (programming language)"  # You can change this to anything
# Fetching summary
summary = wikipedia.summary(search_term, sentences=3)
print(summary)

