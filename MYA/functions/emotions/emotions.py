import json

json_path = 'MYA/functions/emotions/word.json'


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

with open(json_path, 'r') as file:
    data = json.load(file)

def verify(question):
    new_question = question.lower().split()
        
    for palavra in new_question:
        if palavra in data:
            for chave,valor in data[palavra].items():
                new_emotion = max(-1,min(1,valor))
        
                if emotions[chave] < new_emotion:
                    emotions[chave] = emotions[chave] + new_emotion
                elif new_emotion < 0:
                    emotions[chave] = emotions[chave] + new_emotion    
                elif emotions[chave] <= new_emotion:
                    emotions[chave] = new_emotion
                     
    return emotions
