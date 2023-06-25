class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке чтения CSV-файла.
    """

    def __init__(self, message: str = "Файл item.csv поврежден"):
        super().__init__(message)
        self.message = message