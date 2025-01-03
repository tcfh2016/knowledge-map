import dearpygui.dearpygui as dpg

dpg.create_context()


class Window:

    def __init__(self, label):
        self._children = []
        with dpg.stage() as stage:
            self.id = dpg.add_window(label=label)
        self.stage = stage

    def add_child(self, child):
        dpg.move_item(child.id, parent=self.id)

    def submit(self):
        dpg.unstage(self.stage)


class Button:

    def __init__(self, label):
        with dpg.stage():
            self.id = dpg.add_button(label=label)

    def set_callback(self, callback):
        dpg.set_item_callback(self.id, callback)


my_button = Button("Press me")
my_button.set_callback(lambda: print("I've been pressed!"))

my_window = Window("Tutorial")

my_window.add_child(my_button)

my_window.submit()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()