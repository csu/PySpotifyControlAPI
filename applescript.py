#!/usr/bin/python
import subprocess

def run(ascript):
  osa = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  return osa.communicate(ascript)[0]