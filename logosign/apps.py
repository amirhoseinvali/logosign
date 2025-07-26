from django.apps import AppConfig
import sys, os

class LogoSignConfig(AppConfig):
    name = "logosign"

    def ready(self):
        argv = ' '.join(sys.argv).lower()
        valid_commands = [
            "runserver",
            "gunicorn",
            "uwsgi",
        ]
        if any(cmd in argv for cmd in valid_commands) and os.environ.get("RUN_MAIN") == "true":
            logosign_path = os.path.join(os.getcwd(), "logosign.ascii")
            if not os.path.exists(logosign_path):
                logosign_path = os.path.join(os.path.dirname(__file__), "default.ascii")
            with open(logosign_path, "r", encoding="utf-8") as file:
                content = file.read()
                print(content)