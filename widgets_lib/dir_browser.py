import os
import ipywidgets as widgets


class DirBrowser(widgets.VBox):
    def __init__(self, path=None, **kwargs):
        widgets.VBox.__init__(self, **kwargs)
        self.path = path or os.getcwd()
        self.select = widgets.Dropdown(description='Dirs', options=[".."], value="..")
        self.go = widgets.Button(description='Go')
        self.hbox = widgets.HBox()
        self.header = widgets.HTML("<h4>{0}</h4>".format(self.path))
        self.go.on_click(self._on_click)
        self.hbox.children = (self.select, self.go)
        self.children = (self.hbox, self.header)
        self._update()
        
    def _update(self):
        f_dict = [".."]
        for f in os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path, f)):
                f_dict.append(f)
        self.select.options = f_dict

    def _on_click(self, b):
        if self.select.value == "..":
            self.path = os.path.dirname(self.path)
        else:
            self.path = os.path.join(self.path, self.select.value)
        self.header.value = "<h4>{0}</h4>".format(self.path)
        self._update()