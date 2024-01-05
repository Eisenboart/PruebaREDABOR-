# modulo_002.py
from selenium.webdriver.common.by import By
from LocatorsNCommon.locator import PageLocatorsClass
from LocatorsNCommon.common import CommonClass

class ColLandingClass():
    """
    Clase que representa la página de aterrizaje en Colombia.

    Esta clase encapsula la interacción con la página de aterrizaje en Colombia.
    """

    def __init__(self, driver):
        """
        Inicializa la instancia de la clase ColLandingClass.

        :param driver: Instancia del WebDriver de Selenium.
        """
        self.driver = driver
        self.locacion = (By.ID, PageLocatorsClass.col_input_lugar_id)
        self.boton_buscar = (By.ID, PageLocatorsClass.col_search_button_id)
        self.campo_seleccionar_guinia = (By.XPATH, PageLocatorsClass.col_guaina_autocomplete_xpath)

    def seleccionar_ubicacion(self, keys):
        """
        Método para seleccionar la ubicación.

        Este método utiliza otros métodos internos para interactuar con los elementos de la página.
        :param keys: Ubicación que se desea seleccionar.
        """
        ColLandingClass.click_locacion(self)
        ColLandingClass.insertar_locacion(self, keys)
        ColLandingClass.click_buscar_locacion(self)

    def click_locacion(self):
        """Método para hacer clic en el campo de ubicación."""
        CommonClass.click_object_with_waith(self, self.locacion)

    def insertar_locacion(self, keys):
        """
        Método para insertar la ubicación en el campo correspondiente.

        :param keys: Ubicación que se desea insertar.
        """
        CommonClass.send_keys_object(self, self.locacion, keys, clear=True)

    def click_buscar_locacion(self):
        """Método para hacer clic en el botón de búsqueda de ubicación."""
        CommonClass.click_object_with_waith(self, self.boton_buscar)

    def clickCampoGuinia(self):
        """Método para hacer clic en el campo seleccionar Guainía."""
        CommonClass.click_object_with_waith(self, self.campo_seleccionar_guinia)
