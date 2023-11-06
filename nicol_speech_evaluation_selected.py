#!/bin/bash
import nicol_speech
import time

nicol_talker = nicol_speech.NICOL_TALKER()

talker_keys = nicol_talker.synthesizer.tts_model.speaker_manager.ids.keys()


import sox
tfm0 = sox.Transformer()
tfm1 = sox.Transformer()
tfm1.pitch(1.0)
tfm2 = sox.Transformer()
tfm2.tempo(0.9)

variations =[('A',tfm0),('B',tfm1),('C',tfm2)]
#p246
#p248
#p250(very fast)
#p263
#p268
#p270 (!)
#p276
#p293
#p304
#p305 ( very high )
#p336


#268B

#talkers = [('p243',False,False),('p258',False,False),('p277',True,False),('p232',True,False),('p246',False,True),('p267',False,False)]
talkers = [('p243',True,False),('p336',True,False),('p250',False,True), \
                ('p270',True,False),('p305',True,False),('p293',True,False),('ttsx3',True,True)]

from pydub import AudioSegment

all_together = AudioSegment.empty()
#for talker_key in talker_keys:
for t,talker in enumerate(talkers):
    t_number,ef1,ef2 = talker

    print ("processing: " + str(t_number))

    t1 = "I am the NICO L robot. " 


    def process_speech(t,ef1,tfm1,ef2,tfm2,ti):

        if t_number == 'ttsx3':
            
            import pyttsx3
            engine = pyttsx3.init() # object creation
            engine.setProperty('rate', 125)
            engine.stop()
            engine.save_to_file(t, './temp.wav')
            engine.runAndWait()
            time.sleep(2)

        else:            
            nicol_talker.synth(t,"./temp.wav",speaker_idx=t_number)

        if ef1:
            status = tfm1.build(
                input_filepath='./temp.wav',
                output_filepath='./temp_1.wav'
            )
            import shutil
            shutil.copy2('./temp_1.wav', './temp.wav')


        if ef2:
            status = tfm2.build(
                input_filepath='./temp.wav',
                output_filepath='./temp_1.wav'
            )
            import shutil
            shutil.copy2('./temp_1.wav', './temp.wav')


        temp = AudioSegment.from_file("./temp.wav", format="wav")

        t_dur = len(temp)

        silence = AudioSegment.silent(duration=ti-t_dur)

        return(temp+silence)

    # Part two
    all_together = process_speech(t1,ef1,tfm1,ef2,tfm2,2000)

    t2 = "Sometimes I smile. " 

    all_together += process_speech(t2,ef1,tfm1,ef2,tfm2,3000)

    t3 = "When something goes, wrong I look sad. " 

    all_together += process_speech(t3,ef1,tfm1,ef2,tfm2,4000)

    t4 = "And I can even look angry. " 

    all_together += process_speech(t4,ef1,tfm1,ef2,tfm2,4000)


    '''
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
    '''

    all_together.export("../../moviepy/nicol_speech_2/v2_speaker_number_"+str(t)+".aac", format="adts")

time.sleep(1)

#nicol_talker.synth("I am a humanoid robot.","./temp.wav")
#nicol_talker.play("./temp.wav")

#p242
#p243

#232
#253
#258
#267
#487