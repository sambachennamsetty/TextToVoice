from gtts import gTTS
from pydub import AudioSegment
import librosa
import soundfile as sf


text = "సింగరాయకొండ మండల ప్రజలకు దీపావళి పండుగ సందర్భంగా,మీకు మరియు మీ కుటుంబసభ్యులకు దీపావళి పండుగ శుభాకాంక్షలు.ఈ వెలుగుల పండుగ మీ జీవితంలో కాంతులు విజయాలు నింపాలని, మీ ఇంట వెలిగే ప్రతి దీపం కొత్త ఆశలు కొత్త ఆనందాలు ఇవ్వాలని కోరుకుంటున్నాము.పటాసుల తళుకులతో,మీ సాయంకాలం వేడుకగా మారి మీ హృదయాలలో ఉత్సాహం,ఆత్మవిశ్వాసం నింపి మీ ఎదుగుదలకు దారి చూపాలని మనస్ఫూర్తిగ ఆకాంక్షిస్తున్నాము.ఈ దీపావళి మీ కలలను సాకారం చేయాలని ఆయురారోగ్యాలు అష్టైశ్వర్యాలు మీకు ప్రసాదించాలని ఆ భగవంతుడిని ప్రార్థిస్తూ.మీ..!సింగరాయకొండ అప్డేట్స్"
tts = gTTS(text=text, lang='te', slow=False)
# Generate the basic TTS audio file
tts.save("output_te.mp3")

# Step 2: Load the audio with librosa for advanced time-stretching
audio, sr = librosa.load("output_te.mp3")

# Step 3: Use a moderate speed-up factor to retain quality
# Step 3: Time-stretch the audio using phase vocoder algorithm (reduces echo artifacts)
# Use a higher quality phase vocoder
faster_audio = librosa.effects.time_stretch(audio, rate=1.5)

# Step 4: Apply a light high-pass filter to improve voice clarity
# This reduces some lower frequency artifacts that can cause muddiness
faster_audio = librosa.effects.preemphasis(faster_audio)

# Step 5: Save the processed audio back to a file
sf.write("output_te_faster_temp.wav", faster_audio, sr)  # Save temporarily as a WAV file for better quality

# Step 6: Load the time-stretched file with pydub, increase volume
adjusted_audio = AudioSegment.from_wav("output_te_faster_temp.wav")
amplified_audio = adjusted_audio + 4  # Increase volume by 6 dB (adjust as needed)

# Step 7: Export the amplified audio
amplified_audio.export("output_te_faster.mp3", format="mp3")

print("Audio files saved: 'output_te.mp3' (original), 'output_te_faster.mp3' (faster, improved clarity)")

# # Step 2: Load the generated audio file with pydub
# audio = AudioSegment.from_mp3("output_te.mp3")
#
# # Step 3: Customize the speed of the audio
# # Increase speed (e.g., 1.5x faster)
# faster_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * 1.2)})
#
# # Decrease speed (e.g., 0.75x slower)
# slower_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * 1)})
#
# # Step 4: Set frame rate back to the standard 44100 Hz for compatibility and export
# faster_audio = faster_audio.set_frame_rate(44100)
# slower_audio = slower_audio.set_frame_rate(44100)
#
# # Step 5: Save the modified audio files
# faster_audio.export("output_te_faster.mp3", format="mp3")
# slower_audio.export("output_te_slower.mp3", format="mp3")
#
# print("Audio files saved: 'output_te.mp3' (original), 'output_te_faster.mp3' (faster), 'output_te_slower.mp3' (slower)")




# # Load and modify pitch (example increases pitch by 2 semitones)
# audio = AudioSegment.from_mp3("output_te.mp3")
# pitched_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * 1.2)})
# pitched_audio = pitched_audio.set_frame_rate(audio.frame_rate)
#
# # Export with new pitch
# pitched_audio.export("output_te_pitched.mp3", format="mp3")
