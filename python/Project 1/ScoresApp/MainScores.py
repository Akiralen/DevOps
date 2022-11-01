from flask import render_template
from flask import Flask,Markup
import Scores.score as score
from operator import itemgetter
import logging

TEMPLATE_FOLDER = "./templates"
#create High scores table and markup it for flask
def create_highscore():
    scores_str = ""
    scores = score.read_scores()
    i = 1
    for k in  sorted(scores.items(), key=itemgetter(1,0), reverse = True):
        scores_str = scores_str + str(i) + " : " + k[0] + " - " + str(k[1]) + '<br>'
        i = i + 1 
    return Markup(scores_str)

def main():
    app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
    ErrorMsg = ""
    try:
        ScoreStr = create_highscore()
    except:
        ErrorMsg = "Failed to create Highscore table"
    if ErrorMsg == "":
        template = "highscores.html"
    else:
        template = "error.html"
    @app.route('/')
    def servingpage():
        return render_template(template,ERROR = ErrorMsg,SCORE = ScoreStr)

    app.run(app_ip,app_port)


if __name__ == "__main__":
    main()
else:
    logging.error("This is not a module")