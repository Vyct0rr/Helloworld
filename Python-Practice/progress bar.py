from rich.progress import Progress
import time

with Progress() as progress:
    task = progress.add_task("[red]Downloading...", total=100)

    while not progress.finished and progress.tasks[task].completed < 100:
        progress.update(task, advance=10)
        time.sleep(0.1)
