#!/usr/bin/env python
from flask import Flask, render_template, jsonify, request, url_for, redirect
from PySpotifyControl import spotify_control
# from spotifyqueue import SpotifyQueue

# # For queue:
# from multiprocessing import Process, Queue

# For multiscrobbling:
from PyMultiScrobble import MultiScrobbler

import time
import urllib2
import json

app = Flask(__name__)

#### Helpers ####
def searchPlay(query):
    response = urllib2.urlopen('http://ws.spotify.com/search/1/track.json?q=' + query.replace (" ", "+"))
    data = json.load(response)
    playTrackHelper(data["tracks"][0]["href"])

def playTrackHelper(uri):
    spotify_control.playTrack(uri)
    time.sleep(2) # give spotify some time to respond to the applescript
    multiscrobbler.scrobbleAll(spotify_control.getSongArtist(), spotify_control.getSongName())
    ## safer version (don't have to comment out method when multiscrobbler is disabled)
    # if multiscrobbler is not None:
    #     # time.sleep(2) # give spotify some time to respond to the applescript?
    #     print spotify_control.getSongArtist() + ' - ' + spotify_control.getSongName()
    #     multiscrobbler.scrobbleAll(spotify_control.getSongArtist(), spotify_control.getSongName())

# def runQueue(queue):
#     while True:
#         if queue.empty():
#             time.sleep(3) # keep checking until the queue isn't empty
#         else:
#             nextSong = queue.get()
#             playTrackHelper(nextSong[0])
#             time.sleep(float(nextSong[1]))

#### Multiscrobbler routes ####
@app.route('/multiscrobble/account', methods=['POST'])
def addAccountToMultiScrobbler():
    multiscrobbler.addAccount(request.form['username'], request.form['password'])
    return app.send_static_file('redirect.html')

#### POST routes ####

# @app.route('/queue', methods=['POST'])
# def addToQueue():
#     try:
#         queue.put([request.form['track_uri'], request.form['duration']])
#         return jsonify({'added':{'track_uri': request.form['track_uri'], 'duration': request.form['duration']}})
#     except:
#         return jsonify({'error':'Invalid request'})

@app.route('/play', methods=['POST'])
def playTrackPost():
    try:
        # print request.form
        if 'track_uri' in request.form:
            playTrackHelper(request.form['track_uri'])
        elif 'track_search' in request.form:
            searchPlay(request.form['track_search'])
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/setVolume', methods=['POST'])
def setVolumePost():
    try:
        spotify_control.setVolume(request.form['volume'])
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/jumpTo', methods=['POST'])
def jumpToPost(position):
    try:
        spotify_control.jumpTo(request.form['position'])
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

#### GET routes ####

@app.route('/', methods=['GET'])
def serveIndex():
    try:
        return render_template('search.html', songName=spotify_control.getSongName().decode('utf-8'), songArtist=spotify_control.getSongArtist().decode('utf-8'), songURI=spotify_control.getSongId().decode('utf-8'))
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play/<track_uri>', methods=['GET'])
def playTrackGet(track_uri):
    try:
        playTrackHelper(track_uri)
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play/search/<track_search>', methods=['GET'])
def playSearchTrack(track_search):
    try:
        searchPlay(track_search)
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/playpause', methods=['GET'])
def playpause():
    try:
        spotify_control.playPause()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/play', methods=['GET'])
def play():
    try:
        spotify_control.play()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/pause', methods=['GET'])
def pause():
    try:
        spotify_control.pause()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/next', methods=['GET'])
def next():
    try:
        spotify_control.next()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/previous', methods=['GET'])
def previous():
    try:
        spotify_control.previous()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/volumeUp', methods=['GET'])
def volumeUp():
    try:
        spotify_control.volumeUp()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/volumeDown', methods=['GET'])
def volumeDown():
    try:
        spotify_control.volumeDown()
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/setVolume/<volume>', methods=['GET'])
def setVolume(volume):
    try:
        spotify_control.setVolume(volume)
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

@app.route('/jumpTo/<position>', methods=['GET'])
def jumpTo(position):
    try:
        spotify_control.jumpTo(position)
        return app.send_static_file('redirect.html')
    except:
        return jsonify({'error':'Invalid request'})

if __name__ == '__main__':
    # # For queue:
    # queue = Queue()
    # p = Process(target=runQueue, args=(queue,))
    # p.start()

    # For multiscrobbling:
    multiscrobbler = MultiScrobbler()

    app.run(host='0.0.0.0', debug=True)

    # # For queue:
    # p.join()