import random

words = {
    'feliz': ('happiness', 0.6, 1.0),
    'contente': ('happiness', 0.4, 0.8),
    'alegre': ('happiness', 0.5, 0.9),
    'otimista': ('happiness', 0.4, 0.7),
    'radiante': ('happiness', 0.7, 1.0),
    'maravilhoso': ('happiness', 0.8, 1.0),
    ' rir': ('happiness', 0.6, 0.9),
    'gratidão': ('happiness', 0.5, 0.8),

    'morte': ('sadness', 0.8, 1.0),
    'triste': ('sadness', 0.5, 0.8),
    'chorar': ('sadness', 0.6, 0.9),
    'deprimido': ('sadness', 0.8, 1.0),
    'solitário': ('sadness', 0.5, 0.8),
    'luto': ('sadness', 0.9, 1.0),
    'desanimado': ('sadness', 0.3, 0.6),
    'pena': ('sadness', 0.4, 0.7),

    'raiva': ('angry', 0.6, 0.9),
    'fúria': ('angry', 0.8, 1.0),
    'ódio': ('angry', 0.8, 1.0),
    'irritado': ('angry', 0.3, 0.6),
    'bravo': ('angry', 0.4, 0.7),
    'odiar': ('angry', 0.7, 0.9),
    'gritar': ('angry', 0.5, 0.8),
    'incomodado': ('angry', 0.2, 0.5),

    'vergonha': ('embarrassed', 0.6, 0.9),
    'tímido': ('embarrassed', 0.3, 0.6),
    'constrangido': ('embarrassed', 0.5, 0.8),
    'humilhado': ('embarrassed', 0.8, 1.0),
    'corar': ('embarrassed', 0.4, 0.7),
    'vacilo': ('embarrassed', 0.3, 0.5),

    'medo': ('fear', 0.5, 0.8),
    'terror': ('fear', 0.8, 1.0),
    'pânico': ('fear', 0.8, 1.0),
    'assustado': ('fear', 0.4, 0.7),
    'ansioso': ('fear', 0.4, 0.6),
    'perigo': ('fear', 0.6, 0.9),
    'pesadelo': ('fear', 0.5, 0.8),

    'nojo': ('disgusted', 0.6, 0.9),
    'repulsa': ('disgusted', 0.7, 1.0),
    'podre': ('disgusted', 0.5, 0.8),
    'credo': ('disgusted', 0.4, 0.7),
    'eca': ('disgusted', 0.4, 0.6),
    'desprezo': ('disgusted', 0.6, 0.9),

    'surpresa': ('surprise', 0.5, 0.8),
    'choque': ('surprise', 0.7, 1.0),
    'assustou': ('surprise', 0.5, 0.8),
    'caramba': ('surprise', 0.3, 0.6),
    'incrível': ('surprise', 0.6, 0.9),
    'inesperado': ('surprise', 0.4, 0.7),

    'normal': ('neutral', 0.1, 0.3),
    'ok': ('neutral', 0.0, 0.2),
    'tanto faz': ('neutral', 0.2, 0.4),
    'simples': ('neutral', 0.1, 0.2),
    'comum': ('neutral', 0.0, 0.3)
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