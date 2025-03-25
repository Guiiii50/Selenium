from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class SearchResultPage:
    def __init__(self, driver, wait):

        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.search_page_header = (By.CLASS_NAME, "vtmn-text-5xl")
        self.product_list = (By.CLASS_NAME, 'product-list')
        self.liste_tri = (By.ID, 'list-sort-select')

    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs
    
    def verifier_titre_resultats(self, titre):
        resultatRecherche = self.wait.until(EC.visibility_of_element_located(self.search_page_header))
        assert resultatRecherche.text == titre


    def verifier_presence_produits(self):
        liste_produits = self.wait.until(EC.visibility_of_element_located(self.product_list))
        assert liste_produits.is_displayed(), "La liste de produits doit être affichée"


    def trier_resultats(self, type_tri):
        tri_element = self.wait.until(EC.visibility_of_element_located(self.liste_tri))
        select_tri = Select(tri_element)

        assert select_tri.first_selected_option.text == "Meilleures ventes"

        select_tri.select_by_visible_text(type_tri)
        assert select_tri.first_selected_option.text == type_tri