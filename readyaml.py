import yaml
import os 
from fastapi import FastAPI
app = FastAPI()

config = {
    "port": 8000,
    "workers": 1,
    "debug": False,
    "log_level": "info",
    "api_key": "default-secret-000"
}

#now we have to update with the layer2 with yaml 
yaml_file_path = "config.development.yaml"
if os.path.exists(yaml_file_path):
    with open(yaml_file_path,'r') as f:
        yaml_data = yaml.safe_load(f)
        if yaml_data:
            config.update(yaml_data) # This overrides the defaults with values from the YAML file
