import re
import nltk
from nltk.corpus import stopwords
import numpy as np
import emoji

def clean_text(text):

  stop_words = set(stopwords.words("spanish"))
  stop_words.add("@usuario")
  text = np.array(text)
  for i in range(len(text)):

    text[i] = text[i].lower() #miniscula
    text[i] = re.sub(r"\bq\b", "que", text[i]) # q: que
    text[i] = re.sub(r"\bk\b", "que", text[i]) #k : que
    text[i] = re.sub(r"\bxq\b", "porque", text[i])
    text[i] = re.sub(r"\bx\b", "por", text[i])
    text[i] = re.sub(r"\bxque\b", "porque", text[i])
    text[i] = re.sub(r"\bpq\b", "porque", text[i]) # xque : porque
    text[i] = re.sub(r"\bporq\b", "porque", text[i])
    text[i] = re.sub(r"\bxfa\b", "por favor", text[i]) #xfa : por favor
    text[i] = re.sub(r"\b(?=\w*[j])(?=\w*[a])[ja]+\b", "jajaja", text[i]) #estandarizar risas a ja
    text[i] = re.sub(r"\bhdp\b", "hijo de puta", text[i]) #hdp : hijo de puta
    text[i] = re.sub(r"\basesinaaaaaaaaaaaaa\b", "asesina", text[i])
    text[i] = re.sub(r"\bpun-to\b", "punto", text[i])
    text[i] = text[i].replace("[]", "")
    text[i] = re.sub(r"\bkrajo\b", "carajo", text[i])
    text[i] = re.sub(r"\bhdmp\b", "hijo de mil putas", text[i])
    text[i] = re.sub(r"\bd\b", "de", text[i])
    text[i] = re.sub(r"\blpm\b", "la puta madre", text[i]) 
    text[i] = text[i].replace("@usuario", "")  #eliminar la palabra @usuario
    text[i] = text[i].replace("si", "")
    text[i] = re.sub(r'https?://\S+', "url", text[i]) #cambiar una url por "url"
    text[i] = re.sub(r'[^\w\s]', '', text[i]) #quitar signos de puntuación
    text[i] = emoji.replace_emoji(text[i], replace="") #quitar emojis
    text[i] = re.sub(r"\bn\b", "", text[i]) 
    text[i] = text[i].strip()
    text[i] = " ".join([palabra for palabra in text[i].split() if palabra not in stop_words]) #eli

  return text
