# TP OpenFaas - Rendu

## Partie 1 :
Après la commande `faas-cli list` :
![alt text](image.png)

L’interface graphique de OpenFaas est accessible à l’adresse :
http://localhost:8080/ui/

## Partie 2 :

##### /get-quote/handler.py :

    from random import *
    
    quotes = ["Get the jeans, do the science", "PHILIPPE, VIENS ICI QUE JE TE BUTE", "Qui vit dans un annanas dans la mer ?","Le monde appartiens a ceux qui se levent tôt","presque minuit veut dire qu'il n'etait pas minuit"]
    
    def handle(event, context):
    
    return {
    
    "statusCode": 200,
    
    "body": choice(quotes)
    
    }

##### /save-feedback/requierements.txt :

    redis

##### /save-feedback/handler.py :

    import redis
    from datetime import datetime
    import os

    def handle(event, context):
        try:
            # Lire les secrets
            with open('/var/openfaas/secrets/redis-host', 'r') as f:
                redis_host = f.read().strip()

            with open('/var/openfaas/secrets/redis-port', 'r') as f:
                redis_port = int(f.read().strip())

            # Connexion à Redis
            r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

            # Vérifier la connexion
            if not r.ping():
                return {
                    "statusCode": 500,
                    "body": "Impossible de se connecter à Redis."
                }

            # Exemple d'utilisation : SET et GET
            stamp = datetime.now().strftime('%D - %H:%M')
            r.set(stamp, str(event.body))
            value = r.get(stamp)

            return {
                "statusCode": 200,
                "body": f"Connexion réussie à Redis : clé '{stamp}' = '{value}'"
            }
        
        except Exception as e:
            return {
                "statusCode": 500,
                "body": f"Erreur lors de la connexion à Redis : {str(e)}"
            }

##### stack.yaml :

    version: 1.0
    provider:
    name: openfaas
    gateway: http://127.0.0.1:8080
    functions:
    get-quote:
        lang: python3-http
        handler: ./get-quote
        image: kadah/get-quote:latest
    
    save-feedback:
        lang: python3-http
        handler: ./save-feedback
        image: kadah/save-feedback:latest
        secrets:
        - redis-host
        - redis-port
        annotations:
        topic: "redis-topic"
        labels:
        com.openfaas.scale.min: "1"
        com.openfaas.scale.max: "5"

##### redis.yaml :

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: redis
    namespace: default
    spec:
    replicas: 1
    selector:
        matchLabels:
        app: redis
    template:
        metadata:
        labels:
            app: redis
        spec:
        containers:
        - name: redis
            image: redis:latest
            ports:
            - containerPort: 6379
    ---
    apiVersion: v1
    kind: Service
    metadata:
    name: redis
    namespace: default
    spec:
    selector:
        app: redis
    ports:
    - protocol: TCP
        port: 6379
        targetPort: 6379


## Partie 3 :

`curl http://localhost:8080/function/get-quote` :
![alt text](image-1.png)

`curl http://localhost:8080/function/save-feedback -d "Ceci est un message"` :
![alt text](image-2.png)

### Dashboard Promothéus :

#### get-quote :
![alt text](image-3.png)

#### save-feedback :
![alt text](image-4.png)