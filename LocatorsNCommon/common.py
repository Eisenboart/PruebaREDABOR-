from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# Definición de excepciones personalizadas
class ElementNotFoundError(Exception):
    """Excepción para manejar casos en los que un elemento no se encuentra."""
    pass

class ElementNotInteractableError(Exception):
    """Excepción para manejar casos en los que un elemento no es interactuable."""
    pass

# ContextManager para utilizar WebDriverWait
class WebDriverWaitContextManager:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def __enter__(self):
        self.wait = WebDriverWait(self.driver, self.timeout)
        return self.wait

    def __exit__(self, exc_type, exc_value, traceback):
        pass

# Clase utilitaria común para interacciones con elementos
class CommonClass():
    def __init__(self, driver):
        self.driver = driver

    def click_object_with_waith(self, element, keys=None, clear=False, timeout=10):
        """Hace clic o envía teclas a un elemento con espera.

        Args:
            element (tuple): Identificador del elemento (By, value).
            keys (str): Texto a enviar (opcional).
            clear (bool): Limpiar el campo antes de enviar teclas (opcional).
            timeout (int): Tiempo máximo de espera (por defecto: 10 segundos).
        """
        CommonClass.interactuar_con_elemento(self, element, keys, clear, timeout)

    def send_keys_object(self, element, keys, clear=True, timeout=10):
        """Envía teclas a un elemento con espera.

        Args:
            element (tuple): Identificador del elemento (By, value).
            keys (str): Texto a enviar.
            clear (bool): Limpiar el campo antes de enviar teclas (por defecto: True).
            timeout (int): Tiempo máximo de espera (por defecto: 10 segundos).
        """
        CommonClass.interactuar_con_elemento(self, element, keys, clear, timeout)

    def verificar_text_en_campo(self, element, keys):
        """Verifica si un texto está presente en un campo con espera.

        Args:
            element (tuple): Identificador del elemento (By, value).
            keys (str): Texto a verificar.

        Raises:
            ElementNotFoundError: Cuando el campo no está presente en la página.
            AssertionError: Cuando el valor del campo no contiene el texto especificado.
        """
        try:
            actual_text = self.driver.find_element(*element).text
            assert keys in actual_text
            print(f"El texto: '{keys}' se encuentra en el texto actual")
        except NoSuchElementException:
            raise ElementNotFoundError("El campo no está presente en la página.")
        except AssertionError:
            raise AssertionError(f"El valor del campo no contiene '{keys}'. Texto actual: '{actual_text}'")

    def interactuar_con_elemento(self, element, keys=None, clear=False, timeout=10):
        """Interactúa con un elemento (clic o envío de teclas) con espera.

        Args:
            element (tuple): Identificador del elemento (By, value).
            keys (str): Texto a enviar (opcional).
            clear (bool): Limpiar el campo antes de enviar teclas (opcional).
            timeout (int): Tiempo máximo de espera (por defecto: 10 segundos).
        """
        with WebDriverWaitContextManager(self.driver, timeout) as wait:
            try:
                # Esperar a que el elemento esté presente en el DOM
                wait.until(EC.presence_of_element_located(element))
                objeto = self.driver.find_element(*element)

                if keys is not None:
                    # Si se proporcionan teclas, interactuar con el elemento (clic o enviar teclas)
                    if clear:
                        objeto.clear()
                    objeto.send_keys(keys)
                else:
                    # Si no se proporcionan teclas, hacer clic en el elemento
                    objeto.click()

            except TimeoutException:
                raise ElementNotFoundError("No se encontró el elemento dentro del tiempo de espera.")
            except NoSuchElementException:
                raise ElementNotFoundError("El elemento no está presente en la página.")
            except ElementNotInteractableException:
                raise ElementNotInteractableError("No se puede interactuar con el elemento.")
