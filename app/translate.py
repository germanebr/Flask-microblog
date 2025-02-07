import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
            'Ocp-Apim-Subscription-Region': 'eastus'}
    
    r = requests.post('https://api.congnitive.microsofttranslator.com/translate?api-version=3.0&from')