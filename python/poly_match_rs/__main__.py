from jsonargparse import CLI
from .baseline import main as baseline_main
from .v0 import main as v0_main
from .v1 import main as v1_main
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.align import Align


def benchmark():
    console = Console()
    table = Table(title="Benchmark Results")
    table_centered = Align.center(table)
    table.add_column("Version")
    table.add_column("Time per iteration (ms)")
    table.add_column("Speedup")
    with Live(table_centered, console=console, refresh_per_second=2):
        baseline_took = baseline_main()
        table.add_row("baseline", f"{baseline_took * 1000:.2f}", "-")
        v0_took = v0_main()
        table.add_row("v0", f"{v0_took * 1000:.2f}", f"{baseline_took / v0_took:.2f}")
        v1_took = v1_main()
        table.add_row("v1", f"{v1_took * 1000:.2f}", f"{baseline_took / v1_took:.2f}")


def main():
    components = {
        "benchmark": benchmark,
    }

    CLI(components=components)
