import PySimpleGUI as sg
import numpy as np

DEFAULT_MAX_EPOCHS = 5
DEFAULT_MIN_ERROR = 0.05
DEFAULT_LEARNING_RATE = 0.1


def make_window():
    sg.theme('DarkBlue')
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]

    layout = [[sg.MenubarCustom(menu_def, key='-MENU-')],
              [sg.Text('Training parameters', font='bold 14')],
              [sg.Text('Learning Rate', size=15, justification='right',
                       tooltip='Learning rate used in training. Use values between 0.0 and 1.0.'),
               sg.Input(key='-LEARNING_RATE-', default_text=DEFAULT_LEARNING_RATE)],
              [sg.Text('Epochs', size=15, justification='right',
                       tooltip='Max number of epochs to be used in training.'),
               sg.Input(key='-MAX_EPOCHS-', default_text=DEFAULT_MAX_EPOCHS)],
              [sg.Text('Minimum error', size=15, justification='right',
                       tooltip='Error value that stops training once achieved. Use values between 0.0 and 1.0'),
               sg.Input(key='-MIN_ERROR-', default_text=DEFAULT_MIN_ERROR)],
              [sg.Button('Train', size=15)],
              [sg.HSeparator()],
              [sg.Canvas(key='-CANVAS-')]
              ]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('MLP - Func. Aprox.', layout, grab_anywhere=True, resizable=True, margins=(0, 0), use_custom_titlebar=True,
                       finalize=True, keep_on_top=True, size=(800,600))

    window.set_min_size(window.size)
    return window


# TODO handle classify
def main():
    global MADALINE, CURRENT_COMBO_VALUE
    window = make_window()
    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            print('[LOG] Clicked Exit!')
            break
        elif event == 'About':
            print('[LOG] Clicked About!')
            sg.popup('MLP Network - Function aproximation',
                     'Enter training parameters on the input fields',
                     'Accepted parameters: Learning rate, epochs, minimum error',
                     'Press "Train" to train the network, and see it\'s graph on the graph panel',
                     'Authors: C. S. Julia; S. R. Nathan. 2023 - IFTM',
                     keep_on_top=True)
        elif event == 'Train':
            print('[LOG] Clicked Train')
            #TODO implement train
        elif event == 'Classify':
            print('[LOG] Clicked Classify')
            #TODO Implement classify function
    window.close()
    exit(0)


main()
