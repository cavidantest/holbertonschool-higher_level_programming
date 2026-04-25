import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get('title'))
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            
            # Structure data into a list of dictionaries with specific keys
            data_to_save = [
                {
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                }
                for post in posts
            ]
            
            # Write data to posts.csv
            filename = "posts.csv"
            fieldnames = ['id', 'title', 'body']
            
            with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_to_save)
    except Exception as e:
        print(f"An error occurred: {e}")
