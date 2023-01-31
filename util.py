from io import BytesIO

async def read_file(file):
    data = await file.read()
    return data.decode('latin-1')

async def write_file(text):
    buf = BytesIO(text.encode('latin-1'))
    return buf