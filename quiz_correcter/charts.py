import colorsys

from rich.color import Color
from rich.console import Console, ConsoleOptions, Group, RenderableType, RenderResult
from rich.measure import Measurement
from rich.segment import Segment
from rich.style import Style

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel



class ColorBox:
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        for y in range(0, 5):
            for x in range(options.max_width):
                h = x / options.max_width
                l = 0.1 + ((y / 5) * 0.7)
                r1, g1, b1 = colorsys.hls_to_rgb(h, l, 1.0)
                r2, g2, b2 = colorsys.hls_to_rgb(h, l + 0.7 / 10, 1.0)
                bgcolor = Color.from_rgb(r1 * 255, g1 * 255, b1 * 255)
                color = Color.from_rgb(r2 * 255, g2 * 255, b2 * 255)
                yield Segment("▄", Style(color=color, bgcolor=bgcolor))
            yield Segment.line()

    def __rich_measure__(
        self, console: "Console", options: ConsoleOptions
    ) -> Measurement:
        return Measurement(1, options.max_width)



console = Console()
#charts = [
#    doughnut({'a':10, 'b': 20, 'c': 30, 'd': 20}, title='aphabet dist', rich=True),
#    pie({'wefwefqwddwqdqwda':10, 'b': 20, 'c': 30, 'd': 20}, rich=True),
#    bar({'roll': 24, 'bss':10, 'wes':30, 'ewfwef':50}, title='Brunches', rich=True)
#    ]
#user_renderables = [Panel(x, expand=True) for x in charts]
#console.print(Columns(user_renderables))
console.print(ColorBox())
