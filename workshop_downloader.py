import os
import requests
from bs4 import BeautifulSoup

# URL of the Steam page
url = input("Steam Workshop URL: ")

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the game ID (from the 'data-appid' attribute)
    game_store_hyperlink = soup.find('a', class_='btnv6_blue_hoverfade btn_medium')
    if game_store_hyperlink: 
        game_id = game_store_hyperlink.get('data-appid')
    else: 
        game_id = None

    # Initialize list for Workshop item IDs
    workshop_item_id_list = []

    # Extract Workshop item IDs from the collection
    for workshop_item in soup.find_all('div', class_='collectionItemDetails'):
        # Find the <a> tag inside each item and get the href attribute
        href = workshop_item.find('a', href=True)
        if href:
            # Extract the ID from the URL
            workshop_item_id = href['href'].split('=')[-1]
            workshop_item_id_list.append(workshop_item_id)

    # Print the results
    print(f"Game ID: {game_id}")
    print(f"Workshop Size: {len(workshop_item_id_list)}")

    # Check if steamcmd is in PATH
    steamcmd_path = "steamcmd"
    if not os.system("steamcmd --version") == 0:  # Check if steamcmd is accessible
        # SteamCMD is not recognized, ask user for the path
        steamcmd_path = input("SteamCMD is not found. Please enter the full path to your steamcmd (e.g., C:\\SteamCMD\\steamcmd.exe): ")

    # Maximum items per command
    max_items_per_command = 150
    command = f'"{steamcmd_path}" +login anonymous'

    # Iterate through the workshop item list in chunks of max_items_per_command
    for i in range(0, len(workshop_item_id_list), max_items_per_command):
        # Slice the list to get the next batch of items
        batch = workshop_item_id_list[i:i+max_items_per_command]

        # Append each workshop download item command for the current batch
        for workshop_id in batch:
            command += f" +workshop_download_item {game_id} {workshop_id}"

        # Append the quit command to end the session
        command += " +quit"

        # Execute the command for the current batch
        os.system(command)

        # Clear the command for the next batch
        command = f'"{steamcmd_path}" +login anonymous'
