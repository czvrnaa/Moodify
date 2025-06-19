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
        {"artist": "Daft Punk", "name": "Digital Love", "spotify": "https://open.spotify.com/track/2VEZx7NWsZ1D0eJ4uv5Fym?si=098d437d91d8433e", "description": "Futurystyczny, radosny kawałek o miłości i marzeniach."},
        {"artist": "Arctic Monkeys", "name": "Snap Out of It", "spotify": "https://open.spotify.com/track/0NdTUS4UiNYCNn5FgVqKQY?si=8d5af2384a5447b4", "description": "Dynamiczny numer z lekkim, pozytywnym klimatem."},
        {"artist": "Kiss", "name": "Tomorrow", "spotify": "https://open.spotify.com/track/0Md4wlfbySpnA2kEICWyl9?si=2a5db9bb3b854a54", "description": "Melodyjna, optymistyczna piosenka z lat 80."},
    ],
    "smutny": [
        {"artist": "Radiohead", "name": "Exit Music (For a Film)", "spotify": "https://open.spotify.com/track/0z1o5L7HJx562xZSATcIpY?si=83bb3050b7334f3f", "description": "Atmosferyczny utwór o odosobnieniu i emocjonalnym zniknięciu."},
        {"artist": "Myslovitz", "name": "Długość dźwięku samotności", "spotify": "https://open.spotify.com/track/5ytkHKps6RVVDFZwAqVDCB?si=a4f203bb1fab41fc", "description": "Refleksyjny i melancholijny utwór o życiu i samotności."},
        {"artist": "Pink Floyd", "name": "The Final Cut", "spotify": "https://open.spotify.com/album/1yMenUMOx7BpfTDuVQs99y?si=209c661f13174c37", "description": "Pełna bólu i emocji ballada o wojnie i stracie."},
    ],
    "energetyczny": [
        {"artist": "Metallica", "name": "Whiplash", "spotify": "https://open.spotify.com/track/38fIaph07Kd8ZIN6l17ZJs?si=07e8aa18cb3344d8", "description": "Szybki, bezkompromisowy utwór z pierwszych lat zespołu."},
        {"artist": "Linkin Park", "name": "Figure.09", "spotify": "https://open.spotify.com/track/0rPTPahzhGx9LSzI8XX5OM?si=c7d7e83537f34813", "description": "Energetyczna mieszanka rocka i elektroniki z mocnym refrenem."},
        {"artist": "System of a Down", "name": "Chop  Suey!", "spotify": "https://open.spotify.com/track/2DlHlPMa4M17kufBvI2lEN?si=300fbe0481d24883", "description": "Eksperymentalny, szybki i absurdalny – idealny na wyładowanie energii."},
    ],
    "zrelaksowany": [
        {"artist": "Pink Floyd", "name": "Us and Them", "spotify": "https://open.spotify.com/embed/track/0VBI7SO6UnG7rk0yQfT0OE", "description": "Spokojna, senna ballada z niesamowitym klimatem."},
        {"artist": "Daft Punk", "name": "Make Love", "spotify": "https://open.spotify.com/track/4ABWPP59ItFKykdaDF09K5?si=6fa23ca83caf42f7", "description": "Delikatny, instrumentalny utwór idealny do relaksu."},
        {"artist": "Radiohead", "name": "Codex", "spotify": "https://open.spotify.com/track/6ttYF5VadzTssGV2i1Q08T?si=6befe58e153e43b5", "description": "Hipnotyzujący, cichy utwór z albumu *The King of Limbs*."},
    ],
    "zly": [
        {"artist": "Guns N' Roses", "name": "Pretty Tied Up", "spotify": "https://open.spotify.com/track/2hAt6y582UsTcwvCKTcTMs?si=04800e7b5b534423", "description": "Brudny riff i buntowniczy tekst – idealny na frustrację."},
        {"artist": "System of a Down", "name": "Forest", "spotify": "https://open.spotify.com/track/1B5Y9I5wPfvD3C2A81A36C?si=9fb896c5b6024c8d", "description": "Chaotyczny i złośliwy utwór o konflikcie wewnętrznym."},
        {"artist": "Metallica", "name": "The God That Failed", "spotify": "https://open.spotify.com/track/5wAS8svvT4d27ZpiPvFA0Z?si=03f5462116cb4129", "description": "Ciężki, gniewny kawałek o zdradzie i rozczarowaniu."},
    ],
    "zakochany": [
        {"artist": "Kult", "name": "Gdy nie ma dzieci", "spotify": "https://open.spotify.com/track/318KZH2O4R003o3hL1aDqS?si=9491eb50c3134619", "description": "Lekko ironiczny, ale melodyjny kawałek o relacjach."},
        {"artist": "Tyler, The Creator", "name": "Darling, I", "spotify": "https://open.spotify.com/track/0VaeksJaXy5R1nvcTMh3Xk?si=aa7675d507fe4e60", "description": "Szczery love song o niepewnej relacji."},
        {"artist": "Metallica", "name": "Orion", "spotify": "https://open.spotify.com/track/3z9e5b0P7zoIeV6I3iyX8O?si=bc8c0806ecd64bde", "description": "Instrumentalna, epicka kompozycja – refleksja i emocje bez słów."},
    ],
}
@app.route("/", methods=["GET", "POST"])
def mood():
    if request.method == "POST":
        selected_mood = request.form.get("mood")
        if selected_mood in songs_by_mood:
            return render_template(
                "mood.html",
                moods=mood_settings,
                mood=selected_mood,
                recommendations=songs_by_mood[selected_mood],
                error=None
            )
        else:
            return render_template(
                "mood.html",
                moods=mood_settings,
                mood=None,
                recommendations=[],
                error="Niepoprawny nastrój!"
            )
    # GET
    return render_template(
        "mood.html",
        moods=mood_settings,
        mood=None,
        recommendations=[],
        error=None
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)



