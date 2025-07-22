from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

app = FastAPI(title="API Quitar Fondo", description="Quita fondo de imágenes con IA usando rembg", version="1.0")

@app.get("/")
def read_root():
    return {"status": "API corriendo correctamente"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    # Leer imagen subida
    image_bytes = await file.read()

    # Procesar imagen con rembg
    result = remove(image_bytes)

    # Convertir resultado a BytesIO para poder enviarlo como archivo
    output = BytesIO(result)
    output.seek(0)

    # Devolver imagen sin fondo
    return StreamingResponse(output, media_type="image/png")
