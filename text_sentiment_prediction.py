import pandas as pd
import numpy as np

import tensorflow
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

train_data = pd.read_csv(".\\static\\data_files\\tweet_emotions.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "content"]
    training_sentences.append(sentence)

#load model
model = load_model(".\\static\\model_files\\Tweet_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

#assign emoticons for different emotions
emo_code_url = {
    "empty": [0, "./static/emoticons/Empty.png"],
    "sadness": [1,"./static/emoticons/Sadness.png" ],
    "enthusiasm": [2, "./static/emoticons/Enthusiasm.png"],
    "neutral": [3, "./static/emoticons/Neutral.png"],
    "worry": [4, "./static/emoticons/Worry.png"],
    "surprise": [5, "./static/emoticons/Surprise.png"],
    "love": [6, "./static/emoticons/Love.png"],
    "fun": [7, "./static/emoticons/fun.png"],
    "hate": [8, "./static/emoticons/hate.png"],
    "happiness": [9, "./static/emoticons/happiness.png"],
    "boredom": [10, "./static/emoticons/boredom.png"],
    "relief": [11, "./static/emoticons/relief.png"],
    "anger": [12, "./static/emoticons/anger.png"]
}

def fit(some_list, target_len):
  part1 = list(some_list[:target_len])
  filler = " "* (target_len - len(some_list))
  part1 += filler
  return part1

# write the function to predict emotion
def predict(text: str) -> str:
    sequences = tokenizer.texts_to_sequences([fit(text, 100)])
    padded = pad_sequences(
        sequences,
        maxlen=100,
        padding=padding_type,
        truncating=trunc_type
    )
    prediction = list(model.predict(padded)[0])
    index = prediction.index(max(prediction))

    for cell in emo_code_url:
        value = emo_code_url[cell]
        if value[0] == index:
            print(f"{cell}: {prediction[index]}")
            return f"{cell}::{value[1]}"

    return "Unknown::Unknown"