from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pyarrow

df = pd.read_parquet("datos_limpios.parquet")
df = df[["clean_text", "HATEFUL"]]

train, test = train_test_split(df, 
                               random_state=42, 
                               shuffle=True,
                               test_size= 0.35,
                               stratify= df["HATEFUL"])

train.to_parquet("train.parquet", engine = "pyarrow")
test.to_parquet("test.parquet", engine = "pyarrow")

print(train.shape)
print(test.shape)