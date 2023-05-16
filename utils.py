import os

import soundfile as sf


def rename_audio(path="./data/jay"):
    num = 0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file_path.endswith(".wav"):
            file_new_path = os.path.join(path, f"A-{str(num).zfill(3)}.wav")
            os.rename(file_path, file_new_path)
            num += 1
            print(file_new_path)


def filter_audio(file_dir="./data/jay"):
    for file in os.listdir(file_dir):
        file_path = os.path.join(file_dir, file)
        data, samplerate = sf.read(file_path)
        channels = len(data.shape)
        length_s = len(data) / float(samplerate)
        if (length_s < 3.0):
            os.remove(file_path)
            print(file_path)


if __name__ == '__main__':
    rename_audio()
    # filter_audio()
