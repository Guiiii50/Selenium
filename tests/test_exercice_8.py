import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.homepage import HomePage
from pages.search_result_page import SearchResultPage

@pytest.fixture
def driver():

    # Tout ce qui vient avant le yield sera exécuté avant
    # le lancement des tests.

    # Instancier le driver Chrome avec ses options
    browser = webdriver.Chrome()
    
    # Aller sur la page de Décathlon
    browser.get("https://www.decathlon.fr/")

    # Maximiser la fenêtre
    browser.maximize_window()

    yield browser  # Provide the driver to the test

    # Tout ce qui vient après le yield sera exécuté
    # à la fin des tests
    browser.quit()  # Fermeture du navigateur


@pytest.fixture
def wait(driver):
    # Instancier le wait explicit pour le driver
    return WebDriverWait(driver, 10)


def test_recherche(driver, wait):

    # Instancier la page d'accueil
    homepage = HomePage(driver, wait)

    # Continuer sans accepter les cookies
    homepage.continuer_sans_cookies()

    # Vérifier le titre de la page
    homepage.verifier_titre_homepage("DECATHLON | Magasin de Sport")

    # Chercher le produit Vélo
    homepage.chercher_produit("Vélo")
    
    # Instancier la page d'accueil
    search_page_result = SearchResultPage(driver, wait)

    # Vérifier le titre des résultats
    search_page_result.verifier_titre_resultats("Vélos")

    # Vérifier la présence de la liste des produits
    search_page_result.verifier_presence_produits()

    # Trier les résultats par Prix décroissants
    search_page_result.trier_resultats("Prix décroissants")