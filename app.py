
### 🧩 app.py
```python
from fastapi import FastAPI, UploadFile
import hashlib

app = FastAPI(title="Blockchain Hash Verification")

@app.post("/hash-file")
async def hash_file(file: UploadFile):
    data = await file.read()
    file_hash = hashlib.sha256(data).hexdigest()
    return {"filename": file.filename, "sha256": file_hash}
  
