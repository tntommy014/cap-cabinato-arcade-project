class Image:
    HEART: Image
    SAD: Image
    SMILE: Image


class _Display:
    def show(self, image: Image) -> None: ...


class _Pin:
    def write_digital(self, value: int) -> None: ...


class _SPI:
    def init(
        self,
        baudrate: int = ...,
        bits: int = ...,
        mode: int = ...,
        sclk: _Pin = ...,
        mosi: _Pin = ...,
        miso: _Pin = ...,
    ) -> None: ...

    def write(self, data: bytes) -> None: ...


display: _Display
pin1: _Pin
pin14: _Pin
pin13: _Pin
pin15: _Pin
pin16: _Pin
spi: _SPI


def sleep(milliseconds: int | float) -> None: ...
