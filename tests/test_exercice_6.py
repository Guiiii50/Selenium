import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():

    # Instancier le driver Chrome avec ses options
    browser = webdriver.Chrome()
    
    # Aller sur la page de Décathlon
    browser.get("https://www.decathlon.fr/")

    # Maximiser la fenêtre
    browser.maximize_window()

    yield browser  # Provide the driver to the test
    browser.quit()  # Cleanup after test


@pytest.fixture
def wait(driver):
    # Instantiating explicit wait for the given driver
    return WebDriverWait(driver, 10)


def test_recherche(driver, wait):

    # Vérifier que le titre de la page est correct
    assert driver.title == 'DECATHLON | Magasin de Sport'

    # Continuer sans accepter les cookies
    try:
        wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "didomi-continue-without-agreeing"))
            ).click()
    except TimeoutException:
        print("Cookies pop-up is not present")

    # Récupérer le champ de recherche en utilisant le xpath
    search_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))
        )

    # Ecrire Vélo dans le champ de recherche et simuler le bouton Entrée
    search_box.clear()
    search_box.send_keys("Vélo")
    search_box.send_keys(Keys.RETURN)

    # Vérifier que nous sommes sur la page des vélos
    resultatRecherche = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
    assert resultatRecherche.text == "Vélos"

    # Vérifier qu'il y a au moins un produit affiché
    product_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-list')))
    assert product_list.is_displayed(), "Products should be visible"

    # Trouver le menu déroulant
    tri_element = wait.until(EC.visibility_of_element_located((By.ID, 'list-sort-select')))
    select_tri = Select(tri_element)

    assert select_tri.first_selected_option.text == "Meilleures ventes"

    select_tri.select_by_visible_text("Prix croissants")
    assert select_tri.first_selected_option.text == "Prix croissants"

    select_tri.select_by_index(3)
    assert select_tri.first_selected_option.text == "Remise décroissante"

    select_tri.select_by_value("4")
    assert select_tri.first_selected_option.text == "Note des clients"
