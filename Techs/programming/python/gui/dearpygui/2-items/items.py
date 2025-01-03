import dearpygui.dearpygui as dpg

dpg.create_context()

def change_text(sender):
    app_data = 'hello'
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")

with dpg.window(width=500, height=300):
    text_flag = dpg.add_button(label="Click me with any mouse button", tag="text item")
    print(text_flag)
    #with dpg.item_handler_registry(tag="widget handler") as handler:
    #    dpg.add_item_clicked_handler(callback=change_text)
    #dpg.bind_item_handler_registry("text item", "widget handler")
    dpg.set_item_callback(text_flag, change_text)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()