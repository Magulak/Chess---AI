# @sajaner Pygame is cool and powerfull liblary, but I want to check out PySimpleGUI and see where it will be easier
# to build I checked out tkinker and qt too. PySimpleGUI says "Transforms the tkinter, Qt, WxPython,
# and Remi (browser-based) GUI frameworks into a simpler interface."

# Depending on the program and framework used, a PySimpleGUI program may require 1/2 to 1/10th amount of code to
# create an identical window using one of the frameworks directly.
# https://github.com/PySimpleGUI/PySimpleGUI


import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Sup ' + values['-INPUT-'] + "! Time to code some chess!")

# Finish up by removing from the screen
window.close()