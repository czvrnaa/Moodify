from flask import Flask, render_template, request

app = Flask(__name__)

mood_settings = {
    "wesoly": {"emoji": "😊"},
    "smutny": {"emoji": "😢"},
    "energetyczny": {"emoji": "⚡"},
    "zrelaksowany": {"emoji": "😌"},
    "zly": {"emoji": "😠"},
    "zakochany": {"emoji": "😍"},
}

songs_by_mood = {
    "wesoly": [
        {"artist": "Daft Punk", "name": "Digital Love", "youtube": "https://www.youtube.com/watch?v=FxzBvqYH4bY", "description": "Futurystyczny, radosny kawałek o miłości i marzeniach."},
        {"artist": "Arctic Monkeys", "name": "Snap Out of It", "youtube": "https://www.youtube.com/watch?v=H8tLS_NOWLs", "description": "Dynamiczny numer z lekkim, pozytywnym klimatem."},
        {"artist": "Kiss", "name": "Tomorrow", "youtube": "https://www.youtube.com/watch?v=Ot2QAMwCZNw", "description": "Melodyjna, optymistyczna piosenka z lat 80."},
    ],
    # ... pozostałe kategorie takie same ...
}

@app.route("/", methods=["GET", "POST"])
def mood():
    if request.method == "POST":
        selected_mood = request.form.get("mood")
        if selected_mood in songs_by_mood:
            return render_template(
                "mood.html",
                mood=selected_mood,
                emoji=mood_settings[selected_mood]["emoji"],
                recommendations=songs_by_mood[selected_mood],
                moods=mood_settings
            )
    return render_template("index.html", moods=mood_settings)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




