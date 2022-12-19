
from flask import Flask, request, render_template
from utils import * # load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route("/") # main_page, all links candidates
def main():
    candidates = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<x>") # data every candidate
def candidate_page(x):
    candidate = get_candidate(x)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>") # search candidate by his name
def candidate_search_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, amount=len(candidates))


@app.route("/skill/<skill_name>") # search candidate by his skills
def search_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, amount=len(candidates))


app.run()
