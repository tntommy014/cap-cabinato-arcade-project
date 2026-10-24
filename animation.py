from microbit import Image, display, sleep  # type: ignore[reportMissingModuleSource]


def show_faces():
    display.show(Image.SAD)
    sleep(1000)
    display.show(Image.SMILE)
    sleep(1000)
