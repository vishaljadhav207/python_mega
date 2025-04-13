from itertools import compress

import FreeSimpleGUI as sg

label1 = sg.Text("Select file for compress:")
input1 = sg.Input()
choose = sg.FileBrowse("Choose")

label2 = sg.Text("Select folder destination:")
input2 = sg.Input()
choose2 = sg.FolderBrowse("Choose")

compress_=sg.Button("Compress")

window = sg.Window("File compressor",
                   layout=[[label1, input1, choose],
                           [label2, input2, choose2],
                           [compress_]])



window.read()
window.close()
