from tqdm.auto import tqdm
import numpy as np
from sklearn.utils import shuffle
import nltk
import nlpaug.augmenter.word.context_word_embs as aug
import transformers
import pandas as pd
from cleaner import clean_text
import pyarrow
def main():

    modelo = "dccuchile/bert-base-spanish-wwm-uncased"
    augmenter = aug.ContextualWordEmbsAug(model_path= modelo, action="insert")

    df = pd.read_parquet("datos_limpios.parquet")
    df = df[["HATEFUL", "clean_text"]]
    aug_df = augmentMyData(df, augmenter, samples=33084)

    print(aug_df["HATEFUL"].value_counts())
    aug_df.to_parquet("datos_limpios_aug.parquet", engine = "pyarrow")




def augmentMyData(df, augmenter, repetitions=1, samples=200):
    augmented_texts = []
    
    hateful_df = df[df['HATEFUL'] == 1].reset_index(drop=True) 
    for i in tqdm(np.random.randint(0, len(hateful_df), samples)):
        
        for _ in range(repetitions):
            augmented_text = augmenter.augment(hateful_df['clean_text'].iloc[i])
            augmented_text_clean = clean_text(augmented_text)
            augmented_texts.append(str(augmented_text_clean))
    
    data = {
        'HATEFUL': 1,
        'clean_text': augmented_texts
    }
    aug_df = pd.DataFrame(data)
    df = shuffle(pd.concat([df,aug_df], axis = 0).reset_index(drop=True))
    return df


if __name__ == "__main__":

    main()