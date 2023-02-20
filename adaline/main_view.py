import PySimpleGUI as sg

def make_window():
    sg.theme('SystemDefault')
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']] ]

    input_grid_namager = [[sg.Text('Input', font='bold 14')],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB0{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB1{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB2{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB3{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB4{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB5{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB6{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB7{i}') for i in range (0,6)],
                          [sg.Checkbox('', pad=(0,0), key=f'-CB8{i}') for i in range (0,6)],
                        ]
    input_selectors_manager = [
                               [sg.Combo(['Val1', 'Val2', 'Val3'], 'Val1', size=10)],
                               [sg.Button('Classify', size=10)],
                              ]
    #TODO Add animated error x epoch graph, updated while training
    graph_manager_layout = [[sg.Text('Error x Epoch Graph', font='bold 14')]]

    layout = [[sg.MenubarCustom(menu_def, key='-MENU-')], 
              [sg.Text('Training parameters', font='bold 14')],
              [sg.Text('Learning Rate', size=10, justification='right', tooltip='Learning rate used in training. Use values between 0.0 and 1.0.'), sg.Input(key='-LEARNING_RATE-')],
              [sg.Text('Epochs', size=10, justification='right', tooltip='Max number of epochs to be used in training.'), sg.Input(key='-MAX_EPOCHS-')],
              [sg.Text('Minimum error', size=10, justification='right', tooltip='Error value that stops training once achieved. Use values between 0.0 and 1.0'), sg.Input(key='-MIN_ERROR-')],
              [sg.Button('Train', size=15)],
              [sg.HSeparator()],
              [sg.Column(input_grid_namager), sg.Column(input_selectors_manager, vertical_alignment='top'), sg.VSeparator(), sg.Column(graph_manager_layout)]
            ]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('Adaline', layout, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window

#TODO handle main_view events (train, classify)
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
    window.close()
    exit(0)

main()