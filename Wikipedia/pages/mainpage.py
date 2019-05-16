from pages.page import Page


class MainPage(Page):
    def open_lang_list(self):
        self.br.find_element_by_class_name('lang-list-button-text').click()
    def switch_to_language(self, lang):
        lang_list = self.br.find_element_by_class_name('lang-list-content')
        lang_list.find_element_by_link_text(lang).click()