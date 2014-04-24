from pyspotifycontrol import spotify_control
from multiprocessing import Process, Queue
import time

def runQueue(queue):
    while True:
        if queue.empty():
            time.sleep(3) # keep checking until the queue isn't empty
        else:
            nextSong = queue.get()
            spotify_control.playTrack(nextSong[0])
            time.sleep(float(nextSong[1]))

queue = Queue()
p = Process(target=runQueue, args=(queue,))
p.start()

queue.put(['spotify:track:5ZrrXIYTvjXPKVQMjqaumR', '227'])
queue.put(['spotify:track:2GAIycsMaDVtMtdvxzR2xI', '354'])