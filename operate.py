import pandas as pd
import glob
import os

path_files_test = glob.glob("data/test/*")
path_files_train = glob.glob("data/train/*")


def read_txt(path_to_read):
    with open(path_to_read, "r") as file:
        file_content = file.read()
    return file_content


def construct_data(path_input):

    # "data/test/*"
    path_files_test = glob.glob(path_input)
    path_txt = []
    for sentiment in path_files_test:
        sub_folders = glob.glob(os.path.join(sentiment, "*"))
        sentiment_label = os.path.split(sentiment)[-1]
        list_by_sentiment = []
        for sub_folder in sub_folders:
            dict_result = {}
            dict_result["phrase"] = read_txt(sub_folder)
            dict_result["sentiment"] = sentiment_label
            list_by_sentiment.append(dict_result)

        path_txt += list_by_sentiment

    df_out = pd.DataFrame(path_txt)
    return df_out


df_test = construct_data("data/test/*")
df_train = construct_data("data/train/*")

with open("test_dataset.csv", "w") as file:
    df_test.to_csv(file, index=False)

with open("train_dataset.csv", "w") as file:
    df_train.to_csv(file, index=False)
