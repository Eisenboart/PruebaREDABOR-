# EmpleosYFiltrosClass.py
from selenium.webdriver.common.by import By
from LocatorsNCommon.locator import PageLocatorsClass
from LocatorsNCommon.common import CommonClass
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class EmpleosYFiltrosClass():
    """
    Clase que representa la página de Empleos y Filtros.

    Esta clase encapsula la interacción con la página de búsqueda de empleos y filtros en Computrabajo.
    """

    def __init__(self, driver):
        """
        Inicializa la instancia de la clase EmpleosYFiltrosClass.

        :param driver: Instancia del WebDriver de Selenium.
        """
        self.driver = driver

        self.campo_busqueda_puesto  = (By.ID,PageLocatorsClass.enf_input_cargo_id)
        self.boton_busqueda_puesto  = (By.ID,PageLocatorsClass.enf_search_button_id)
        self.ahora_no_boton         = (By.XPATH,PageLocatorsClass.enf_no_now_button_xpath)
        self.filtro_tiempo_exp      = (By.XPATH,PageLocatorsClass.enf_xp_xpath)
        self.seleccion_año_exp      = (By.XPATH,PageLocatorsClass.enf_xp_one_year_xpath)
        self.filtro_salario         = (By.XPATH,PageLocatorsClass.enf_salario_xpath)
        self.salario_menos_set      = (By.XPATH,PageLocatorsClass.enf_salario_menos_de_xpath)
        self.localizacion_puesto    = (By.XPATH,PageLocatorsClass.enf_localizacion_xpath)
        self.tres_puntos            = (By.XPATH,PageLocatorsClass.enf_dots_xpath)
        self.postularse             = (By.XPATH,PageLocatorsClass.enf_postularse_xpath)
        self.campo_email            = (By.ID,PageLocatorsClass.enf_email_model_id)
        self.continue_button        = (By.ID,PageLocatorsClass.enf_continue_button_enf_id)

    def buscar_puesto(self, keys):
        """
        Método para buscar un puesto en la página de empleos.

        :param keys: Término de búsqueda para el puesto.
        """
        EmpleosYFiltrosClass.click_campo_busqueda(self)
        EmpleosYFiltrosClass.insertar_puesto(self, keys)
        EmpleosYFiltrosClass.click_boton_busqueda(self)

    def setear_filtro_experiencia(self):
        """Método para establecer el filtro de experiencia."""
        EmpleosYFiltrosClass.click_filtro_tiempo_exp(self)
        EmpleosYFiltrosClass.click_seleccion_año_exp(self)

    def setear_filtro_salario(self):
        """Método para establecer el filtro de salario."""
        EmpleosYFiltrosClass.click_filtro_salario(self)
        EmpleosYFiltrosClass.click_seleccion_salario_menos_set(self)

    def verificar_puesto_y_postularse(self, keys):
        """
        Método para verificar la ubicación del puesto y realizar la acción de postulación.

        :param keys: Ubicación esperada del puesto.
        """
        EmpleosYFiltrosClass.verificar_localizacion_puesto(self, keys)
        EmpleosYFiltrosClass.click_tres_puntos(self)
        EmpleosYFiltrosClass.click_postularse(self)

    def iniciar_proceso_de_creacion_de_cuenta(self, keys):
        """
        Método para iniciar el proceso de creación de cuenta.

        :param keys: Correo electrónico para la creación de cuenta.
        """
        EmpleosYFiltrosClass.click_campo_email(self)
        EmpleosYFiltrosClass.insertar_email(self, keys)
        EmpleosYFiltrosClass.click_continue_button(self)

    def clickElementoConEspera(self, elemento):
        """
        Método para hacer clic en un elemento con espera.

        Este método maneja la excepción ElementClickInterceptedException y realiza una acción alternativa.
        :param elemento: Elemento en el que se desea hacer clic.
        """
        try:
            CommonClass.click_object_with_waith(self, elemento)
        except ElementClickInterceptedException:
            EmpleosYFiltrosClass.click_ahora_no_boton()
            CommonClass.click_object_with_waith(self, elemento)

    def click_campo_busqueda(self):
        """Método para hacer clic en el campo de búsqueda de puesto."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.campo_busqueda_puesto)
        
    def insertar_puesto(self, keys):
        """
        Método para insertar el puesto en el campo de búsqueda.

        :param keys: Término de búsqueda para el puesto.
        """
        try:
            CommonClass.send_keys_object(self, self.campo_busqueda_puesto, keys, clear=True)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.send_keys_object(self, self.campo_busqueda_puesto, keys, clear=True)

    def click_boton_busqueda(self):
        """Método para hacer clic en el botón de búsqueda de puesto."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.boton_busqueda_puesto)

    def click_filtro_tiempo_exp(self):
        """Método para hacer clic en el filtro de experiencia."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.filtro_tiempo_exp)
        
    def click_seleccion_año_exp (self):
        """Método para hacer clic en la selección de un año de experiencia."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.seleccion_año_exp)

    def click_filtro_salario(self):
        """Método para hacer clic en el filtro de salario."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.filtro_salario)

    def click_seleccion_salario_menos_set (self):
        """Método para hacer clic en la selección de salario 'Menos de $700,000'."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.salario_menos_set)

    def verificar_localizacion_puesto(self, keys):
        """
        Método para verificar la ubicación del puesto en la página.

        :param keys: Ubicación esperada del puesto.
        """
        try:
            CommonClass.verificar_text_en_campo(self, self.localizacion_puesto, keys)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.verificar_text_en_campo(self, self.localizacion_puesto, keys)

    def click_tres_puntos(self):
        """Método para hacer clic en los tres puntos de opciones del puesto."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.tres_puntos)

    def click_postularse(self):
        """Método para hacer clic en el botón de postulación."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.postularse)

    def click_campo_email(self):
        """Método para hacer clic en el campo de correo electrónico."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.campo_email)

    def insertar_email(self, keys):
        """
        Método para insertar el correo electrónico en el campo correspondiente.

        :param keys: Correo electrónico que se desea insertar.
        """
        try:
            CommonClass.send_keys_object(self, self.campo_email, keys, clear=True)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.send_keys_object(self, self.campo_email, keys, clear=True)

    def click_continue_button(self):
        """Método para hacer clic en el botón de continuar en el proceso de creación de cuenta."""
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.continue_button)

    def click_ahora_no_boton(self):
        """Método para hacer clic en el botón 'Ahora no' en caso de interferencia."""
        CommonClass.click_object_with_waith(self, self.ahora_no_boton)
