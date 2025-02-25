# Steam Workshop Downloader

This script allows you to download multiple items from a Steam Workshop collection using `steamcmd`. It retrieves the Workshop item IDs from a specified collection page and executes `steamcmd` commands to download them.

## Features

- Scrapes the Steam Workshop page to gather item IDs.
- Allows downloading of up to 150 Workshop items at a time in one `steamcmd` command (configurable).
- Automatically checks if `steamcmd` is installed and asks the user for the path if not found.

## Requirements

- Python 3.x
- `requests` and `beautifulsoup4` libraries (can be installed via `pip install requests beautifulsoup4`)
- `steamcmd` (Steam Command Line tool)

## Usage

1. Clone this repository or download the script.

2. Install the required dependencies:

    ```bash
    pip install requests beautifulsoup4
    ```

3. Run the script:

    ```bash
    python workshop_downloader.py
    ```

4. Provide the Steam Workshop collection URL when prompted.

5. If `steamcmd` is not found in your PATH, you will be asked to provide the full path to `steamcmd`.
