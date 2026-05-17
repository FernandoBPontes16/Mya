import random

words = {
    'feliz': ('happiness',0.6,1.0),
}

boost_words = {
    'muito': 1.5,
    'bastante': 1.2
}

negative_words = {
    'nao',
    'nunca',
    'jamais'    
}

emotions = {
    'happiness': 0.0,
    'sadness': 0.0,
    'angry': 0.0,
    'embarrassed': 0.0,
    'fear': 0.0,
    'disgust': 0.0,
    'surprise': 0.0,
    'neutral': 0.0
}

status = {
    'happiness': 'neutro',
    'sadness': 'neutro',
    'angry': 'neutro',
    'embarrassed': 'neutro',
    'fear': 'neutro',
    'disgust': 'neutro',
    'surprise': 'neutro',
    'neutral': 'neutro'
}

def clamp(value):
    return max(-3, min(3, value))

def verify(question):
    question = question.lower().split()

    multiplier = 1.0
    negative = False

    for word in question:

        if word in boost_words:
            multiplier *= boost_words[word]
            continue

        if word in negative_words:
            negative = True
            continue

        if word in words:

            emotion, min_value, max_value = words[word]
            value = random.uniform(min_value, max_value)

            if negative == True:
                multiplier = -1

            value *= multiplier

            emotions[emotion] += value

            emotions[emotion] = clamp(emotions[emotion])

            multiplier = 1.0
            negative = False
    return emotions

def emotion_level():
    for emotion in emotions:
        if -3 <= emotions[emotion] < -2:
            status[emotion] = 'never'
        elif -2 <= emotions[emotion] < 0:
            status[emotion] = 'low'
        elif 0 <= emotions[emotion] < 1:
            status[emotion] = 'neutral'
        elif 1 <= emotions[emotion] < 2:
            status[emotion] = 'high'
        elif 2 <= emotions[emotion] <= 3:
            status[emotion] = 'very'     
    return(status)
        
def losing_emotions():
    for emotion in emotions:
        emotions[emotion] *= 0.90