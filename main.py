from kivy.app import App
from kivy.uix.video import Video
import time


class SimpleApp(App):
    def build(self):
        stream = Video(source="rtsp://admin:admin@192.168.1.2/1/1", play=True)
        return stream


if __name__ == "__main__":
    SimpleApp().run()