from ctypes.wintypes import SC_HANDLE
import json
import os.path
import utils
import logging

#scores saved as JSON dictionary name:score
scores = {}

def read_scores():
    if not os.path.isfile(utils.SCORES_FILE_NAME):
        with open(utils.SCORES_FILE_NAME,"x") as f:
            f.write("{ }")
        return {}
    else:
        with open(utils.SCORES_FILE_NAME,"r") as f:
            data = json.load(f)
        return data


def write_scores(scores_dict):
    scores_json = json.dumps(scores_dict)
    with open(utils.SCORES_FILE_NAME,"w") as f:
        f.write(scores_json)

def add_score(name,win_score):
    scores = read_scores()
    curent_score = scores.get(name,0)
    scores[name] = curent_score + win_score
    write_scores(scores)

if __name__ == '__main_':
    logging.error("This module can't be run as main")
else:
    logging.info('Module "score.py" loaded')
