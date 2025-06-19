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
        {"artist": "KISS", "name": "Tomorrow", "youtube": "https://www.youtube.com/watch?v=11y0Lge2UuU", "description": "Melodyjna, optymistyczna piosenka z lat 80."},
    ],
    "smutny": [
        {"artist": "Radiohead", "name": "How to Disappear Completely", "youtube": "https://www.youtube.com/watch?v=RByvzmmEFiQ", "description": "Atmosferyczny utwór o odosobnieniu i emocjonalnym zniknięciu."},
        {"artist": "Myslovitz", "name": "Scenariusz dla moich sąsiadów", "youtube": "https://www.youtube.com/watch?v=w51NABNPMWs", "description": "Refleksyjny i melancholijny utwór o życiu i samotności."},
        {"artist": "Pink Floyd", "name": "The Final Cut", "youtube": "https://www.youtube.com/watch?v=DPLv2n2rJfQ", "description": "Pełna bólu i emocji ballada o wojnie i stracie."},
    ],
    "energetyczny": [
        {"artist": "Metallica", "name": "Whiplash", "youtube": "https://www.youtube.com/watch?v=QP-PGg4aGv4", "description": "Szybki, bezkompromisowy utwór z pierwszych lat zespołu."},
        {"artist": "Linkin Park", "name": "Figure.09", "youtube": "https://www.youtube.com/watch?v=AwPzH_fFUpI", "description": "Energetyczna mieszanka rocka i elektroniki z mocnym refrenem."},
        {"artist": "System of a Down", "name": "Bounce", "youtube": "https://www.youtube.com/watch?v=YmTmWu4DraY", "description": "Eksperymentalny, szybki i absurdalny – idealny na wyładowanie energii."},
    ],
    "zrelaksowany": [
        {"artist": "Pink Floyd", "name": "A Pillow of Winds", "youtube": "https://www.youtube.com/watch?v=Tk0t3zO0J8k", "description": "Spokojna, senna ballada z akustycznym klimatem."},
        {"artist": "Daft Punk", "name": "Make Love", "youtube": "https://www.youtube.com/watch?v=E_5N1j_z4Kw", "description": "Delikatny, instrumentalny utwór idealny do relaksu."},
        {"artist": "Radiohead", "name": "Codex", "youtube": "https://www.youtube.com/watch?v=I03xZzr1oZM", "description": "Hipnotyzujący, cichy utwór z albumu *The King of Limbs*."},
    ],
    "zly": [
        {"artist": "Guns N' Roses", "name": "Pretty Tied Up", "youtube": "https://www.youtube.com/watch?v=wTZyJ8ZGVKc", "description": "Brudny riff i buntowniczy tekst – idealny na frustrację."},
        {"artist": "System of a Down", "name": "Forest", "youtube": "https://www.youtube.com/watch?v=UW8fNPfFyEY", "description": "Chaotyczny i złośliwy utwór o konflikcie wewnętrznym."},
        {"artist": "Metallica", "name": "The God That Failed", "youtube": "https://www.youtube.com/watch?v=3doL9vWl5Tc", "description": "Ciężki, gniewny kawałek o zdradzie i rozczarowaniu."},
    ],
    "zakochany": [
        {"artist": "Kult", "name": "Gdy nie ma dzieci", "youtube": "https://www.youtube.com/watch?v=_VCWV6pOKv8", "description": "Lekko ironiczny, ale melodyjny kawałek o relacjach."},
        {"artist": "Tyler, The Creator", "name": "Awkward", "youtube": "https://www.youtube.com/watch?v=ovauWjsQMm8", "description": "Szczery, dziwaczny love song o niepewnej relacji."},
        {"artist": "Metallica", "name": "Orion", "youtube": "https://www.youtube.com/watch?v=S0vsYJY9RYU", "description": "Instrumentalna, epicka kompozycja – refleksja i emocje bez słów."},
    ],
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




