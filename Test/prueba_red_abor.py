import os
import sys
import time
import unittest
import traceback

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Page.modulo_001_com_landing import ComLandingClass
from Page.modulo_002_col_landing import ColLandingClass
from Page.modulo_003_empleos_y_filtros import EmpleosYFiltrosClass
from Page.modulo_004_crear_cuenta import CrearCuentaClass

class RedAborTest(unittest.TestCase):
    """
    Clase de prueba para el caso de uso de RedArbor en Computrabajo.

    Esta clase contiene métodos para configurar la prueba, ejecutar el caso de prueba y limpiar después de la prueba.
    """

    @classmethod
    def setUpClass(cls):
        """
        Método para configurar la prueba.

        Este método se ejecuta una vez antes de ejecutar todas las pruebas en la clase.
        """
        super().setUpClass()
        firefox_options = Options()
        firefox_options.add_argument("--disable-notifications")
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        cls.driver = webdriver.Firefox(options=firefox_options)
        cls.driver.set_window_size(1920, 1080)

    def test_01_red_abor(self):
        """
        Método para ejecutar el caso de prueba principal.

        Este método realiza una serie de acciones en la página de Computrabajo y verifica el comportamiento esperado.
        """
        driver = self.driver
        driver.get('https://www.computrabajo.com/')

        com_landing = ComLandingClass(driver)
        try:
            com_landing.click_bandera_colombia()
        except Exception as e:
            self.fail(f"Falla en com_landing. Error: {e}")

        col_landing = ColLandingClass(driver)
        try:
            col_landing.seleccionar_ubicacion("Guainía")
        except Exception as e:            
            self.fail(f"Falla en col_landing. Error: {e}")

        eNF = EmpleosYFiltrosClass(driver)        
        try:
            eNF.buscar_puesto("qa")
            eNF.setear_filtro_experiencia()
            eNF.setear_filtro_salario()
            eNF.verificar_puesto_y_postularse("Guainía")
            eNF.iniciar_proceso_de_creacion_de_cuenta("prueba@test.com")
        except Exception as e:
            self.fail(f"Falla en empleos. Error: {e}")
            
        crear_cuenta = CrearCuentaClass(driver)
        try:
            crear_cuenta.completar_informacion_personal("nombre", "apellido", "password123")
            crear_cuenta.completar_informacion_laboral("Tester QA")
            crear_cuenta.completar_localizacion()
            crear_cuenta.completar_captcha("0000")
            crear_cuenta.verificar_error_pop_up("Captcha incorrecto")
        except Exception as e:
            self.fail(f"Falla en crear cuenta. Error: {e}")
        
    @classmethod
    def tearDownClass(cls):
        """
        Método para limpiar después de la prueba.

        Este método se ejecuta una vez después de ejecutar todas las pruebas en la clase.
        """
        cls.driver.quit()
        super().tearDownClass()
        print("Fin del test RedArbor")

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__, limit=1)
