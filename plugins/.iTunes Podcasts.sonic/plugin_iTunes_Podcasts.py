import requests

def search_podcasts(search_query):
    url = f"https://itunes.apple.com/search?entity=podcast&term={search_query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        podcasts = data.get('results', [])
        return podcasts
    else:
        print("Error searching for podcasts.")
        return []

def display_podcasts(podcasts):
    for i, podcast in enumerate(podcasts):
        print(f"{i + 1}. {podcast['artistName']} - {podcast['collectionName']}")

def download_podcast(podcasts, choice):
    if 1 <= choice <= len(podcasts):
        selected_podcast = podcasts[choice - 1]
        print(f"Downloading '{selected_podcast['collectionName']}'...")
        # Add your download logic here
    else:
        print("Invalid choice. Please select a valid podcast.")

while True:
    search_query = input("Enter a podcast search term (or 'exit' to quit): ")
    if search_query.lower() == "exit":
        break

    podcasts = search_podcasts(search_query)

    if podcasts:
        print("Top 10 podcasts found:")
        display_podcasts(podcasts[:10])

        try:
            choice = int(input("Enter the number of the podcast you want to download (11 to search again): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 11:
            continue
        else:
            download_podcast(podcasts, choice)
    else:
        print("No podcasts found for the search term.")

print("Exiting the program.")