import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO
import uvicorn

app = FastAPI(
    title="API Quitar Fondo",
    description="Quita fondo de imágenes con IA usando rembg",
    version="1.0"
)

@app.get("/")
def read_root():
    return {"status": "API corriendo correctamente"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = remove(image_bytes)
    output = BytesIO(result)
    output.seek(0)
    return StreamingResponse(output, media_type="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
