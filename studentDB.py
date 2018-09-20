# ---------- studentdb.py  ----------

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import FadeTransition


# class StudentListButton(ListItemButton):
#     pass
#
#
# class StudentDB(BoxLayout):
#     # Connects the value in the TextInput widget to these
#     # fields
#     first_name_text_input = ObjectProperty()
#     last_name_text_input = ObjectProperty()
#     student_list = ObjectProperty()
#
#     def submit_student(self):
#         # Get the student name from the TextInputs
#         student_name = self.first_name_text_input.text + " " + \
#             self.last_name_text_input.text
#
#         # Add the student to the ListView
#         self.student_list.adapter.data.extend([student_name])
#
#         # Reset the ListView
#         self.student_list._trigger_reset_populate()
#
#     def delete_student(self, *args):
#         # If a list item is selected
#         if self.student_list.adapter.selection:
#             # Get the text from the item selected
#             selection = self.student_list.adapter.selection[0].text
#
#             # Remove the matching item
#             self.student_list.adapter.data.remove(selection)
#
#             # Reset the ListView
#             self.student_list._trigger_reset_populate()
#
#     def replace_student(self, *args):
#         # If a list item is selected
#         if self.student_list.adapter.selection:
#
#             # Get the text from the item selected
#             selection = self.student_list.adapter.selection[0].text
#
#             # Remove the matching item
#             self.student_list.adapter.data.remove(selection)
#
#             # Get the student name from the TextInputs
#             student_name = self.first_name_text_input.text + " " + \
#                 self.last_name_text_input.text
#
#             # Add the updated data to the list
#             self.student_list.adapter.data.extend([student_name])
#
#             # Reset the ListView
#             self.student_list._trigger_reset_populate()


class ClearWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = {}


class Painter(Widget):
    # id = "draw"

    def on_touch_down(self, touch):

        with self.canvas:
            touch.ud["line"] = Line(points=[touch.x, touch.y])

    def on_touch_move(self, touch):
        try:
            touch.ud["line"].points += [touch.x, touch.y]
        except KeyError as e:
            print e
        print touch.ud


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):

    def clear_screen(self, draw):
        print "clear_screen", self, draw
        print dir(self)
        print dir(draw)
        print draw.__dict__
        self.remove_widget(draw)
        # try:
        #     self.remove_widget(self.draw)
        # except:
        #     pass
        draw = Painter()
        self.add_widget(draw)


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("test.kv")


class MainApp(App):
    def build(self):
        return presentation


MainApp().run()
