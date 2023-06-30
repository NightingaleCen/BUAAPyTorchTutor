import json
import os
import pandas as pd
import numpy as np
import re

with open("10 plants dataset/test_labels.json", "r") as f:
    test_labels = json.load(f)

df = pd.DataFrame()
for num, file in enumerate(os.listdir("review")):
    if file.endswith(".json"):
        with open(f"review/{file}", "r") as f:
            res = json.load(f)

        # raw_keys = list(res.keys())

        # for key in raw_keys:
        #    res[re.sub(r"\b10(?=\d)", "", key)] = res[key]
        #    del res[key]
        test_acc = np.mean([1 if res[i] == test_labels[i] else 0 for i in res.keys()])
        temp_df = pd.DataFrame(
            {"Name": re.sub(r".json", "", file), "Acc": float(test_acc)}, index=[num]
        )
        df = pd.concat([df, temp_df])
df = df.sort_values(by="Acc", ascending=False)
df.to_excel("review_result.xlsx", index=False)
