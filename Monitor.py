from playwright.sync_api import sync_playwright
import json 
import requests
import os

def enviar_telegram(mensaje):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    datos = {
        "chat_id": chat_id,
        "text": mensaje
    }

    respuesta = requests.post(url, data=datos, timeout=15)
    respuesta.raise_for_status()
    return respuesta.json()

with open("estado.json", "r", encoding="utf-8") as archivo:
    estado_anterior = json.load(archivo)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://cyberleek.perma.online")

    page.locator(".content-title").first.wait_for()

    items = page.locator("#card-content .content-item")

    contenido = []

    estado = {}

    for item in items.all():
        titulo = item.locator(".content-title").inner_text()
        enlaces = item.locator("a").evaluate_all(
            "(links) => links.map(a => ({texto: a.innerText, url: a.href}))"
        )
        
        urls = []
        for enlace in enlaces:
            urls.append(enlace["url"])
        estado[titulo] = urls
        
        
        contenido.append({
    "titulo": titulo,
    "enlaces": enlaces
})

    browser.close()

nuevos = set(estado) - set(estado_anterior)

for titulo in nuevos:
    mensaje = f"🚨 Nuevo título detectado:\n\n{titulo}"

    for url in estado[titulo]:
        mensaje += f"\n{url}"

    enviar_telegram(mensaje)
    print(f"Notificación enviada: {titulo}")

for titulo in nuevos:
    print(titulo)
    for enlace in estado[titulo]:
        print(f"   {enlace}")

with open("estado.json", "w", encoding="utf-8") as archivo:
    json.dump(estado, archivo, indent=4, ensure_ascii=False)