'''
Flask app that detects emotion of th input text provided in html template
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("This is an Emotion detection application")

@app.route("/emotionDetector")
def emotions():
    '''Detects emotion of the input text and returns output according to it'''
    text_to_analyze = request.args.get('textToAnalyze')
    # if text_to_analyze == "":
    #     return "Input is blank! Try providing proper input"
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    message = "For the given statement, the system response is "
    for emotion, score in res.items():
        message = message + emotion + ": " + str(score) + ", "
    # in the end adding most dominant emotion
    message = message + f"The most dominant emotion is {res['dominant_emotion']}"
    return message

@app.route("/")
def get_html():
    '''Returns basic html interface when app is opened(i.e. Get request)'''
    return render_template("index.html")

# run the flask app
app.run(port = 5000)
