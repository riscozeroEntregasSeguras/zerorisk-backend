API_HOST = "localhost"
API_PORT = 5000
API_DEBUG = True

CORS_RESOURCES_SETUP = {
    r"/*":
        {
            "methods": "OPTIONS",
            "origins": ["http://localhost:8080",
                        "https://zerorisk-webapp.herokuapp.com/#/home'"]
        }
}
