from os import path as op
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

path = op.dirname(op.realpath(__file__))
print(f'Ruta = {path}')
path_kv = op.join(path, 'kv')
print(f'KV = {path_kv}')
path_utils = op.join(path_kv, 'utils.kv')
print(f'Utils = {path_utils}')
path_find_device = op.join(path_kv, 'find_device.kv')

Builder.load_file(op.join(path_kv, 'screens.kv'))


class BluiGui(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return BluiGui()

if __name__ == '__main__':
    MyApp().run()
