import os

def handle(event, context):
    try:
        # Chemin local vers le dossier depot dans le contexte de la fonction
        base_dir = os.path.dirname(__file__)
        depot_path = os.path.join(base_dir, "depot")

        # Vérifie si le dossier existe
        if not os.path.exists(depot_path):
            return {
                "statusCode": 404,
                "body": f"Le répertoire 'depot/' n'existe pas dans la fonction."
            }

        files = [f for f in os.listdir(depot_path) if os.path.isfile(os.path.join(depot_path, f))]
        file_count = len(files)

        return {
            "statusCode": 200,
            "body": f"Nombre de fichiers dans depot/ : {file_count}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Erreur : {str(e)}"
        }
