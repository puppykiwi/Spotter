# Spotify Terminal Player

This is a simple Python script that allows you to control Spotify playback from the terminal using Spotify's Web API.

## Features

- Play, pause, skip, and adjust volume of Spotify tracks.
- Display currently playing track information.
- Search for tracks and play them.

## Prerequisites

Before running the script, you need to set up a Spotify Developer account and obtain your Client ID and Client Secret. You also need to register a Redirect URI for your application.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/puppykiwi/Terminal-player.git
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Set up your Spotify Developer account and obtain your Client ID and Client Secret.

4. Configure the script with your Client ID, Client Secret, and Redirect URI.

## Usage

1. Run the script:

    ```
    python spotify_player.py
    ```

2. Follow the instructions to authenticate with Spotify.

3. Once authenticated, you can use the following commands:

    - `play`: Resume playback.
    - `pause`: Pause playback.
    - `next`: Skip to the next track.
    - `prev`: Return to the previous track.
    - `search <query>`: Search for tracks by `query` and play the selected track.
    - `volume <level>`: Adjust the volume level (0-100).
    - `info`: Display information about the currently playing track.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.
