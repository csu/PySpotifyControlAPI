#!/usr/bin/env python
from flask import Flask, jsonify, request
from pyspotifycontrol import spotify_control

app = Flask(__name__)

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

#### POST routes ####

@app.route('/play', methods=['POST'])
def playTrackPost():
    try:
        spotify_control.playTrack(request.form['track_uri'])
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/setVolume', methods=['POST'])
def setVolumePost():
    try:
        spotify_control.setVolume(request.form['volume'])
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/jumpTo', methods=['POST'])
def jumpToPost(position):
    try:
        spotify_control.jumpTo(request.form['position'])
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

#### GET routes ####

@app.route('/play/<track_uri>', methods=['GET'])
def playTrack(track_uri):
    try:
        spotify_control.playTrack(track_uri)
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/playpause', methods=['GET'])
def playpause():
    try:
        spotify_control.playPause()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play', methods=['GET'])
def play():
    try:
        spotify_control.play()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/pause', methods=['GET'])
def pause():
    try:
        spotify_control.pause()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/next', methods=['GET'])
def next():
    try:
        spotify_control.next()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/previous', methods=['GET'])
def previous():
    try:
        spotify_control.previous()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/volumeUp', methods=['GET'])
def volumeUp():
    try:
        spotify_control.volumeUp()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/volumeDown', methods=['GET'])
def volumeDown():
    try:
        spotify_control.volumeDown()
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/setVolume/<volume>', methods=['GET'])
def setVolume(volume):
    try:
        spotify_control.setVolume(volume)
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/jumpTo/<position>', methods=['GET'])
def jumpTo(position):
    try:
        spotify_control.jumpTo(position)
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

if __name__ == '__main__':
    app.run(debug=True)