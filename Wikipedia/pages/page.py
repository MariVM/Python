class Page():
    def __init__(self, browser):
        self.br = browser
    @property
    def title(self):
        return self.br.title