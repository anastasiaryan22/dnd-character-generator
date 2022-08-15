from turtle import textinput
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
import requests 
import json

class MainWidget(Widget):
    pass

class TheLabApp(App):
    def build(self):
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=40)
        screen = Screen()
        #spell = TextInput(text = '', multiline=False)
        self.spell = TextInput(hint_text = "Enter Spell", multiline=False)
        self.spell_variable = self.spell.text
        button = Button(text="Get Spell", on_release=self.submit)
        layout.add_widget(self.spell)
        layout.add_widget(button)
        
        return layout

    def submit(self, obj):
        user_input = self.spell_variable
        #making input into url ready thingy

        making_string = ''.join(str(x) for x in user_input)

        x = '-'.join(making_string.split())
        url = requests.get('https://www.dnd5eapi.co/api/spells/' + x)

        #making it look pretty
        pretty_spells = json.dumps(url.json(), indent=2)

        #making it so I can get values from json 
        resp = json.loads(pretty_spells)

        #print(resp['name'])
        print(resp['range'])
        #getting the components out of a list
        components_list = resp['components']
        components_strings = ''.join(str(x) for x in components_list)
        print(components_strings)

        #print only if it has a material component
        if 'material' in resp:
            print(resp['material'])

        print(resp['duration'])
        print("Concentration: ", resp['concentration'])
        print("Ritual: ", resp['ritual'])

        #getting the description out of a list
        description_list = resp['desc']
        description_strings = ''.join(str(x) for x in description_list)
        print(description_strings)

        #getting higher levels out of a list
        higher_level_list = resp['higher_level']
        higher_level_strings = ''.join(str(x) for x in higher_level_list)
        print(higher_level_strings)

        print("Level: ", resp['level'])
        print(resp['school']['name'])


TheLabApp().run()