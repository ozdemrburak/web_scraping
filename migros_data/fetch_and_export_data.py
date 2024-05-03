import pandas as pd


def data_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("data.xlsx", index=False)


def data_to_json(data):
    df = pd.DataFrame(data)
    df.to_json("data.json", index=False)
