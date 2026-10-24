from microbit import pin1, pin13, pin14, pin15, pin16, sleep, spi  # type: ignore[reportMissingModuleSource]


class ST7735:
    WIDTH = 128
    HEIGHT = 160

    def __init__(self) -> None:
        self._dc = pin1
        self._cs = pin16
        self._cs.write_digital(1)
        self._dc.write_digital(1)

        spi.init(baudrate=8_000_000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14)

        self._command(0x01)
        sleep(150)
        self._command(0x11)
        sleep(150)
        self._command_data(0xB1, b"\x01\x2C\x2D")
        self._command_data(0xB2, b"\x01\x2C\x2D")
        self._command_data(0xB3, b"\x01\x2C\x2D\x01\x2C\x2D")
        self._command_data(0xB4, b"\x07")
        self._command_data(0xC0, b"\xA2\x02\x84")
        self._command_data(0xC1, b"\xC5")
        self._command_data(0xC2, b"\x0A\x00")
        self._command_data(0xC3, b"\x8A\x2A")
        self._command_data(0xC4, b"\x8A\xEE")
        self._command_data(0xC5, b"\x0E")
        self._command_data(0x3A, b"\x05")
        self._command_data(0x36, b"\xC0")
        self._command_data(0x2A, b"\x00\x00\x00\x7F")
        self._command_data(0x2B, b"\x00\x00\x00\x9F")
        self._command(0x20)
        self._command(0x13)
        sleep(10)
        self._command(0x29)
        sleep(100)
        self.fill(0x0000)

    def draw_pixel(self, x: int, y: int, color: str) -> None:
        if not 0 <= x < self.WIDTH or not 0 <= y < self.HEIGHT:
            raise ValueError("pixel coordinates are outside the display")
        if len(color) != 7 or color[0] != "#":
            raise ValueError("color must use #RRGGBB format")

        rgb = int(color[1:], 16)
        red = (rgb >> 16) & 0xFF
        green = (rgb >> 8) & 0xFF
        blue = rgb & 0xFF
        color = ((red & 0xF8) << 8) | ((green & 0xFC) << 3) | (blue >> 3)

        self._set_window(x, y, x, y)
        self._command(0x2C)
        self._data(bytes((color >> 8, color & 0xFF)))

    def fill(self, color: int) -> None:
        if not 0 <= color <= 0xFFFF:
            raise ValueError("color must be a 16-bit RGB565 value")

        self._set_window(0, 0, self.WIDTH - 1, self.HEIGHT - 1)
        self._command(0x2C)

        pixel = bytes((color >> 8, color & 0xFF))
        chunk = pixel * 64
        remaining = self.WIDTH * self.HEIGHT
        self._cs.write_digital(0)
        self._dc.write_digital(1)
        while remaining:
            pixels = min(remaining, 64)
            spi.write(chunk if pixels == 64 else pixel * pixels)
            remaining -= pixels
        self._cs.write_digital(1)

    def _set_window(self, x0: int, y0: int, x1: int, y1: int) -> None:
        self._command_data(0x2A, bytes((0, x0, 0, x1)))
        self._command_data(0x2B, bytes((0, y0, 0, y1)))

    def _command(self, command: int) -> None:
        self._cs.write_digital(0)
        self._dc.write_digital(0)
        spi.write(bytes((command,)))
        self._cs.write_digital(1)

    def _data(self, data: bytes) -> None:
        self._cs.write_digital(0)
        self._dc.write_digital(1)
        spi.write(data)
        self._cs.write_digital(1)

    def _command_data(self, command: int, data: bytes) -> None:
        self._command(command)
        self._data(data)
