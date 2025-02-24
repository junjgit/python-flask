import requests
import json

import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send a POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response text into a dictionary
        response_dict = response.json()
        
        # Extract the emotion scores
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format the output
        formatted_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        # Return the formatted output
        return formatted_output
    elif response.status_code == 400:
        # Return a dictionary with all values set to None for blank entries
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Return an error message if the request fails
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }