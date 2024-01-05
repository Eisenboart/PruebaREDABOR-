class PageLocatorsClass():
    """Clase que contiene localizadores de elementos en la página."""

    # .comLanding
    com_colombia_flag_id = 'Colombialink'

    # .coLanding
    col_input_lugar_id = 'place-search-input'
    col_search_button_id = 'search-button'
    col_guaina_autocomplete_xpath = '//*[@data-autocomplete-item-selectable-url="/empleos-en-guainia"]'

    # empleosNFiltros
    enf_input_cargo_id = 'prof-cat-search-input'
    enf_search_button_id = 'search-button'
    enf_no_now_button_xpath = '//button[contains(text(),"Ahora no")]'
    enf_xp_xpath = '//*[P="Experiencia"]'  # Aquí parece haber un error, debería ser '//*[@P="Experiencia"]', pero al buscar por ese xpath no encuentra el elemento, el actual funciona
    enf_xp_one_year_xpath = '//*[Span="1 año"]'
    enf_salario_xpath = '//*[P="Salario"]'  # Aquí parece haber un error, debería ser '//*[@P="Salario"]', pero al buscar por ese xpath no encuentra el elemento, el actual funciona
    enf_salario_menos_de_xpath = '//*[Span="Menos de $ 700.000"]'
    enf_localizacion_xpath = '//a[contains(text(),"Test automation Engineer QA")]/../../p/span'
    enf_dots_xpath = '//a[contains(text(),"Test automation Engineer QA")]/../../div[@class="opt_dots"]'
    enf_postularse_xpath = '//a[contains(text(),"Test automation Engineer QA")]/../../div/div/a[contains(@label-ga, "Shortcuts_postular")]'
    enf_email_model_id = 'LoginModel_Email'
    enf_continue_button_enf_id = 'continueWithMailButton'

    # crearCuenta
    crc_nombre_id = 'Name'
    crc_apellido_id = 'SurName'
    crc_contraseña_id = 'Password'
    crc_campo_cargo_id = 'Cargo'
    crc_seleccionar_cargo_xpath = '//span[contains(text(),"Tester QA")]/..'  # Se cambió la ruta XPath para obtener el padre
    crc_localizacion_xpath = '//*[@id="LocationId"]/..'  # Se cambió la ruta XPath para obtener el padre
    crc_localizacion_guainía_xpath = '//li[contains(text(),"Guainía")]'
    crc_captcha_id = 'CaptchaInputText'
    crc_continue_button_sign_in_id = 'continueButton'
    crc_captcha_error_pop_up_xpath = '//span[contains(text(),"Captcha incorrecto")]'
