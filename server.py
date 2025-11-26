''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created: TODO
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions labels in a list from the response
    list_response_keys = list(response.keys())
    
    # Check if at least one emotion is None, indicating an error or invalid input
    if response['anger'] is None:
        return "Invalid input! Try again."
    else:
        #initialize the formatted string
        formatted_string = "For the given statement, the system response is "
        i = 0
        n = len(list_response_keys) - 1
        while i < n:
            formatted_string = formatted_string + "'" + list_response_keys[i] +"'" + ": " + str(response[list_response_keys[i]]) + ", "
            i = i + 1 
        
        #adding the dominant emotion
        formatted_string = formatted_string + "The dominant emotion is " + response[list_response_keys[n]]
        
        # Return a formatted string with the emotion label and  score
        return formatted_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run(host="0.0.0.0", port=5000)
