
import alexandre_lib as bell
import re
import sounddevice
from scipy.io.wavfile import write

fs=44110


name = str(input("Enter the name of Recording: "))
record_name = str(name + ".wav")
output_dir = r"C:\Users\Alexandre\Desktop" + r"\\" + record_name 
second = int(input("Enter the duration in seconds: "))
print("Recording...")
record_voice =sounddevice.rec(int(second*fs),samplerate=fs, channels=2)
sounddevice.wait()
write(record_name, fs, record_voice)
print("Finished...\nPLease Check it...")

url = output_dir

bell.winR(url)





