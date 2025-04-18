import requests

def advice_context(request):
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=3)
        data = response.json()
        return {"advice": data.get("slip", {}).get("advice", "Consejo no disponible.")}
    except:
        return {"advice": "Consejo no disponible."}