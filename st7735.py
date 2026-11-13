from microbit import pin1, pin13, pin14, pin15, pin16, sleep, spi  # type: ignore[reportMissingModuleSource]


_FONT_5X7 = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01111", "10000", "10000", "10000", "10000", "10000", "01111"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "G": ("01111", "10000", "10000", "10111", "10001", "10001", "01111"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "J": ("00111", "00010", "00010", "00010", "10010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "10000", "11110", "00001", "00001", "11110"),
    "6": ("01110", "10000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00001", "01110"),
    "a": ("00000", "00000", "01110", "00001", "01111", "10001", "01111"),
    "b": ("10000", "10000", "10110", "11001", "10001", "10001", "11110"),
    "c": ("00000", "00000", "01111", "10000", "10000", "10000", "01111"),
    "d": ("00001", "00001", "01101", "10011", "10001", "10001", "01111"),
    "e": ("00000", "00000", "01110", "10001", "11111", "10000", "01110"),
    "f": ("00110", "01001", "01000", "11100", "01000", "01000", "01000"),
    "g": ("00000", "01111", "10001", "10001", "01111", "00001", "01110"),
    "h": ("10000", "10000", "10110", "11001", "10001", "10001", "10001"),
    "i": ("00100", "00000", "01100", "00100", "00100", "00100", "01110"),
    "j": ("00010", "00000", "00110", "00010", "00010", "10010", "01100"),
    "k": ("10000", "10000", "10010", "10100", "11000", "10100", "10010"),
    "l": ("01100", "00100", "00100", "00100", "00100", "00100", "01110"),
    "m": ("00000", "00000", "11010", "10101", "10101", "10101", "10101"),
    "n": ("00000", "00000", "10110", "11001", "10001", "10001", "10001"),
    "o": ("00000", "00000", "01110", "10001", "10001", "10001", "01110"),
    "p": ("00000", "11110", "10001", "10001", "11110", "10000", "10000"),
    "q": ("00000", "01111", "10001", "10001", "01111", "00001", "00001"),
    "r": ("00000", "00000", "10110", "11001", "10000", "10000", "10000"),
    "s": ("00000", "00000", "01111", "10000", "01110", "00001", "11110"),
    "t": ("01000", "01000", "11100", "01000", "01000", "01001", "00110"),
    "u": ("00000", "00000", "10001", "10001", "10001", "10011", "01101"),
    "v": ("00000", "00000", "10001", "10001", "10001", "01010", "00100"),
    "w": ("00000", "00000", "10001", "10001", "10101", "10101", "01010"),
    "x": ("00000", "00000", "10001", "01010", "00100", "01010", "10001"),
    "y": ("00000", "10001", "10001", "10001", "01111", "00001", "01110"),
    "z": ("00000", "00000", "11111", "00010", "00100", "01000", "11111"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
    ":": ("00000", "00100", "00000", "00000", "00000", "00100", "00000"),
    "#": ("11111", "11111", "11111", "11111", "11111", "11111", "11111"),
}


class ST7735:
    WIDTH = 160
    HEIGHT = 128

    def __init__(self) -> None:
        self._dc = pin1
        self._cs = pin16
        self._cs.write_digital(1)
        self._dc.write_digital(1)
        self._pixel_buffer = bytearray(256)
        self._pixel_buffer_view = memoryview(self._pixel_buffer)
        self._text_areas = {}

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
        self._command_data(0x36, b"\xA0")
        self._command_data(0x2A, bytes((0, 0, 0, self.WIDTH - 1)))
        self._command_data(0x2B, bytes((0, 0, 0, self.HEIGHT - 1)))
        self._command(0x20)
        self._command(0x13)
        sleep(10)
        self._command(0x29)
        sleep(100)
        self.fill(0x0000)

    def draw_pixel(self, x: int, y: int, color: str) -> None:
        x = min(max(x, 0), self.WIDTH - 1)
        y = min(max(y, 0), self.HEIGHT - 1)
        self._write_run(x, y, x, y, self._color_to_rgb565(color))

    def draw_matrix(self, matrix: list, x: int, y: int, color: str) -> None:
        rgb565 = self._color_to_rgb565(color)

        for row, values in enumerate(matrix):
            pixel_y = y + row
            if not 0 <= pixel_y < self.HEIGHT:
                continue

            column = 0
            while column < len(values):
                while column < len(values) and values[column] != 1:
                    column += 1
                run_start = column
                while column < len(values) and values[column] == 1:
                    column += 1

                run_x0 = max(x + run_start, 0)
                run_x1 = min(x + column - 1, self.WIDTH - 1)
                if run_start < column and run_x0 <= run_x1:
                    self._write_run(run_x0, pixel_y, run_x1, pixel_y, rgb565)

    def move_sprite(
        self,
        sprite: list,
        old_x: int,
        old_y: int,
        x: int,
        y: int,
        color: str,
        background: str,
    ) -> None:
        if x == old_x and y == old_y:
            return

        sprite_height = len(sprite)
        sprite_width = max((len(row) for row in sprite), default=0)
        if not sprite_width or not sprite_height:
            return

        x0 = max(min(old_x, x), 0)
        y0 = max(min(old_y, y), 0)
        x1 = min(max(old_x, x) + sprite_width - 1, self.WIDTH - 1)
        y1 = min(max(old_y, y) + sprite_height - 1, self.HEIGHT - 1)
        if x0 > x1 or y0 > y1:
            return

        foreground = self._color_to_rgb565(color)
        background_rgb565 = self._color_to_rgb565(background)
        self._set_window(x0, y0, x1, y1)
        self._command(0x2C)
        self._cs.write_digital(0)
        self._dc.write_digital(1)

        region_width = x1 - x0 + 1
        remaining = region_width * (y1 - y0 + 1)
        offset = 0
        while remaining:
            pixels = min(remaining, len(self._pixel_buffer) // 2)
            for index in range(pixels):
                pixel_x = x0 + (offset + index) % region_width
                pixel_y = y0 + (offset + index) // region_width
                sprite_row = pixel_y - y
                sprite_column = pixel_x - x
                pixel_color = background_rgb565
                if (
                    0 <= sprite_row < sprite_height
                    and 0 <= sprite_column < len(sprite[sprite_row])
                    and sprite[sprite_row][sprite_column] == 1
                ):
                    pixel_color = foreground

                buffer_offset = index * 2
                self._pixel_buffer[buffer_offset] = pixel_color >> 8
                self._pixel_buffer[buffer_offset + 1] = pixel_color & 0xFF

            spi.write(self._pixel_buffer_view[:pixels * 2])
            offset += pixels
            remaining -= pixels

        self._cs.write_digital(1)

    def draw_text(self, text: str, x: int, y: int, color: str) -> None:
        lines = text.split("\n")
        for character in text:
            if character != "\n" and character not in _FONT_5X7:
                raise ValueError("unsupported character: " + character)

        rgb565 = self._color_to_rgb565(color)
        area = (x, y)
        previous_width, previous_height = self._text_areas.get(area, (0, 0))
        width = max((len(line) for line in lines), default=0) * 6
        height = len(lines) * 8
        clear_width = max(previous_width, width)
        clear_height = max(previous_height, height)
        x0 = max(x, 0)
        y0 = max(y, 0)
        x1 = min(x + clear_width - 1, self.WIDTH - 1)
        y1 = min(y + clear_height - 1, self.HEIGHT - 1)

        if width and height:
            self._text_areas[area] = (width, height)
        else:
            self._text_areas.pop(area, None)

        if x0 > x1 or y0 > y1:
            return

        self._set_window(x0, y0, x1, y1)
        self._command(0x2C)
        self._cs.write_digital(0)
        self._dc.write_digital(1)

        buffer_pixels = len(self._pixel_buffer) // 2
        region_width = x1 - x0 + 1
        foreground_high = rgb565 >> 8
        foreground_low = rgb565 & 0xFF
        offset = 0
        while offset < region_width * (y1 - y0 + 1):
            pixel_y = y0 + offset // region_width
            row_offset = offset % region_width
            pixels = min(buffer_pixels, region_width - row_offset)
            text_y = pixel_y - y
            line_number = text_y // 8
            glyph_row = text_y % 8

            for index in range(pixels):
                text_x = x0 + row_offset + index - x
                pixel_color = 0
                if 0 <= line_number < len(lines) and 0 <= text_x < width:
                    character_number = text_x // 6
                    glyph_column = text_x % 6
                    if glyph_row < 7 and glyph_column < 5:
                        line = lines[line_number]
                        if character_number < len(line):
                            glyph = _FONT_5X7[line[character_number]]
                            if glyph[glyph_row][glyph_column] == "1":
                                pixel_color = rgb565

                buffer_offset = index * 2
                self._pixel_buffer[buffer_offset] = (
                    foreground_high if pixel_color else 0
                )
                self._pixel_buffer[buffer_offset + 1] = (
                    foreground_low if pixel_color else 0
                )

            spi.write(self._pixel_buffer_view[:pixels * 2])
            offset += pixels

        self._cs.write_digital(1)

    def fill(self, color: int) -> None:
        if not 0 <= color <= 0xFFFF:
            raise ValueError("color must be a 16-bit RGB565 value")

        self._write_run(0, 0, self.WIDTH - 1, self.HEIGHT - 1, color)

    @staticmethod
    def _color_to_rgb565(color: str) -> int:
        if len(color) != 7 or color[0] != "#":
            raise ValueError("color must use #RRGGBB format")

        rgb = int(color[1:], 16)
        red = (rgb >> 16) & 0xFF
        green = (rgb >> 8) & 0xFF
        blue = rgb & 0xFF
        return ((red & 0xF8) << 8) | ((green & 0xFC) << 3) | (blue >> 3)

    def _write_run(self, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
        self._set_window(x0, y0, x1, y1)
        self._command(0x2C)

        high = color >> 8
        low = color & 0xFF
        remaining = (x1 - x0 + 1) * (y1 - y0 + 1)
        buffered_pixels = min(remaining, len(self._pixel_buffer) // 2)
        for offset in range(0, buffered_pixels * 2, 2):
            self._pixel_buffer[offset] = high
            self._pixel_buffer[offset + 1] = low

        self._cs.write_digital(0)
        self._dc.write_digital(1)
        while remaining:
            pixels = min(remaining, len(self._pixel_buffer) // 2)
            spi.write(self._pixel_buffer_view[:pixels * 2])
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
