#!/bin/bash
import nicol_speech
import time

nicol_talker = nicol_speech.NICOL_TALKER()

talker_keys = nicol_talker.synthesizer.tts_model.speaker_manager.ids.keys()

import sox
tfm0 = sox.Transformer()
tfm1 = sox.Transformer()
tfm1.pitch(-3)
tfm2 = sox.Transformer()
tfm2.tempo(0.8)

variations =[('A',tfm0),('B',tfm1),('C',tfm2)]
from pydub import AudioSegment

all_together = AudioSegment.empty()
for talker_key in talker_keys:
    for variation in variations:
        subspeaker,tfm=variation
        nicol_talker.synth("I am speaker number "+ str(talker_key)+ " "+subspeaker+". . Hello, I am the NICOL robot. Does the voice fit to me?","./temp.wav",speaker_idx=talker_key)

        status = tfm.build(
            input_filepath='./temp.wav',
            output_filepath=subspeaker+'.wav'
        )
    from pydub import AudioSegment

    sounds = [
        AudioSegment.from_wav('A.wav'),
        AudioSegment.from_wav('B.wav'),
        AudioSegment.from_wav('C.wav'),
    ]

    all_subspeakers = AudioSegment.empty()
    for sound in sounds:
        all_subspeakers += sound
    #all_subspeakers.export("./temp.wav", format="wav")
    all_together +=all_subspeakers
    #nicol_talker.play("./temp.wav")

all_together.export("./complete_NICOL_speech_evaluation.wav", format="wav")

time.sleep(1)

#nicol_talker.synth("I am a humanoid robot.","./temp.wav")
#nicol_talker.play("./temp.wav")
#232
#253
#258
#267
#487