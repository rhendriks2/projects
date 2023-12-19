import tkinter

import requests
import json
from tkinter import filedialog


def get_pdf_file_as_binary_stream(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        pdf_file_binary_stream = f.read()
    return pdf_file_binary_stream


def convert_pdf_to_speech(pdf_file_binary_stream):
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",

    }

    request_body = {
        "input": {
            "type": "BYTES",
            "value": pdf_file_binary_stream.encode("base64"),

        },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Wavenet-A",
        },
        "audioConfig": {
            "audioEncoding": "MP3",
        },

    }
    response = requests.post("https://texttospeech.googleapis.com/v1beta1/text:synthesize",
                             headers=headers,
                             json=request_body,
                             )

    if response.status_code != 200:
        raise Exception("Failed to convert pdf to speech {}".format(response.status_code))

    audio_content = response.json()["audioContent"]

    decoded_audio_content = audio_content.decode("base64")

    return decoded_audio_content


def save_audio_content_to_file(audio_content, file_path):
    with open(file_path, "wb") as f:
        f.write(audio_content)

    pdf_file_binary_stream = get_pdf_file_as_binary_stream()

    audio_content = convert_pdf_to_speech()

    save_audio_content_to_file(audio_content, audio_file_path)


def get_pdf_file_path():
    root = tkinter.Tk()
    root.withdraw()
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])


def main():
    pdf_file_path = get_pdf_file_path()
    audio_file_path = filedialog.asksaveasfilename(filetypes=[("MP3 files", "*.mp3")])
    convert_pdf_to_speech_and_save_audio_to_file(pdf_file_path, audio_file_path)


if __name__ == "__main__":
    main()
