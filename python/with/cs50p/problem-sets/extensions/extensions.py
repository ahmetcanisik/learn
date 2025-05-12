#!/usr/bin/env python
mime_types = [
    {"extensions": ["jpg", "jpeg"], "mime_type": "image/jpeg"},
    {"extensions": ["png"], "mime_type": "image/png"},
    {"extensions": ["gif"], "mime_type": "image/gif"},
    {"extensions": ["bmp"], "mime_type": "image/bmp"},
    {"extensions": ["webp"], "mime_type": "image/webp"},
    {"extensions": ["mp3"], "mime_type": "audio/mpeg"},
    {"extensions": ["wav"], "mime_type": "audio/wav"},
    {"extensions": ["ogg"], "mime_type": "audio/ogg"},
    {"extensions": ["flac"], "mime_type": "audio/flac"},
    {"extensions": ["mp4"], "mime_type": "video/mp4"},
    {"extensions": ["mov"], "mime_type": "video/quicktime"},
    {"extensions": ["avi"], "mime_type": "video/x-msvideo"},
    {"extensions": ["webm"], "mime_type": "video/webm"},
    {"extensions": ["mkv"], "mime_type": "video/x-matroska"},
    {"extensions": ["pdf"], "mime_type": "application/pdf"},
    {"extensions": ["zip"], "mime_type": "application/zip"},
    {"extensions": ["json"], "mime_type": "application/json"},
    {"extensions": ["xml"], "mime_type": "application/xml"},
    {"extensions": ["csv"], "mime_type": "text/csv"},
    {"extensions": ["txt"], "mime_type": "text/plain"},
    {"extensions": ["html", "htm"], "mime_type": "text/html"},
    {"extensions": ["css"], "mime_type": "text/css"},
    {"extensions": ["js"], "mime_type": "application/javascript"},
    {"extensions": ["doc"], "mime_type": "application/msword"},
    {
        "extensions": ["docx"],
        "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    },
    {"extensions": ["ppt"], "mime_type": "application/vnd.ms-powerpoint"},
    {
        "extensions": ["pptx"],
        "mime_type": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    },
    {"extensions": ["xls"], "mime_type": "application/vnd.ms-excel"},
    {
        "extensions": ["xlsx"],
        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    },
    {"extensions": ["bin"], "mime_type": "application/octet-stream"},
]


def find_mime_type(file: str = None):
    if file is None:
        raise ValueError("File name is required")

    file_ext = file.split(".")[-1]

    if "." not in file:
        print("application/octet-stream")
        return

    for mime in mime_types:
        if file_ext in mime["extensions"]:
            print(mime["mime_type"])
            return


def main():
    # up is user prompt
    up = input("File name: ").strip().lower()

    find_mime_type(up)


if __name__ == "__main__":
    main()
