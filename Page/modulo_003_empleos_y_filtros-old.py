from selenium.webdriver.common.by import By
from LocatorsNCommon.locator import PageLocatorsClass
from LocatorsNCommon.common import CommonClass
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class EmpleosYFiltrosClass():

    def __init__(self, driver):
        self.driver = driver

        #ejemplo: 
        #self.banderaColombia = (By.ID,PageLocators.colombiaFlag_ID)
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

    def buscar_puesto(self,keys):
        EmpleosYFiltrosClass.click_campo_busqueda(self)
        EmpleosYFiltrosClass.insertar_puesto(self, keys)
        EmpleosYFiltrosClass.click_boton_busqueda(self)
    
    def setear_filtro_experiencia(self):
        EmpleosYFiltrosClass.click_filtro_tiempo_exp(self)
        EmpleosYFiltrosClass.click_seleccion_año_exp(self)
    
    def setear_filtro_salario(self):
        EmpleosYFiltrosClass.click_filtro_salario(self)
        EmpleosYFiltrosClass.click_seleccion_salario_menos_set(self)

    def verificar_puesto_y_postularse(self,keys):
        EmpleosYFiltrosClass.verificar_localizacion_puesto(self, keys)
        EmpleosYFiltrosClass.click_tres_puntos(self)
        EmpleosYFiltrosClass.click_postularse(self)
    
    def iniciar_proceso_de_creacion_de_cuenta(self,keys):
        EmpleosYFiltrosClass.click_campo_email(self)
        EmpleosYFiltrosClass.insertar_email(self, keys)
        EmpleosYFiltrosClass.click_continue_button(self)

    def clickElementoConEspera(self, elemento):
        try:
            CommonClass.click_object_with_waith(self, elemento)
        except ElementClickInterceptedException:
            EmpleosYFiltrosClass.click_ahora_no_boton()
            CommonClass.click_object_with_waith(self, elemento)

    def click_campo_busqueda(self,):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.campo_busqueda_puesto)
        
    def insertar_puesto(self, keys):
        try:
            CommonClass.send_keys_object(self, self.campo_busqueda_puesto, keys, clear=True)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.send_keys_object(self, self.campo_busqueda_puesto, keys, clear=True)

    def click_boton_busqueda(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.boton_busqueda_puesto)

    def click_filtro_tiempo_exp(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.filtro_tiempo_exp)
        
    def click_seleccion_año_exp (self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.seleccion_año_exp)

    def click_filtro_salario(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.filtro_salario)

    def click_seleccion_salario_menos_set (self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.salario_menos_set)

    def verificar_localizacion_puesto(self, keys):
        try:
            CommonClass.verificar_text_en_campo(self, self.localizacion_puesto, keys)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.verificar_text_en_campo(self, self.localizacion_puesto, keys)

    def click_tres_puntos(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.tres_puntos)

    def click_postularse(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.postularse)

    def click_campo_email(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.campo_email)

    def insertar_email(self, keys):
        try:
            CommonClass.send_keys_object(self, self.campo_email, keys, clear=True)
        except ElementClickInterceptedException:
            self.click_ahora_no_boton()
            CommonClass.send_keys_object(self, self.campo_email, keys, clear=True)

    def click_continue_button(self):
        EmpleosYFiltrosClass.clickElementoConEspera(self, self.continue_button)

    def click_ahora_no_boton(self):
        CommonClass.click_object_with_waith(self, self.ahora_no_boton)
