import numpy as np
import pickle
import json
import gzip

model = None
features = None

def load_artifacts():
    global model
    global features

    with gzip.open("artifacts/ipl.pickle.gz", "rb") as f:
        model = pickle.load(f)

    with open("artifacts/features.json", "r") as f:
        features = json.load(f)

def get_team():
    load_artifacts()
    global features

    return features["team"]

def get_venue():
    global  features

    return features["venue"]


def predict_score(runs=50,wickets=0,overs=5.1,runs_last_5=50,wickets_last_5=0,bat_team='chennai super kings', bowl_team='mumbai indians',venue="barabati"):
    global model
    temp_array = list()
    print(runs,wickets,overs,runs_last_5,wickets_last_5,bat_team,bowl_team,venue)
  # Batting Team
    if bat_team == 'chennai super kings':
        temp_array = temp_array + [0,0,0,0,0,0,0]
    elif bat_team == 'delhi capitals':
        temp_array = temp_array + [1,0,0,0,0,0,0]
    elif bat_team == 'kings xi punjab':
        temp_array = temp_array + [0,1,0,0,0,0,0]
    elif bat_team == 'kolkata knight riders':
        temp_array = temp_array + [0,0,1,0,0,0,0]
    elif bat_team == 'mumbai indians':
        temp_array = temp_array + [0,0,0,1,0,0,0]
    elif bat_team == 'rajasthan royals':
        temp_array = temp_array + [0,0,0,0,1,0,0]
    elif bat_team == 'royal challengers bangalore':
        temp_array = temp_array + [0,0,0,0,0,1,0]
    elif bat_team == 'sunrisers hyderabad':
        temp_array = temp_array + [0,0,0,0,0,0,1]

  # Bowling Team
    if bowl_team == 'chennai super kings':
        temp_array = temp_array + [0,0,0,0,0,0,0]
    elif bowl_team == 'delhi capitals':
        temp_array = temp_array + [1,0,0,0,0,0,0]
    elif bowl_team == 'kings xi punjab':
        temp_array = temp_array + [0,1,0,0,0,0,0]
    elif bowl_team == 'kolkata knight riders':
        temp_array = temp_array + [0,0,1,0,0,0,0]
    elif bowl_team == 'mumbai indians':
        temp_array = temp_array + [0,0,0,1,0,0,0]
    elif bowl_team == 'rajasthan royals':
        temp_array = temp_array + [0,0,0,0,1,0,0]
    elif bowl_team == 'royal challengers bangalore':
        temp_array = temp_array + [0,0,0,0,0,1,0]
    elif bowl_team == 'sunrisers hyderabad':
        temp_array = temp_array + [0,0,0,0,0,0,1]

  # Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
    temp_array = [overs, runs, wickets, runs_last_5, wickets_last_5]+temp_array

  # Converting into numpy array
    temp_array = np.array([temp_array])
    print(temp_array)
    print(int(model.predict(temp_array)[0]))
    print("hello")
  # Prediction
    return int(model.predict(temp_array)[0])


if __name__ == "__main__":
    print(get_team())
    print("-------------------------------")
    print(get_venue())
    print("-------------------------------")
    print(predict_score(61, 2, 7.2, 40, 2, "chennai super kings", "mumbai indians",
                  "barabati stadium"))

