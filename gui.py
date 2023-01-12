import PySimpleGUI as gi
from extractor import extract_archive

gi.theme("Black")

label1= gi.Text("Select Archive: ")
input_box = gi.Input(size=40)
choose_button1 = gi.FileBrowse("Choose", key="archive")

label2= gi.Text("Select Directory: ")
input_box2 = gi.Input(size=40)
choose_button2 = gi.FolderBrowse("Choose", key="folder")

extract_button = gi.Button("Extract")
output_label = gi.Text(key="output", text_color="white")

window = gi.Window("Archive Extractor",
layout=[[label1, input_box, choose_button1],
         [label2, input_box2, choose_button2],
         [extract_button,output_label]  ])


while True:
    event, values =window.read()
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value="Extraction Completed")
    window.read()


    window.close()



