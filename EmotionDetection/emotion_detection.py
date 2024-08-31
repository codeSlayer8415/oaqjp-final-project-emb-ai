import requests
import json

def dominant_emotion(emotions):
    dominant = ""
    dom_score = -10
    for emotion, score in emotions.items():
        if score > dom_score:
            dominant = emotion
            dom_score = score
    return dominant



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Sending post request to AI model
    response = requests.post(url, json = myobj, headers = header)
    # converting response.text to dict format
    res = json.loads(response.text)
    # the following returns list of emotions in dictionary format
    emotions = res["emotionPredictions"][0]["emotion"]
    #now find the dominant emotion and add dominant emotion to dict
    dominant = dominant_emotion(emotions)
    emotions['dominant_emotion'] = dominant
    return emotions
