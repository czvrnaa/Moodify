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
        {"artist": "Daft Punk", "name": "Digital Love", "spotify": "https://open.spotify.com/embed/track/2VEZx7NWsZ1D0eJ4uv5Fym", "description": "Futurystyczny, radosny kawałek o miłości i marzeniach."},
        {"artist": "Arctic Monkeys", "name": "Snap Out of It", "spotify": "https://open.spotify.com/embed/track/0NdTUS4UiNYCNn5FgVqKQY", "description": "Dynamiczny numer z lekkim, pozytywnym klimatem."},
        {"artist": "Kiss", "name": "Tomorrow", "spotify": "https://open.spotify.com/embed/track/0Md4wlfbySpnA2kEICWyl9", "description": "Melodyjna, optymistyczna piosenka z lat 80."},
    ],
    "smutny": [
        {"artist": "Radiohead", "name": "Exit Music (For a Film)", "spotify": "https://open.spotify.com/embed/track/0z1o5L7HJx562xZSATcIpY", "description": "Atmosferyczny utwór o odosobnieniu i emocjonalnym zniknięciu."},
        {"artist": "Myslovitz", "name": "Długość dźwięku samotności", "spotify": "https://open.spotify.com/embed/track/5ytkHKps6RVVDFZwAqVDCB", "description": "Refleksyjny i melancholijny utwór o życiu i samotności."},
        {"artist": "Arctic Monkeys", "name": "No. 1 Party Anthem", "spotify": "https://open.spotify.com/embed/track/5TTGoX70AFrTvuEtqHK37S?si=b6c6abb90a944aa2", "description": "Nastrojowa i pełna tęsknoty ballada o samotności w tłumie."},
    ],
    "energetyczny": [
        {"artist": "Metallica", "name": "Whiplash", "spotify": "https://open.spotify.com/embed/track/38fIaph07Kd8ZIN6l17ZJs", "description": "Szybki, bezkompromisowy utwór z pierwszych lat zespołu."},
        {"artist": "Linkin Park", "name": "Figure.09", "spotify": "https://open.spotify.com/embed/track/0rPTPahzhGx9LSzI8XX5OM", "description": "Energetyczna mieszanka rocka i elektroniki z mocnym refrenem."},
        {"artist": "System of a Down", "name": "Chop Suey!", "spotify": "https://open.spotify.com/embed/track/2DlHlPMa4M17kufBvI2lEN", "description": "Eksperymentalny, szybki i absurdalny – idealny na wyładowanie energii."},
    ],
    "zrelaksowany": [
        {"artist": "Gorrilaz", "name": "On Melancholy Hill", "spotify": "https://open.spotify.com/embed/track/0q6LuUqGLUiCPP1cbdwFs3?si=00d039395373418d", "description": "Ten utwór łączy subtelny synth-pop z melancholijnym klimatem, tworząc poczucie spokoju i zadumy."},
        {"artist": "Daft Punk", "name": "Make Love", "spotify": "https://open.spotify.com/embed/track/4ABWPP59ItFKykdaDF09K5", "description": "Delikatny, instrumentalny utwór idealny do relaksu."},
        {"artist": "Radiohead", "name": "Codex", "spotify": "https://open.spotify.com/embed/track/6ttYF5VadzTssGV2i1Q08T", "description": "Hipnotyzujący, cichy utwór z albumu *The King of Limbs*."},
    ],
    "zly": [
        {"artist": "Guns N' Roses", "name": "Pretty Tied Up", "spotify": "https://open.spotify.com/embed/track/2hAt6y582UsTcwvCKTcTMs", "description": "Brudny riff i buntowniczy tekst – idealny na frustrację."},
        {"artist": "System of a Down", "name": "Forest", "spotify": "https://open.spotify.com/embed/track/1B5Y9I5wPfvD3C2A81A36C", "description": "Chaotyczny i złośliwy utwór o konflikcie wewnętrznym."},
        {"artist": "Metallica", "name": "The God That Failed", "spotify": "https://open.spotify.com/embed/track/5wAS8svvT4d27ZpiPvFA0Z", "description": "Ciężki, gniewny kawałek o zdradzie i rozczarowaniu."},
    ],
    "zakochany": [
        {"artist": "Kult", "name": "Gdy nie ma dzieci", "spotify": "https://open.spotify.com/embed/track/318KZH2O4R003o3hL1aDqS", "description": "Lekko ironiczny, ale melodyjny kawałek o relacjach."},
        {"artist": "Tyler, The Creator", "name": "Darling, I", "spotify": "https://open.spotify.com/embed/track/0VaeksJaXy5R1nvcTMh3Xk", "description": "Szczery love song o niepewnej relacji."},
        {"artist": "Metallica", "name": "Orion", "spotify": "https://open.spotify.com/embed/track/3z9e5b0P7zoIeV6I3iyX8O", "description": "Instrumentalna, epicka kompozycja – refleksja i emocje bez słów."},
    ],
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", moods=mood_settings)

@app.route("/mood", methods=["POST"])
def mood():
    selected_mood = request.form.get("mood")
    print("Odebrano nastrój:", selected_mood)
    if selected_mood in songs_by_mood:
        return render_template(
            "mood.html",
            mood=selected_mood,
            moods=mood_settings,
            recommendations=songs_by_mood[selected_mood]
        )
    return render_template("index.html", moods=mood_settings, error="Niepoprawny nastrój.")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





