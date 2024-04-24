import os
import PySimpleGUI as py
from PIL import Image
import pillow_heif


# Creating GUI for Ap
label = py.Text("Choose HEIC Folder")

input_box = py.InputText()

choose_button = py.FolderBrowse("Choose", key='source')

convert_button = py.Button("Convert")

window = py.Window("HEIC Converter", layout=[[label, input_box, choose_button], [convert_button]])


def convert_heic_to_jpeg(heic_path, jpeg_path):
        img = Image.open(heic_path)
        img.save(jpeg_path, format='JPEG')
    
    
def convert_all_heic_to_jpeg(input_folder, output_folder):
    # Register HEIF opener with Pillow
    pillow_heif.register_heif_opener()

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in input folder
    for filename in os.listdir(input_folder):
        # Check if file is a HEIC file
        if filename.endswith(".heic") or filename.endswith(".HEIC"):
            # Build full path to input and output file
            heic_path = os.path.join(input_folder, filename)
            jpeg_filename = f'{os.path.splitext(filename)[0]}.jpg'
            jpeg_path = os.path.join(output_folder, jpeg_filename)
            # Convert HEIC to JPEG
            convert_heic_to_jpeg(heic_path, jpeg_path)



while True:
    event, values = window.read()
    input_folder = values['source']
    output_folder = values['source'] + r'\converted'
    convert_all_heic_to_jpeg(input_folder, output_folder)