import PySimpleGUI as sg
import numpy as np
import network_elements as ne
import graph_generator as graph

COMBO_VALUES = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3','E1','E2','E3','J1','J2','J3','K1','K2','K3']
CHARACTERS = np.loadtxt(open("docs/x.csv", "rb"), delimiter=",", skiprows=0)
MADALINE = ne.Madaline()
CURRENT_COMBO_VALUE = 'A1'

DEFAULT_MAX_EPOCHS = 5
DEFAULT_MIN_ERROR = 0.05
DEFAULT_LEARNING_RATE = 0.1


def update_character(window, char_id):
    index = COMBO_VALUES.index(char_id)
    char_data = CHARACTERS[index]
    print(f'Update_character: char_data={char_data}')
    i = 0
    k = 0
    while i < 9:
        j = 0
        while j < 7:
            if char_data[k] == 1:
                window[f'-CB{i}{j}'].update(value=True)
            else:
                window[f'-CB{i}{j}'].update(value=False)
            k += 1
            j += 1
        i += 1
    

def make_window():
    sg.theme('SystemDefault')
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]

    input_grid_manager = [[sg.Text('Input', font='bold 14')],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB0{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB1{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB2{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB3{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB4{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB5{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB6{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB7{i}') for i in range(0, 7)],
                          [sg.Checkbox('', pad=(0, 0), key=f'-CB8{i}') for i in range(0, 7)],
                          ]
    input_selectors_manager = [
        [sg.Combo(COMBO_VALUES, 'A1', size=10, key='-COMBO_BOX-', enable_events=True, readonly=True)],
        [sg.Button('Classify', size=10, disabled=True)],
        [sg.Text('', key='-ANS_TXT-')]
    ]

    layout = [[sg.MenubarCustom(menu_def, key='-MENU-')],
              [sg.Text('Training parameters', font='bold 14')],
              [sg.Text('Learning Rate', size=10, justification='right',
                       tooltip='Learning rate used in training. Use values between 0.0 and 1.0.'),
               sg.Input(key='-LEARNING_RATE-', default_text=DEFAULT_LEARNING_RATE)],
              [sg.Text('Epochs', size=10, justification='right',
                       tooltip='Max number of epochs to be used in training.'), sg.Input(key='-MAX_EPOCHS-', default_text=DEFAULT_MAX_EPOCHS)],
              [sg.Text('Minimum error', size=10, justification='right',
                       tooltip='Error value that stops training once achieved. Use values between 0.0 and 1.0'),
               sg.Input(key='-MIN_ERROR-', default_text=DEFAULT_MIN_ERROR)],
              [sg.Button('Train', size=15)],
              [sg.HSeparator()],
              [sg.Column(input_grid_manager, vertical_alignment='top'), sg.Column(input_selectors_manager, vertical_alignment='top'),
               sg.VSeparator(), sg.Canvas(key='-CANVAS-')]
              ]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('Adaline', layout, grab_anywhere=True, resizable=True, margins=(0, 0), use_custom_titlebar=True,
                       finalize=True, keep_on_top=True)

    graph.draw_initial_graph(window['-CANVAS-'].TKCanvas)

    window.set_min_size(window.size)
    return window


# TODO handle classify
def main():
    window = make_window()
    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            print('[LOG] Clicked Exit!')
            break
        elif event == 'About':
            print('[LOG] Clicked About!')
            sg.popup('Adaline NetworkTrainer',
                     'Enter training parameters on the input fields',
                     'Accepeted parameters: Learning rate, epochs, minimum error',
                     'Press "Train" to train the network, and see it\'s graph on the graph panel',
                     'Test pre-made or custom inputs using the menu on the left',
                     'Authors: C. S. Julia; S. R. Nathan. 2023 - IFTM',
                     keep_on_top=True)
        elif event == 'Train':
            print('[LOG] Clicked Train')
            learning_rate = float(values['-LEARNING_RATE-'])
            max_epochs = float(values['-MAX_EPOCHS-'])
            min_error = float(values['-MIN_ERROR-'])
            print(f'[LOG] Calling Train method on network_elements. Values=(learning_rate={learning_rate}, max_epochs={max_epochs}, minimum_error={min_error})')
            MADALINE = ne.train(window, learning_rate, max_epochs, min_error)
            window['Classify'].update(disabled=False)
        elif event == 'Classify':
            print('[LOG] Clicked Classify')
            CURRENT_COMBO_VALUE = values['-COMBO_BOX-']
            response = MADALINE.classify(COMBO_VALUES.index(CURRENT_COMBO_VALUE))
            print(f'[LOG] Classify response: {response}')
            window['-ANS_TXT-'].update(f'{response}')
            #TODO Update a text element with the response
        elif event == '-COMBO_BOX-':
            CURRENT_COMBO_VALUE = values['-COMBO_BOX-']
            print(f'[LOG] Combo box changed, value = {CURRENT_COMBO_VALUE}')
            update_character(window, CURRENT_COMBO_VALUE)
    window.close()
    exit(0)


main()
