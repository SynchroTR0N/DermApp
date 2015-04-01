from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button

from kivy.core.window import Window

class DermRoot(BoxLayout):
    dict_filled_from_form = {}
    def add_entry_to_db(self,dict_filled_from_form):
        pass

class DemographForm(BoxLayout):
    data = {}

    __events__ = ('on_save', )

    def on_save(self, data):
        pass

    def edit(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = {} 

    # def dwn_norm_to_bin(self, key, state):
    #     if state == 'down':
    #         self.data[key] = 1
    #     else:
    #         self.data[key] = 0

    def add_entry(self,dict_of_form):
        dict_filled_from_form = dict_of_form
        #is this possible?
        #or do I have to do dict_filled_from_form['series1'] = series1.value etc

class DermApp(App):
    pass

if __name__ == '__main__':
    DermApp().run()
