from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('gui.kv')

class MyLayout(Widget):
    def selected(self,filename):
        try:
            self.ids.my_video.source = filename[0]
        except:
            pass    

class vidPdfier(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    vidPdfier().run()
