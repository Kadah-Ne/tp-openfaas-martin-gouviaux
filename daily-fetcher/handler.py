import json
from datetime import datetime

def handle(event, context):
    """
    Fonction déclenchée tous les jours à 8h.
    Publie un message JSON contenant la date du jour.
    """
    today = datetime.now().strftime('%Y-%m-%d')
    message = {
        "order_date": today
    }
    return json.dumps(message)
