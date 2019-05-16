from pages.page import Page


class MainPageLocalize(Page):
    def search(self, text):
        self.br.find_element_by_id('searchInput').send_keys(text)