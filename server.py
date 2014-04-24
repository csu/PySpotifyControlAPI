#!/usr/bin/env python
from flask import Flask, jsonify, request, url_for, redirect
from pyspotifycontrol import spotify_control
# from spotifyqueue import SpotifyQueue
from multiprocessing import Process, Queue
import time
import urllib2
import json

app = Flask(__name__)

#### POST routes ####

@app.route('/queue', methods=['POST'])
def addToQueue():
    try:
        queue.put([request.form['track_uri'], request.form['duration']])
        return jsonify({'added':{'track_uri': request.form['track_uri'], 'duration': request.form['duration']}})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play', methods=['POST'])
def playTrackPost():
    try:
        print request.form
        if 'track_uri' in request.form:
            spotify_control.playTrack(request.form['track_uri'])
        elif 'track_search' in request.form:
            response = urllib2.urlopen('http://ws.spotify.com/search/1/track.json?q=' + request.form['track_search'].replace (" ", "+"))
            data = json.load(response)
            spotify_control.playTrack(data["tracks"][0]["href"])
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

@app.route('/', methods=['GET'])
def serveIndex():
    try:
        return app.send_static_file('index.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play/<track_uri>', methods=['GET'])
def playTrack(track_uri):
    try:
        spotify_control.playTrack(track_uri)
        return jsonify({'status':'success'})
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play/search/<track_search>', methods=['GET'])
def playSearchTrack(track_search):
    try:
        response = urllib2.urlopen('http://ws.spotify.com/search/1/track.json?q=' + track_search.replace (" ", "+"))
        data = json.load(response)
        spotify_control.playTrack(data["tracks"][0]["href"])
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

# @app.route('/', methods=['GET'])
# def index():
#     programInfo = dict()
#     programInfo['author'] = 'Christopher Su'
#     programInfo['author_url'] = 'http://christophersu.net/'
#     programInfo['name'] = 'PySpotifyControl'
#     programInfo['version'] = '0.0.1'
#     programInfo['project_url'] = 'http://github.com/csu'
#     programInfo['source_url'] = 'http://github.com/csu/PySpotifyControl/'
#     programInfo['description'] = 'A REST API for controlling Spotify.'
#     return jsonify(programInfo)

def runQueue(queue):
    while True:
        if queue.empty():
            time.sleep(3) # keep checking until the queue isn't empty
        else:
            nextSong = queue.get()
            spotify_control.playTrack(nextSong[0])
            time.sleep(float(nextSong[1]))

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=runQueue, args=(queue,))
    p.start()
    app.run(host='0.0.0.0', debug=True)
    p.join()