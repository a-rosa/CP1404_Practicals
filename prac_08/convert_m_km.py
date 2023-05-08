from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConvertKilometer(App):
    def build(self):
        self.title = "Convert Miles to Kilometer"
        self.root = Builder.load_file("convert_m_km.kv")
        return self.root

    def handle_increment(self, amount):
        value = self.get_valid_miles() + amount
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_calculate(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_kilometer.text = str(result)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConvertKilometer().run()
