from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.search_result_page import SearchResultPage
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.ignore_cookies_button = (By.CLASS_NAME, "didomi-continue-without-agreeing")
        self.search_bar = (By.XPATH, "//input[@type='search']")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def verifier_titre_homepage(self, titre):
        actual_title = self.driver.title
        assert actual_title == titre, f"Le titre attendu devrait être '{titre}', mais le résultat est '{actual_title}'"
    

    def continuer_sans_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ignore_cookies_button)).click()
        except TimeoutException:
            print("Cookies pop-up is not present")


    def chercher_produit(self, produit):
        search_bar_element = self.wait.until(EC.element_to_be_clickable(self.search_bar))
        search_bar_element.clear()
        search_bar_element.send_keys(produit)
        search_bar_element.send_keys(Keys.RETURN)
