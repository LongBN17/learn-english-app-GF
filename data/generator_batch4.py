import json
import random

def get_current_content():
    try:
        with open('data/content.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_content(content):
    with open('data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

new_items = []

# --- GRAMMAR QUIZZES ---
grammar_quizzes = [
    ("She ___ to the gym everyday.", ["go", "goes", "going", "went"], 1, "Present simple for habit: She goes."),
    ("I ___ working here for 2 years.", ["have been", "am", "was", "had"], 0, "Present perfect continuous: have been working."),
    ("If I ___ you, I would accept the offer.", ["was", "am", "were", "been"], 2, "Conditional type 2: If I were you."),
    ("He said he ___ busy.", ["is", "was", "will be", "has been"], 1, "Reported speech backshift: is -> was."),
    ("This code needs ___.", ["refactor", "refactoring", "refactored", "to refactor"], 1, "Need + V-ing (passive meaning) or Need + noun."),
    ("I look forward to ___ you.", ["meet", "meeting", "met", "will meet"], 1, "Look forward to + V-ing."),
    ("She is interested ___ learning AI.", ["on", "in", "at", "about"], 1, "Interested in."),
    ("I am used to ___ late.", ["work", "working", "worked", "works"], 1, "Be used to + V-ing."),
    ("He stopped ___ to smoke.", ["work", "working", "to work", "works"], 2, "Stop to do something (dừng để làm gì). Context: stopped (driving/walking/coding) to smoke."),
    ("He stopped ___ because he was tired.", ["smoke", "smoking", "to smoke", "smoked"], 1, "Stop V-ing (dừng hẳn việc gì)."),
    ("Neither John ___ Mary is here.", ["or", "nor", "and", "but"], 1, "Neither... nor."),
    ("Either you ___ I have to fix this.", ["or", "nor", "and", "but"], 0, "Either... or."),
    ("I suggest ___ a new branch.", ["create", "creating", "to create", "created"], 1, "Suggest + V-ing."),
    ("Do you mind ___ the window?", ["open", "opening", "to open", "opened"], 1, "Do you mind + V-ing."),
    ("It's time we ___ the project.", ["start", "started", "starting", "starts"], 1, "It's time + S + V2/ed."),
    ("I wish I ___ known better.", ["have", "had", "has", "having"], 1, "Wish + Past Perfect (regret in past)."),
    ("By the time you arrive, I ___ left.", ["will have", "have", "had", "will"], 0, "Future perfect: will have left."),
    ("Hardly had I arrived ___ it started raining.", ["than", "when", "then", "after"], 1, "Hardly... when."),
    ("No sooner had I arrived ___ it started raining.", ["than", "when", "then", "after"], 0, "No sooner... than."),
    ("The man ___ car was stolen looks angry.", ["who", "whose", "whom", "which"], 1, "Whose (possessive)."),
    ("The bugs, ___ were fixed, caused many issues.", ["that", "which", "who", "whom"], 1, "Non-defining clause uses 'which', not 'that'."),
    ("Despite ___ hard, he failed.", ["study", "studying", "studied", "studies"], 1, "Despite + V-ing/Noun."),
    ("Although he ___ hard, he failed.", ["study", "studied", "studying", "studies"], 1, "Although + S + V."),
    ("Because of the ___, we cancelled the release.", ["rain", "rained", "raining", "rainy"], 0, "Because of + Noun."),
    ("Unless you ___ hard, you will fail.", ["study", "don't study", "will study", "won't study"], 0, "Unless = If not (auto negative)."),
    ("She asked me where ___.", ["I was", "was I", "am I", "I am"], 0, "Indirect question order: S + V."),
    ("I don't know who ___.", ["is he", "he is", "are they", "is she"], 1, "Indirect question order: S + V."),
    ("Let's go, ___?", ["will we", "shall we", "do we", "don't we"], 1, "Tag for Let's: shall we."),
    ("Don't touch that, ___?", ["will you", "do you", "don't you", "did you"], 0, "Tag for Imperative: will you."),
    ("He works ___ an engineer.", ["as", "like", "same", "similar"], 0, "Work as (role)."),
    ("He runs ___ a cheetah.", ["as", "like", "same", "so"], 1, "Like (similarity)."),
    ("It is ___ cold to swim.", ["enough", "too", "so", "very"], 1, "Too... to."),
    ("She is smart ___ to solve this.", ["enough", "too", "so", "very"], 0, "Adj + enough."),
    ("Have you ___ been to Vietnam?", ["ever", "never", "yet", "still"], 0, "Present perfect question: ever."),
    ("I haven't finished ___.", ["already", "yet", "just", "ever"], 1, "Negative perfect: yet."),
    ("She has ___ left.", ["yet", "just", "ever", "still"], 1, "Recent action: just."),
    ("It was ___ a nice day.", ["so", "such", "very", "too"], 1, "Such a..."),
    ("The code is ___ complicated.", ["so", "such", "too", "enough"], 0, "So + Adj."),
    ("Avoid ___ global variables.", ["use", "using", "to use", "used"], 1, "Avoid + V-ing."),
    ("He decided ___ the job.", ["take", "taking", "to take", "took"], 2, "Decide + to V."),
    ("I promise ___ late.", ["not be", "not to be", "to not be", "don't be"], 1, "Promise not to V."),
    ("Would you like ___ a drink?", ["have", "having", "to have", "had"], 2, "Would you like + to V."),
    ("How about ___ pizza?", ["eat", "eating", "to eat", "eaten"], 1, "How about + V-ing."),
    ("Why don't we ___ a break?", ["take", "taking", "to take", "taken"], 0, "Why don't we + V(bare)."),
    ("My laptop needs ___.", ["fix", "fixing", "to fix", "fixed"], 1, "Need + V-ing (passive)."),
]

for q, opts, ans, exp in grammar_quizzes:
    new_items.append({"type": "quiz", "question": q, "options": opts, "answer": ans, "explain": exp})
    
current_content = get_current_content()
current_content.extend(new_items)
save_content(current_content)

print(f"Added {len(new_items)} items. Total items: {len(current_content)}")
