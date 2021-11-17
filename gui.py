from main import probe_movement
import PySimpleGUI as sg


sg.theme("DarkAmber")

layout = [
    [sg.Text("Valor de X", size=(15, 1)), sg.InputText(key="x", size=(15, 1))],
    [sg.Text("Valor de Y", size=(15, 1)), sg.InputText(key="y", size=(15, 1))],
    [sg.Text("Posição", size=(15, 1)), sg.InputText(key="direction", size=(15, 1))],
    [sg.Text("Comando", size=(15, 1)), sg.InputText(key="command", size=(15, 1))],
    [sg.Button("Ok", border_width=5), sg.Button("Cancel", border_width=5)],
]

window = sg.Window(
    "Explorando marte", layout, size=(400, 180), element_justification="center"
)

input_key_list = [key for key, value in window.key_dict.items()
    if isinstance(value, sg.InputText)]

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    if all(map(str.strip, [values[key] for key in input_key_list])):
        probe_location = probe_movement(**values)
        sg.popup(probe_location, title="Result", keep_on_top=True)
    else:
        sg.popup_error("Fill all fields", title="Error", keep_on_top=True)

window.close()
