#!/usr/bin/env python
from flask import Flask, jsonify
import applescript

app = Flask(__name__)

def playTrack(track_uri):
    applescript.run('tell application "Spotify" to play track "' + track_uri + '"')

@app.route('/', methods=['GET'])
def index():
    programInfo = dict()
    programInfo['author'] = 'Christopher Su'
    programInfo['author_url'] = 'http://christophersu.net/'
    programInfo['name'] = 'PySpotifyControl'
    programInfo['version'] = '0.0.1'
    programInfo['project_url'] = 'http://github.com/csu'
    programInfo['source_url'] = 'http://github.com/csu/PySpotifyControl/'
    programInfo['description'] = 'A REST API for controlling Spotify.'
    return jsonify(programInfo)

@app.route('/play/<track_uri>', methods=['GET'])
def getIdea(track_uri):
    try:
        playTrack(track_uri)
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

if __name__ == '__main__':
    app.run(debug=True)