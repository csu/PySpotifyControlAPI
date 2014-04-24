from multiprocessing import Queue
import time
from pyspotifycontrol import spotify_control

class SpotifyQueue(object):
    def __init__(self):
        self.queue = Queue()

    def getNext(self):
        return self.queue.get()

    def addSong(self, song_uri, song_duration):
        self.queue.put([song_uri, song_duration])

    def runQueue(self):
        while True:
            if self.queue.empty():
                time.sleep(3) # keep checking until the queue isn't empty
            else:
                nextSong = getNext()
                spotify_control.playTrack(nextSong[0])
                time.sleep(float(nextSong[1]))