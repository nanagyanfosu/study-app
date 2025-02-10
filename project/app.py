from pyswip import Prolog
from flask import Flask, render_template, request

app = Flask(__name__)
prolog = Prolog()
prolog.consult("study_rules.pl")

# # Rules for recommendations
# rules = [
#     {"condition": {"style": "visual", "time": "short"}, "recommendation": "Use mind maps or flashcards to quickly review concepts."},
#     {"condition": {"style": "visual", "time": "long"}, "recommendation": "Create detailed diagrams or charts to organize the material."},
#     {"condition": {"style": "visual", "difficulty": "hard"}, "recommendation": "Watch video tutorials that explain the subject visually."},
#     {"condition": {"style": "visual", "motivation": "low"}, "recommendation": "Use colorful notes or apps to make studying visually appealing."},
#     {"condition": {"style": "auditory", "time": "short"}, "recommendation": "Listen to quick summary podcasts or recorded lectures."},
#     {"condition": {"style": "auditory", "time": "long"}, "recommendation": "Record yourself reading notes and play them back for review."},
#     {"condition": {"style": "auditory", "difficulty": "hard"}, "recommendation": "Join study groups and engage in discussions to clarify concepts."},
#     {"condition": {"style": "auditory", "motivation": "low"}, "recommendation": "Pair up with a friend and teach each other concepts aloud."},
#     {"condition": {"style": "kinesthetic", "time": "short"}, "recommendation": "Use hands-on methods like building models or using physical flashcards."},
#     {"condition": {"style": "kinesthetic", "time": "long"}, "recommendation": "Incorporate real-world examples or experiments into your study routine."},
#     {"condition": {"style": "kinesthetic", "difficulty": "hard"}, "recommendation": "Break down the material into smaller tasks and practice repeatedly."},
#     {"condition": {"style": "kinesthetic", "motivation": "low"}, "recommendation": "Take frequent breaks and include movement, like pacing while reviewing notes."},
#     {"condition": {"time": "short", "difficulty": "hard"}, "recommendation": "Focus on the most critical topics and practice with quick quizzes."},
#     {"condition": {"motivation": "low", "difficulty": "hard"}, "recommendation": "Set small, achievable goals and reward yourself after completing each task."},
#     {"condition": {"style": "visual", "style": "auditory", "motivation": "high"}, "recommendation": "Combine video tutorials and podcasts for a comprehensive review."},
# ]

# Function to get a recommendation based on user input
# def get_recommendation(user_input, rules):
#     for rule in rules:
#         if all(user_input.get(k) == v for k, v in rule["condition"].items()):
#             return rule["recommendation"]
#     return "No specific recommendation found for your input. Try refining your details."


def get_recommendation(user_input):
    style = user_input.get("style", "_") or "_"
    time = user_input.get("time", "_") or "_"
    difficulty = user_input.get("difficulty", "_") or "_"
    motivation = user_input.get("motivation", "_") or "_"

    query = f"recommendation({style}, {time}, {difficulty}, {motivation}, Material)."
    result = list(prolog.query(query))

    if result: 
        return result[0]["Material"]
    return "No specific recommendation found for your input. Try refining your details."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = {
        "style": request.form.get('style').strip().lower(),
        "time": request.form.get('time').strip().lower(),
        "difficulty": request.form.get('difficulty').strip().lower(),
        "motivation": request.form.get('motivation').strip().lower(),
    }
    recommendation = get_recommendation(user_input)
    return render_template('result.html', recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
