import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS



def textToSpeech(text,filename):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext,lang=language,slow = False)

    

# This function returns pydub audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined  += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.MP3')
    #Generate kripya dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.MP3",format = "MP3")

    # 2 is from city

    # 3 se chalkar

    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.MP3",format="MP3")
     
    # 4 is via city


    # 5 ke raste 
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.MP3",format = "MP3")

    #6 is to city

    #Generate ko jaane wali gaadi sakhiya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.MP3",format = "MP3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mein platform sakhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.MP3",format = "MP3")
    
    #10 is platform number

    # 11 Generate par aa rahi hai

    start = 109000
    finish = 112250 
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.MP3",format = "MP3")
  
def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        pass
        # 2 - Generate from City
        textToSpeech(item["from"],"2_hindi.MP3")
        # 4 - Generate via City
        textToSpeech(item["via"],"4_hindi.MP3")

        # 6 - Generate to City
        textToSpeech(item["to"],"6_hindi.MP3")

        # 8 - Generate train no and name
        textToSpeech(item["train_no"] + " " + item["train_name"],"8_hindi.MP3")

        # 10 - Generate platform number
        textToSpeech(item["platform"],"10_hindi.MP3")

        audios = [f"{i}_hindi.MP3" for i in range(1,12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_new{index+1}.MP3",format = "MP3")





if __name__ == "__main__" :
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now Generating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")
