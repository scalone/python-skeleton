import yaml
import os

path = os.path.join(os.path.dirname(__file__), "..", 'config', 'application.yaml')
environment = os.getenv('SKELETON_ENV', 'development')
with open(path, "r") as f:
    settings = yaml.load(f)[environment]

settings["credential_blabla"] = os.getenv('CREDENTIAL_BLABLA', settings["credential_blabla"])
settings["token"]             = os.getenv('CREDENTIAL_S3'    , settings["token"])
