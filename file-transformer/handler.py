import os
import pandas as pd
from datetime import datetime

def handle(event, context):
    try:
        base_dir = os.path.dirname(__file__)
        input_path = os.path.join(base_dir, "input.csv")

        if not os.path.exists(input_path):
            return {
                "statusCode": 404,
                "body": f"Fichier d'entrée introuvable : {input_path}"
            }
        df = pd.read_csv(input_path)

        df['customer'] = df['customer'].str.upper()
        df['product'] = df['product'].str.lower()
        df['Processed-Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['Processed-By'] = "kadah"

        depot_path = os.path.join(base_dir, "status-checker/depot")
        os.makedirs(depot_path, exist_ok=True)

        output_path = os.path.join(depot_path, "output.csv")
        df.to_csv(output_path, index=False)

        return {
            "statusCode": 200,
            "body": f"Transformation réussie, fichier généré : {output_path}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Erreur durant le traitement : {str(e)}"
        }
