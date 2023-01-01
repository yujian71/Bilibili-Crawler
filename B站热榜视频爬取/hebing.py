
import os
import subprocess

list = os.listdir('D:/B站视频')
a = []
for i in list:
    i = i.split(".")[0]
    a.append(i)
a = set(a)
for i in a:
    try:
        cmd = f"ffmpeg -i D:/B站视频/{i}.mp4 -i D:/B站视频/{i}.mp3 -c:v copy -c:a aac -strict experimental D:/B站视频/{i}_output.mp4 -loglevel quiet -n"
        subprocess.run(cmd, shell=True)
        os.remove(f'D:/B站视频/{i}.mp3')
        os.remove(f'D:/B站视频/{i}.mp4')
        print(f'{i}完成')
    except FileNotFoundError:
        continue
