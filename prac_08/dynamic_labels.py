from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Winnie", "Davy", "Hattie", "Tony", "Raynard"]

class DynamicLabelApp(App):

    def build(self):
        self.title = "Dynamic Label"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.enteries_label.add_widget(temp_label)

DynamicLabelApp().run()