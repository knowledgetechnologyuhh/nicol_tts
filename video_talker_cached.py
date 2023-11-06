
import nicol_speech
import time
from pydub import AudioSegment
import sox

nicol_talker = nicol_speech.NICOL_TALKER()

talker_keys = nicol_talker.synthesizer.tts_model.speaker_manager.ids.keys()



tfm0 = sox.Transformer()
tfm1 = sox.Transformer()
tfm1.pitch(1.0)
tfm2 = sox.Transformer()
tfm2.tempo(0.9)

variations =[('A',tfm0),('B',tfm1),('C',tfm2)]
#talkers = [('p243',False,False),('p258',False,False),('p277',True,False),('p232',True,False),('p246',False,True),('p267',False,False)]
talkers = [('p243',True,False),('p336',True,True),('p250',False,True), \
                ('p270',True,True),('p305',True,False),('p293',True,False),('ttsx3',True,True)]
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

use_cache = True

texts = ["Hi, Nico!",
        "Yes",
        "No",
        "Yes, I agree",
        "No, I do not think so",
        "OK, Let me see!",
        "I know about the concept of colors. I see two yellow objects and one red object. I think "+
        "you ask me to put the object in the middle or on my left to the box, right ?!",
        "OK, the color is the same for both objects. As another attribute " +
        "you named softness. I have to check the red objects for this attribute!",
        "I know about the concept of softness. I think only the object in " +
        "the middle is soft. So I will put the object in the middle in the box." +
        "Is that right?",
        "Is this the right object?!",
        "Oh, there are some objects on my table!",
        "I think the red object is a tomato!",
]

talker = talkers[1]

def input_for_text():
    for t, text in enumerate(texts):
        print ("\n (" + str(t) + ") " + text)

    v_input = input("\n\nWhich text should be played? Please input number and return. \n\n")
    print("\n OK. Playing number " + str(v_input))
    return(v_input)

def process_speech(t,ef1,tfm1,ef2,tfm2,ti):

    if t_number == 'ttsx3':
        
        import pyttsx3
        engine = pyttsx3.init() # object creation
        engine.setProperty('rate', 125)
        engine.stop()
        engine.save_to_file(t, './temp.wav')
        engine.runAndWait()
        #engine.close()
        time.sleep(2)

    else: 
        print ("using: " + t_number)           
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

    if ti != 0:
        silence = AudioSegment.silent(duration=ti-t_dur)
        temp = temp + silence

    return(temp)


t_number,ef1,ef2 = talker
if use_cache:
    
    for c,text in enumerate(texts):
        
        print ("Caching: " + text)
    
        # Part two
        all_together = process_speech(text,ef1,tfm1,ef2,tfm2,0)
        all_together.export("./talker_cache/"+str(c)+".wav", format="wav")

from pydub import AudioSegment

all_together = AudioSegment.empty()
#for talker_key in talker_keys:
#for t,talker in enumerate(talkers):
v_input = 0

while v_input != -1:

    number_to_speak = input_for_text()

    print ("processing: " + str(number_to_speak))

    nicol_talker.play("./talker_cache/"+str(number_to_speak)+".wav")
