from flask import Flask, request
from spell_corrector import correction
import config
import json

app = Flask(__name__)


@app.route("/spellCorrect", methods=["POST"])
def spell_correct():
    requests = request.json
    word = requests["word"]
    correct = correction(word)
    return json.dumps(correct)


if __name__=="__main__":
    app.run()