# Created by Charles
# April 11, 2017

# Imports
from flask import jsonify
import RPi.GPIO as GPIO

# Class to represent a GPIO
# output pin on the Rapsberry PI
class Group:

    # Constructor
    def __init__(self, id, outputs, info):
       self.id = id
       self.outputs = outputs
       self.info = info
       self.state = False

    # Toggles the pins voltage
    def toggle(self):
        for output in self.outputs:
            output.toggle()

    # Returns a dictionnary of the object infomations
    def toDict(self):
        rtrn = []
        for output in self.outputs:
            rtrn.append(output.toDict())
        return {'id' : self.id, 'outputs' : rtrn, 'info' : self.info, 'state' : self.state}

    # Returns a JSON of the object informations
    def toJSON(self):
        return jsonify(self.toDict())
