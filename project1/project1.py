from abc import ABC, abstractmethod
from PIL import Image
import wave
import numpy as np
from pydub import AudioSegment
import contextlib

class File(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def edit(self):
        pass

class TextFile(File):
    def __init__(self, file_path,content=""):
        self.file_path = file_path
        self.content = content

    def read(self):
        with open(self.file_path, 'r') as file:
            self.content = file.read()

    def write(self):
        with open(self.file_path, 'w') as file:
            file.write(self.content)

    def edit(self, new_content):
        self.content += new_content

class ImageFile(File):
    def __init__(self, file_path):
        self.file_path = file_path
        self.image = None

    def read(self):
        self.image = Image.open(self.file_path)

    def write(self):
        self.image.save(self.file_path)

    def edit(self, resize_box):
        self.image = self.image.resize(resize_box)

class AudioFile(File):
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio = None

    def read(self):
        with contextlib.closing(wave.open(self.file_path, 'rb')) as file:
            self.audio = file.readframes(file.getnframes())

    def write(self, output_path):
        # Load the audio file
        with wave.open(self.file_path, 'rb') as wf:
            params = wf.getparams()
            frames = wf.readframes(wf.getnframes())

        # Convert frames to numpy array
        audio_data = np.frombuffer(frames, dtype=np.int16)

        # Write the audio data to a new file
        with wave.open(output_path, 'wb') as wf:
            wf.setparams(params)
            wf.writeframes(audio_data.tobytes())

    def edit(self, speed_factor):
        audio_segment = AudioSegment.from_file(self.file_path)
        modified_audio = audio_segment.speedup(playback_speed=speed_factor)
        modified_audio.export(self.file_path, format="wav")
    
class FileFactory:
    @staticmethod
    def create_file(file_type, file_path):
        if file_type == 'text':
            return TextFile(file_path)
        elif file_type == 'image':
            return ImageFile(file_path)
        elif file_type == 'audio':
            return AudioFile(file_path)
        else:
            raise ValueError("Unsupported file type")
        
def main():
    #=========================== TEXT INSTANCE ===========================
    #create txt file
    text_file = FileFactory.create_file('text', 'example.txt')
    #write it (make a real txt file)
    text_file.write()
    #read txt file
    text_file.read()
    #edit & put it in file
    text_file.edit("\nThis is new content.")
    text_file.write()
    #=========================== IMG INSTANCE ===========================
    image_file = FileFactory.create_file('image', 'example.jpg')
    image_file.read()
    image_file.write()
    print("Image size before resize:", image_file.image.size)
    image_file.edit((600,306))
    image_file.write()
    print("Image size after resize:", image_file.image.size)

    #=========================== Audio INSTANCE ===========================
    audio_file = FileFactory.create_file('audio', 'example.wav')
    audio_file.read()
    audio_file.edit(speed_factor=1.5)
    audio_file.write("output.wav")

if __name__ == "__main__":
    main()