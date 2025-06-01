import logging
import logging.handlers
import os
import sys
from pathlib import Path
from ..config import config # Usamos ruta relativa para importar config desde dentro del paquete

LOG_DIR_NAME = "logs" # Nombre del directorio de logs dentro de facturador_siat_modular

def setup_logging():
    """
    Configura el logging para la aplicación.
    """
    log_level_str = config.LOG_LEVEL.upper()
    log_level = getattr(logging, log_level_str, logging.INFO)

    # Crear el directorio de logs si no existe
    # La ruta base será el directorio donde se encuentra este archivo (utils),
    # luego subimos un nivel (a facturador_siat_modular) y entramos a 'logs'
    base_dir = Path(__file__).resolve().parent.parent 
    log_dir = base_dir / LOG_DIR_NAME
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file_path = log_dir / "facturador_modular_app.log"

    # Formateador
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
    )

    # Logger raíz
    # Es buena práctica configurar el logger raíz y luego obtener loggers específicos por módulo.
    # O, si preferimos un logger específico para nuestra app modular:
    # logger = logging.getLogger("facturador_modular")
    # logger.setLevel(log_level)
    # Por simplicidad inicial, configuraremos el logger raíz.
    # Si esta app modular es parte de una app más grande, podríamos querer un logger con nombre.
    
    root_logger = logging.getLogger() # Obtiene el logger raíz
    root_logger.setLevel(log_level)
    
    # Evitar duplicación de handlers si setup_logging se llama múltiples veces
    if root_logger.hasHandlers():
        # Limpiar solo los handlers que podríamos haber añadido nosotros, 
        # o ser más selectivo si hay handlers globales que queremos preservar.
        # Por ahora, para este módulo autocontenido, limpiar todos está bien.
        root_logger.handlers.clear()

    # Handler para la consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Handler para archivo rotativo
    # Usar valores de config.py para tamaño y número de backups
    file_handler = logging.handlers.RotatingFileHandler(
        log_file_path,
        maxBytes=config.LOG_FILE_MAX_SIZE,
        backupCount=config.LOG_FILE_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    logging.info("Logging configurado exitosamente.")
    logging.info(f"Nivel de log: {log_level_str}")
    logging.info(f"Directorio de logs: {log_dir.resolve()}")
    logging.info(f"Archivo de log: {log_file_path.resolve()}")

# Ejemplo de cómo obtener un logger en otros módulos:
# import logging
# logger = logging.getLogger(__name__)
# logger.info("Este es un mensaje de prueba.")

# Si quieres que se configure automáticamente al importar el módulo (no siempre recomendado):
# setup_logging()
