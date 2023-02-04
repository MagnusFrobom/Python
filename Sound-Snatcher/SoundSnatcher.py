import youtube_dl
import ffmpeg

# Set the URL of the YouTube video
url = "https://www.youtube.com/watch?v=-teK_6JX9gc"

# Use youtube_dl to download the video
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Use ffmpeg to extract the audio from the video
input_file = "./video.mp4"
output_file = "./audio.mp3"
ffmpeg_command = (
    "ffmpeg -i {input_file} -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 {output_file}"
).format(input_file=input_file, output_file=output_file)

# Execute the ffmpeg command
ffmpeg.input(ffmpeg_command).run()
