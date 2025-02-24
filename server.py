"""
Flask application for emotion detection using Watson NLP.

This module provides a web interface for analyzing the emotions in a given text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the emotion of the provided text and return the result.

    Returns:
        str: A formatted string containing the emotion scores and dominant emotion.
             If the input text is invalid, returns an error message.
    """
    # Get the text to analyze from the query parameter
    text_to_analyze = request.args.get('text')

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result contains an error
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response

@app.route('/')
def index():
    """
    Render the index.html file.

    Returns:
        str: The rendered HTML content of the index page.
    """
    # Render the index.html file
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
