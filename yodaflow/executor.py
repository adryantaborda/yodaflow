import yaml

# read a yaml file
def yaml_reader(yaml_file: str):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data

