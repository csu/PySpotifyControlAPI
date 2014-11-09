PySpotifyControlAPI
================

A Flask app that uses [PySpotifyControl](https://github.com/csu/PySpotifyControl) to allow users to control a Spotify desktop client through a REST API and front end web interface.

## Features
* Can scrobble plays to the Last.fm accounts of all listeners (using [PyMultiScrobble](https://github.com/csu/PyMultiScrobble))
* Speech control (using [PySpotifySpeechControl](https://github.com/csu/PySpotifySpeechControl))
* API endpoints for playing a specific song, play/pause, volume up/down, next/previous song, and getting the current song's name and artist.

## Requirements
* Mac OS X
* Spotify for Mac

## Installation

    git clone https://github.com/csu/PySpotifyControlAPI.git
    cd PySpotifyControlAPI
    pip install -r requirements.txt
    python server.py

## Contributing
Pull requests are welcome. Submit feature requests and bugs through GitHub issues.
