# app.wsgi

from app import app  # Remplacez "mon_application" par le nom de votre module/application

# Créez l'application WSGI en utilisant l'instance de votre application
app = app

# Configurez des options de déploiement si nécessaire
# Par exemple, définissez des variables d'environnement, configurez la gestion des erreurs, etc.
# Vous pouvez personnaliser cette partie en fonction de vos besoins spécifiques de déploiement.
