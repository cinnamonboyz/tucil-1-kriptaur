from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates

from algo.onetimepad import decrypt_otp, encrypt_otp, generate_random_key
from algo.playfair import playfair_decrypt, playfair_encrypt
from algo.vigenere import vigenere_decrypt, vigenere_encrypt
from algo.vigenere_extended import extended_vigenere_decrypt, extended_vigenere_encrypt
from algo.enigma import enigma

from util import read_file, write_file

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/vigenere')
async def vigenere_home(request: Request):
    return templates.TemplateResponse('vigenere.html', {'request': request})

@app.get('/extended_vigenere')
async def extended_vigenere_home(request: Request):
    return templates.TemplateResponse('extended_vigenere.html', {'request': request})

@app.get('/playfair')
async def playfair_home(request: Request):
    return templates.TemplateResponse('playfair.html', {'request': request})

@app.get('/onetimepad')
async def onetimepad_home(request: Request):
    return templates.TemplateResponse('onetimepad.html', {'request': request})

@app.get('/enigma')
async def enigma_home(request: Request):
    return templates.TemplateResponse('enigma.html', {'request': request})

@app.post('/file')
async def to_file(cipher_text: str = Form(None)):
    return StreamingResponse(await write_file(cipher_text), media_type='text/plain')

@app.get('/favicon.ico')
async def favicon():
    return FileResponse('/static/logo_1024.png')


# vigenere
@app.post('/vigenere_encrypt_text')
async def vigenere_encrypt_text(plain_text: str = Form(None), key: str = Form(None)):
    cipher = vigenere_encrypt(plain_text, key)
    return cipher

@app.post('/vigenere_encrypt_file')
async def vigenere_decrypt_file(plain_file: UploadFile = File(None), key: str = Form(None),):
    cipher = vigenere_encrypt(await read_file(plain_file), key)
    return StreamingResponse(await write_file(cipher), media_type=plain_file.content_type)

@app.post('/vigenere_decrypt_text')
async def vigenere_decrypt_text(cipher_text: str = Form(None), key: str = Form(None)):
    plain = vigenere_decrypt(cipher_text, key)
    return plain

@app.post('/vigenere_decrypt_file')
async def vigenere_decrypt_file(cipher_file: UploadFile = File(None), key: str = Form(None)):
    plain = vigenere_decrypt(await read_file(cipher_file), key)
    return StreamingResponse(await write_file(plain), media_type=cipher_file.content_type)


# vigenere extended
@app.post('/extended_vigenere_encrypt_text')
async def extended_vigenere_encrypt_text(plain_text: str = Form(None), key: str = Form(None)):
    cipher = extended_vigenere_encrypt(plain_text, key)
    return cipher

@app.post('/extended_vigenere_encrypt_file')
async def extended_vigenere_decrypt_file(plain_file: UploadFile = File(None), key: str = Form(None),):
    cipher = extended_vigenere_encrypt(await read_file(plain_file), key)
    return StreamingResponse(await write_file(cipher), media_type=plain_file.content_type)

@app.post('/extended_vigenere_decrypt_text')
async def extended_vigenere_decrypt_text(cipher_text: str = Form(None), key: str = Form(None)):
    plain = extended_vigenere_decrypt(cipher_text, key)
    return plain

@app.post('/extended_vigenere_decrypt_file')
async def extended_vigenere_decrypt_file(cipher_file: UploadFile = File(None), key: str = Form(None)):
    plain = extended_vigenere_decrypt(await read_file(cipher_file), key)
    return StreamingResponse(await write_file(plain), media_type=cipher_file.content_type)


# playfair
@app.post('/playfair_encrypt_text')
async def playfair_encrypt_text(plain_text: str = Form(None), key: str = Form(None)):
    cipher = playfair_encrypt(plain_text, key)
    return cipher

@app.post('/playfair_encrypt_file')
async def playfair_decrypt_file(plain_file: UploadFile = File(None), key: str = Form(None),):
    cipher = playfair_encrypt(await read_file(plain_file), key)
    return StreamingResponse(await write_file(cipher), media_type=plain_file.content_type)

@app.post('/playfair_decrypt_text')
async def playfair_decrypt_text(cipher_text: str = Form(None), key: str = Form(None)):
    plain = playfair_decrypt(cipher_text, key)
    return plain

@app.post('/playfair_decrypt_file')
async def playfair_decrypt_file(cipher_file: UploadFile = File(None), key: str = Form(None)):
    plain = playfair_decrypt(await read_file(cipher_file), key)
    return StreamingResponse(await write_file(plain), media_type=cipher_file.content_type)


# one time pad
@app.post('/otp_encrypt')
async def otp_encrypt(plain_text: str = Form(None), key: UploadFile = Form(None)):
    cipher = encrypt_otp(plain_text, await read_file(key))
    return cipher
    
@app.post('/otp_encrypt_file')
async def otp_encrypt_file(plain_file: UploadFile = File(None), key: UploadFile = Form(None)):
    cipher = encrypt_otp(await read_file(plain_file), await read_file(key))
    return cipher

@app.post('/otp_decrypt_file')
async def otp_decrypt_file(cipher_file: UploadFile = File(None), key: UploadFile = Form(None)):
    plain = decrypt_otp(await read_file(cipher_file), await read_file(key))
    return plain

@app.post('/otp_decrypt')
async def otp_decrypt(cipher_text: str = Form(None), key: UploadFile = Form(None)):
    plain = decrypt_otp(cipher_text, await read_file(key))
    return plain

@app.post('/create_key')
async def create_key():
    return StreamingResponse(await write_file(generate_random_key(10000)), media_type='text/plain')


# enigma
@app.post('/enigma_text')
async def enigma_text(text: str = Form(None), key_1: str = Form(None), key_2: str = Form(None), key_3: str = Form(None)):
    result = enigma(text, key_1 + key_2 + key_3)
    return result

@app.post('/enigma_file')
async def enigma_text(files: UploadFile = File(None), key_1: str = Form(None), key_2: str = Form(None), key_3: str = Form(None)):
    result = enigma(await read_file(files), key_1 + key_2 + key_3)
    return StreamingResponse(await write_file(result), media_type='text/plain')
