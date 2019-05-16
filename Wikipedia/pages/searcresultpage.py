from pages.page import Page


class SearcResultPage(Page):
    def open_result(self, name):
        self.br.find_element_by_link_text(name).click()