#!/bin/bash
import nicol_speech
import time

nicol_talker = nicol_speech.NICOL_TALKER()

nicol_talker.synth("Hello, I am the NICOL robot.","./temp.wav")
nicol_talker.play("./temp.wav")

time.sleep(1)

nicol_talker.synth("I am a humanoid robot.","./temp.wav")
nicol_talker.play("./temp.wav")
