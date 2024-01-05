# CrearCuentaClass.py
from selenium.webdriver.common.by import By
from LocatorsNCommon.locator import PageLocatorsClass
from LocatorsNCommon.common import CommonClass

class CrearCuentaClass():
    """
    Clase que representa la página de creación de cuenta en Computrabajo.

    Esta clase encapsula la interacción con la página de creación de cuenta, proporcionando métodos
    para completar la información personal, laboral, la localización, el captcha y realizar las acciones correspondientes.
    """

    def __init__(self, driver):
        """
        Inicializa la instancia de la clase CrearCuentaClass.

        :param driver: Instancia del WebDriver de Selenium.
        """
        self.driver = driver

        self.nombre                     = (By.ID, PageLocatorsClass.crc_nombre_id)
        self.apellido                   = (By.ID, PageLocatorsClass.crc_apellido_id)
        self.contraseña                 = (By.ID, PageLocatorsClass.crc_contraseña_id)
        self.campo_cargo                = (By.ID, PageLocatorsClass.crc_campo_cargo_id)
        self.seleccionar_cargo          = (By.XPATH, PageLocatorsClass.crc_seleccionar_cargo_xpath)
        self.localizacion               = (By.XPATH, PageLocatorsClass.crc_localizacion_xpath)
        self.localizacion_guainia       = (By.XPATH, PageLocatorsClass.crc_localizacion_guainía_xpath)
        self.captcha                    = (By.ID, PageLocatorsClass.crc_captcha_id)
        self.continue_button_sign_in    = (By.ID, PageLocatorsClass.crc_continue_button_sign_in_id)
        self.captcha_error_pop_up       = (By.XPATH, PageLocatorsClass.crc_captcha_error_pop_up_xpath)

    def completar_informacion_personal(self, nombre, apellido, password):
        """
        Método para completar la información personal en la página de creación de cuenta.

        :param nombre: Nombre a insertar.
        :param apellido: Apellido a insertar.
        :param password: Contraseña a insertar.
        """
        CrearCuentaClass.insertar_nombre(self, nombre)
        CrearCuentaClass.insertar_apellido(self, apellido)
        CrearCuentaClass.insertar_contraseña(self, password)
    
    def completar_informacion_laboral(self, keys):
        """
        Método para completar la información laboral en la página de creación de cuenta.

        :param keys: Puesto pretendido a insertar.
        """
        CrearCuentaClass.click_campo_cargo(self)
        CrearCuentaClass.insertar_puesto_pretendido(self, keys)
        CrearCuentaClass.click_puesto_de_trabajo(self)

    def completar_localizacion(self):
        """Método para completar la localización en la página de creación de cuenta."""
        CrearCuentaClass.click_localizacion(self)
        CrearCuentaClass.click_localizacion_guainia(self)
    
    def completar_captcha(self, captcha):
        """
        Método para completar el captcha en la página de creación de cuenta.

        :param captcha: Valor del captcha a insertar.
        """
        CrearCuentaClass.insertar_captcha(self, captcha)
        CrearCuentaClass.click_continue_button_sign_in(self)

    def insertar_nombre(self, keys):
        """Método para insertar el nombre en el campo correspondiente."""
        CommonClass.send_keys_object(self, self.nombre, keys, clear=True)

    def insertar_apellido(self, keys):
        """Método para insertar el apellido en el campo correspondiente."""
        CommonClass.send_keys_object(self, self.apellido, keys, clear=True)
    
    def insertar_contraseña(self, keys):
        """Método para insertar la contraseña en el campo correspondiente."""
        CommonClass.send_keys_object(self, self.contraseña, keys, clear=True)
    
    def click_campo_cargo(self):
        """Método para hacer clic en el campo de cargo."""
        CommonClass.click_object_with_waith(self, self.campo_cargo)
    
    def insertar_puesto_pretendido(self, keys):
        """Método para insertar el puesto pretendido en el campo correspondiente."""
        CommonClass.send_keys_object(self, self.campo_cargo, keys, clear=False)
    
    def click_puesto_de_trabajo(self):
        """Método para hacer clic en el puesto de trabajo seleccionado."""
        CommonClass.click_object_with_waith(self, self.seleccionar_cargo)
    
    def click_localizacion(self):
        """Método para hacer clic en el campo de localización."""
        CommonClass.click_object_with_waith(self, self.localizacion)

    def click_localizacion_guainia(self):
        """Método para hacer clic en la opción de localización 'Guainía'."""
        CommonClass.click_object_with_waith(self, self.localizacion_guainia)
    
    def insertar_captcha(self, keys):
        """Método para insertar el valor del captcha en el campo correspondiente."""
        CommonClass.send_keys_object(self, self.captcha, keys, clear=True)
    
    def click_continue_button_sign_in(self):
        """Método para hacer clic en el botón de continuar en la página de creación de cuenta."""
        CommonClass.click_object_with_waith(self, self.continue_button_sign_in)
    
    def verificar_error_pop_up(self, keys):
        """
        Método para verificar el mensaje de error en el pop-up.

        :param keys: Mensaje de error esperado.
        """
        CommonClass.verificar_text_en_campo(self, self.captcha_error_pop_up, keys)
