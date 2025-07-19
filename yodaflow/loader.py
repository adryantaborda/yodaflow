# used for parsing and validating yamls

import yaml
from typing import Dict, Any
from yodaflow.exceptions import WorkflowValidationError

def load_workflow(yaml_path: str) -> Dict[str, Any]:
    try:
        with open(yaml_path, 'r') as file:
            workflow = yaml.safe_load(file)
            if not isinstance(workflow, dict):
                raise WorkflowValidationError(f"Workflow {workflow} is not a dictionary instance.")
        return workflow
    except FileNotFoundError:
        raise WorkflowValidationError(f"Workflow {workflow} not found.")
    except yaml.YAMLError as e:
        raise WorkflowValidationError(e)