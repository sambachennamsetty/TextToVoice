from flask import Flask, render_template, request, send_file
from gtts import gTTS
from pydub import AudioSegment
import librosa
import soundfile as sf
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    if not text:
        return "No text provided", 400

    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='te', slow=False)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=False)


@app.route('/download', methods=['POST'])
def download():
    text = request.form['text']
    if not text:
        return "No text provided", 400

    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='te', slow=False)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True, download_name="output.mp3")


@app.route('/speedup', methods=['POST'])
def speedup():
    text = request.form['text']
    if not text:
        return "No text provided", 400

    # Convert text to speech and save as temporary file
    tts = gTTS(text=text, lang='te', slow=False)
    tts.save("output_temp.mp3")

    # Load and apply time-stretching
    audio, sr = librosa.load("output_temp.mp3")
    faster_audio = librosa.effects.time_stretch(audio, rate=1.5)  # Increase speed by 1.5x
    sf.write("output_faster.wav", faster_audio, sr)  # Save as WAV for quality

    # Convert to MP3 with pydub for browser compatibility
    faster_audio_pydub = AudioSegment.from_wav("output_faster.wav")
    amplified_audio = faster_audio_pydub + 6
    amplified_audio.export("output_faster.mp3", format="mp3")

    # Remove temporary files
    os.remove("output_temp.mp3")
    os.remove("output_faster.wav")

    return send_file("output_faster.mp3", as_attachment=False)


if __name__ == '__main__':
    app.run(debug=True)