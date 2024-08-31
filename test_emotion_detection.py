import unittest
from EmotionDetection.emotion_detection import emotion_detector 

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Creating various test cases to verify
        emotion = emotion_detector("I am glad this happened")
        self.assertEqual(emotion['dominant_emotion'], "joy")
        # case2
        emotion2 = emotion_detector("I am really mad about this")
        self.assertEqual(emotion2['dominant_emotion'], "anger")
        # case3
        emotion3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion3['dominant_emotion'], "disgust")
        # case4
        emotion4 = emotion_detector("I am so sad about this")
        self.assertEqual(emotion4['dominant_emotion'], "sadness")
        # case5
        emotion5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion5['dominant_emotion'], "fear")
# running test cases
unittest.main()


