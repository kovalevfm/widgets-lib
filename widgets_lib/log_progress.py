import time
import ipywidgets as widgets
from datetime import timedelta
from IPython.display import display

def log_progress(sequence, name='Items'):
    size = len(sequence)
    start_time = time.time()
    every = max(1, int(size / 200))
    progress = widgets.IntProgress(min=0, max=size, value=0)
    label = widgets.HTML()
    box = widgets.VBox(children=[label, progress])
    display(box)
    index = 0
    for index, record in enumerate(sequence, 1):
        if index == 1 or index % every == 0:
            progress.value = index
            process_time = time.time() - start_time
            
            eta = process_time / ((index * 1.0 - 0.99) / size) - process_time
            label.value = u'{0}: {1} / {2}, in: {3}, eta: {4}'.format(name,
                                                                      index,
                                                                      size,
                                                                      timedelta(seconds=int(process_time)),
                                                                      timedelta(seconds=int(eta)))
        yield record
    progress.bar_style = 'success'
    progress.value = index
    process_time = time.time() - start_time
    label.value = "{0}: {1}, in {2}".format(name, index, timedelta(seconds=int(process_time)))
