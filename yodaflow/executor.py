import yaml
from typing import Dict, Any

def run_workflow(workflow_path: str, role: str, context: dict) -> None:
    with open(workflow_path, 'r') as file:
        data = yaml.safe_load(file)
    return data