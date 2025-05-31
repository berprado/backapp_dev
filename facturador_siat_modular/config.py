import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()

class Config:
    # Credenciales y configuraciones SIAT
    SIAT_API_KEY = os.getenv("SIAT_API_KEY", "VALOR_POR_DEFECTO_SI_NO_ESTA_CONFIGURADO")
    SIAT_NIT = os.getenv("SIAT_NIT")
    SIAT_CODIGO_SISTEMA = os.getenv("SIAT_CODIGO_SISTEMA")
    SIAT_CODIGO_AMBIENTE = os.getenv("SIAT_CODIGO_AMBIENTE", "2") # PRUEBAS por defecto
    SIAT_CODIGO_MODALIDAD = os.getenv("SIAT_CODIGO_MODALIDAD", "2") # COMPUTARIZADA_EN_LINEA por defecto
    SIAT_CODIGO_SUCURSAL = os.getenv("SIAT_CODIGO_SUCURSAL", "0")
    SIAT_CODIGO_PUNTO_VENTA = os.getenv("SIAT_CODIGO_PUNTO_VENTA", "0")

    # Configuración de Base de Datos
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./facturador_siat_modular.db")

    # Configuración de Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE_MAX_SIZE = 1024 * 1024 * 5  # 5 MB
    LOG_FILE_BACKUP_COUNT = 5

    # Rutas de certificados para firma digital (ejemplos)
    # CERT_PATH = os.getenv("CERT_PATH", "path/to/your/certificate.pem")
    # KEY_PATH = os.getenv("KEY_PATH", "path/to/your/private_key.pem")

    # Otros parámetros
    # ITEMS_PER_PAGE = 20

config = Config()

# Ejemplo de cómo acceder a una configuración:
# from config import config
# print(config.SIAT_NIT)
