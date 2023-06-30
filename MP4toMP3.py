from moviepy.editor import *

def MP4ToMP3(mp4, mp3):
    file_convert = AudioFileClip(mp4)
    file_convert.write_audiofile(mp3)
    file_convert.close()

mp4_file_name = input("Enter MP4-file name: ")
mp3_file_name = input("Enter MP3-file name: ")

mp4_file_path = mp4_file_name
mp3_file_path = mp3_file_name

MP4ToMP3(mp4_file_path, mp3_file_path)
