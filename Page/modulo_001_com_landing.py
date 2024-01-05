# modulo_001.py
from selenium.webdriver.common.by import By
from LocatorsNCommon.locator import PageLocatorsClass
from LocatorsNCommon.common import CommonClass

class ComLandingClass():
    """
    Clase que representa la página de aterrizaje común.
    
    Esta clase encapsula la interacción con la página de aterrizaje común.
    """

    def __init__(self, driver):
        """
        Inicializa la instancia de la clase ComLandingClass.

        :param driver: Instancia del WebDriver de Selenium.
        """
        self.driver = driver
        self.bandera_colombia = (By.ID, PageLocatorsClass.com_colombia_flag_id)

    def click_bandera_colombia(self):
        """
        Método para hacer clic en la bandera de Colombia.

        Este método utiliza la clase CommonClass para interactuar con el elemento de la bandera de Colombia.
        """
        CommonClass.click_object_with_waith(self, self.bandera_colombia)
