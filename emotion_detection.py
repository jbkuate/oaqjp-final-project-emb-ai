import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the anger, disgust, fear, joy and sadness from the response
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        anger_score = none
        disgust_score = none
        fear_score = none
        joy_score = none
        sadness_score = none
    
    #list of emotions names
    emotion_names = {'0':'anger', '1':'disgust', '2':'fear', '3':'joy', '4':'sadness'}
    
    #list of emotions scores
    emotion_scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]

    #get the dominant emotion score
    dominant_emotion_score = max(emotion_scores)
    #get the index of the dominant emotion score
    index_dominant_emotion = emotion_scores.index(dominant_emotion_score)
    #get the name of dominant emotion name
    dominant_emotion_name = emotion_names[str(index_dominant_emotion)]
    
    #define the response of the function
    dict_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_name
    }

    # Return the emotion detection and dominant emotion in a dictionary
    return dict_response