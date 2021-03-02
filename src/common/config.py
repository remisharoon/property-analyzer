# import yaml
# import re
# import os
from envyaml import EnvYAML

# path_matcher = re.compile(r'\$\{([^}^{]+)\}')
# def path_constructor(loader, node):
#   ''' Extract the matched value, expand env variable, and replace the match '''
#   value = node.value
#   match = path_matcher.match(value)
#   env_var = match.group()[2:-1]
#   return os.environ.get(env_var) + value[match.end():]
#
# yaml.add_implicit_resolver('!path', path_matcher)
# yaml.add_constructor('!path', path_constructor)

# try:
#     with open("config.yaml", "r") as ymlfile:
#         cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
# except Exception as e:
#     try:
#         with open("../config.yaml", "r") as ymlfile:
#             cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
#     except Exception as e:
#         with open("../../config.yaml", "r") as ymlfile:
#             cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

try:
    cfg = EnvYAML(yaml_file='config.yaml', strict=False)
except Exception as e:
    try:
        cfg = EnvYAML('../config.yaml')
    except Exception as e:
        cfg = EnvYAML('../../config.yaml')


print(cfg['ibm_credentials.auth_endpoint'])
print("IBM_RESOURCE_INSTANCE_ID = ", cfg['ibm_credentials.resource_instance_id'])

# iam_serviceid_crn: ${IBM_SERVICEID_CRN}