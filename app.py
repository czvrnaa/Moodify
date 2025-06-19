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
        {"artist": "Daft Punk", "name": "Digital Love", "spotify": "https://open.spotify.com/embed/track/2Foc5Q5nqNiosCNqttzHof", "description": "Futurystyczny, radosny kawałek o miłości i marzeniach."},
        {"artist": "Arctic Monkeys", "name": "Snap Out of It", "spotify": "https://open.spotify.com/embed/track/1wMAnQ7nQ4Dd2GzYi8U0MO", "description": "Dynamiczny numer z lekkim, pozytywnym klimatem."},
        {"artist": "Kiss", "name": "Tomorrow", "spotify": "https://open.spotify.com/embed/track/0MQh7tE3K2r9SwD8mrK2b8", "description": "Melodyjna, optymistyczna piosenka z lat 80."},
    ],
    "smutny": [
        {"artist": "Radiohead", "name": "Exit Music (For a Film)", "spotify": "https://open.spotify.com/embed/track/4TssB1N2wQYJczO4xqaSlR", "description": "Atmosferyczny utwór o odosobnieniu i emocjonalnym zniknięciu."},
        {"artist": "Myslovitz", "name": "Scenariusz dla moich sąsiadów", "spotify": "https://open.spotify.com/embed/track/6OzJY6GqXVKPk2xgm8FJ8j", "description": "Refleksyjny i melancholijny utwór o życiu i samotności."},
        {"artist": "Pink Floyd", "name": "The Final Cut", "spotify": "https://open.spotify.com/embed/track/2G4AUqfwxcVQmYd8vWIir5", "description": "Pełna bólu i emocji ballada o wojnie i stracie."},
    ],
    "energetyczny": [
        {"artist": "Metallica", "name": "Whiplash", "spotify": "https://open.spotify.com/embed/track/6qFtVazr3DylZf9WlNxYz4", "description": "Szybki, bezkompromisowy utwór z pierwszych lat zespołu."},
        {"artist": "Linkin Park", "name": "Figure.09", "spotify": "https://open.spotify.com/embed/track/3FV5qlGkJ28iBPT8fQRa2L", "description": "Energetyczna mieszanka rocka i elektroniki z mocnym refrenem."},
        {"artist": "System of a Down", "name": "Bounce", "spotify": "https://open.spotify.com/embed/track/4zz3pUDK3UXvVlRkhzKoKI", "description": "Eksperymentalny, szybki i absurdalny – idealny na wyładowanie energii."},
    ],
    "zrelaksowany": [
        {"artist": "Pink Floyd", "name": "A Pillow of Winds", "spotify": "https://open.spotify.com/embed/track/0VBI7SO6UnG7rk0yQfT0OE", "description": "Spokojna, senna ballada z akustycznym klimatem."},
        {"artist": "Daft Punk", "name": "Make Love", "spotify": "https://open.spotify.com/embed/track/2T7DXU8gWjExVJPtUnX2Ft", "description": "Delikatny, instrumentalny utwór idealny do relaksu."},
        {"artist": "Radiohead", "name": "Codex", "spotify": "https://open.spotify.com/embed/track/6vJz0zImu1vriZtT3zJ6A9", "description": "Hipnotyzujący, cichy utwór z albumu *The King of Limbs*."},
    ],
    "zly": [
        {"artist": "Guns N' Roses", "name": "Pretty Tied Up", "spotify": "https://open.spotify.com/embed/track/1iZt7OcT1Azf7hKbdTSE1U", "description": "Brudny riff i buntowniczy tekst – idealny na frustrację."},
        {"artist": "System of a Down", "name": "Forest", "spotify": "https://open.spotify.com/embed/track/1PUijKMEOKwAfF2uHmjS6A", "description": "Chaotyczny i złośliwy utwór o konflikcie wewnętrznym."},
        {"artist": "Metallica", "name": "The God That Failed", "spotify": "https://open.spotify.com/embed/track/1e6iDMoEfgUor6OLvDCI5g", "description": "Ciężki, gniewny kawałek o zdradzie i rozczarowaniu."},
    ],
    "zakochany": [
        {"artist": "Kult", "name": "Gdy nie ma dzieci", "spotify": "https://open.spotify.com/embed/track/6myJMXZzMO3fj8R5AZ3hQ3", "description": "Lekko ironiczny, ale melodyjny kawałek o relacjach."},
        {"artist": "Tyler, The Creator", "name": "Awkward", "spotify": "https://open.spotify.com/embed/track/6XEvs5nS7gqgec9J3GJpOA", "description": "Szczery, dziwaczny love song o niepewnej relacji."},
        {"artist": "Metallica", "name": "Orion", "spotify": "https://open.spotify.com/embed/track/3QZ7uX97s82HFYSmQUAN1D", "description": "Instrumentalna, epicka kompozycja – refleksja i emocje bez słów."},
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
                recommendations=songs_by_mood[selected_mood]
            )
    return render_template("index.html", moods=mood_settings)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)



