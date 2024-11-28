from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración inicial
driver = None

def setup_driver():
    global driver
    if driver is None:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./whatsapp_session')  # Guarda la sesión para no iniciar siempre
        driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
        driver.get('https://web.whatsapp.com/')
        input("Escanea el código QR y presiona Enter para continuar...")

def send_whatsapp_message(phone, message):
    global driver
    try:
        setup_driver()

        # Formatear el número y abrir el chat
        url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
        driver.get(url)

        # Esperar a que cargue el campo de mensaje
        time.sleep(10)

        # Enviar mensaje
        send_btn = driver.find_element(By.XPATH, "//button[@data-testid='compose-btn-send']")
        send_btn.click()

        return True
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
        return False
