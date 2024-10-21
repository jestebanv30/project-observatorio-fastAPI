import os
import pandas as pd
from fastapi import UploadFile
from fastapi import HTTPException
from app.persistance.repository.file_repository import FileRepository

class FileService:
    def __init__(self):
        self.file_repository = FileRepository()

    async def process_file(self, file: UploadFile):
        file_extension = os.path.splitext(file.filename)[1]
        
        if file_extension.lower() not in ['.csv', '.xlsx']:
            raise Exception("Invalid file type. Only CSV and Excel files are allowed.")

        # Si es un archivo Excel, convertirlo a CSV
        if file_extension.lower() == ".xlsx":
            temp_file_path = await self.file_repository.save_temp_file(file)
            df = pd.read_excel(temp_file_path)
            df.to_csv(self.file_repository.FILE_PATH, index=False) # Guardar el archivo CSV en la ruta especificada
        else:
            csv_file_path = await self.file_repository.save_temp_file(file)

        return csv_file_path
    
    async def list_all(self):
        # Cargar el archivo CSV
        df = await self.file_repository.load_csv()

        # Reemplazar los NaN con un valor predeterminado o eliminarlos
        df = df.fillna(0)  # O puedes usar df.dropna() si prefieres eliminar filas con NaN

        # Convertir DataFrame a una lista de diccionarios y retornar
        return df.to_dict(orient='records')