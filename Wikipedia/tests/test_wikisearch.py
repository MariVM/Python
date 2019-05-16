from pages.page import Page 
from pages.mainpage import MainPage
from pages.mainpagelocalize import MainPageLocalize
from pages.searcresultpage import SearcResultPage
from pages.wikipage import WikiPage
import pytest

        
def test_search_pope(br):
    MainPage(br).open_lang_list()
    MainPage(br).switch_to_language('Українська')
    MainPageLocalize(br).search("Пій 12\n")
    SearcResultPage(br).open_result('Пій XII')
    assert WikiPage(br).title == 'Пій XII — Вікіпедія'