# -*- coding:utf-8 -*-
from flask import render_template
from flask import Flask, Markup
import utils.score as score
from operator import itemgetter
import logging
import sys, getopt

TEMPLATE_FOLDER = "./templates"

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)

logging.basicConfig(
    format="%(asctime)s<%(name)s>%(levelname)s:%(message)s",
    datefmt="[%d.%m.%Y|%I:%M.%S]",
    level=logging.INFO,
    filename="event.log",
)

# create High scores table and markup it for flask
def create_highscore():
    scores_str = ""
    scores = score.read_scores()
    i = 1
    for k in sorted(scores.items(), key=itemgetter(1, 0), reverse=True):
        scores_str = scores_str + str(i) + " : " + k[0] + " - " + str(k[1]) + "<br>"
        i = i + 1
    return Markup(scores_str)


def main(argv):
    app_ip = "0.0.0.0"
    app_port = "8080"
    # check arguments for ip/port override
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ip=", "port="])
    except getopt.GetoptError:
        print("Usage: mainscores.py -i <ip> -p <port>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("Usage: mainscores.py -i <ip> -p <port>")
            sys.exit()
        elif opt in ("-i", "--ip"):
            app_ip = arg
        elif opt in ("-p", "--port"):
            app_port = arg


    @app.route("/")
    def servingpage():
        ErrorMsg = ""
        try:
            ScoreStr = create_highscore()
        except:
            ErrorMsg = "Failed to create Highscore table"

        if ErrorMsg == "":
            print(ScoreStr)
            template = "highscores.html"
        else:
            template = "error.html"
        return render_template(template, ERROR=ErrorMsg, SCORE=ScoreStr)

    print("Starting App on - " + app_ip + ":" + app_port)
    app.run(app_ip, app_port)


if __name__ == "__main__":
    main(sys.argv[1:])
else:
    logging.error("This is not a module")
