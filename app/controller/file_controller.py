from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.domain.services.file_service import FileService

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...), file_service: FileService = Depends()):
    try:
        file_location = await file_service.process_file(file)
        return {"message": "File processed successfully", "file_location": file_location}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list_all/")
async def list_all(file_service: FileService = Depends()):
    try:
        result = await file_service.list_all()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))