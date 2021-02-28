import yaml
try:
    with open("../config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
except Exception as e:
    with open("../../config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
