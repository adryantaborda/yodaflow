from yodaflow.loader import load_workflow
from typing import Dict, Any
from yodaflow.exceptions import WorkflowValidationError

def validate_workflow(workflow: Dict[str, Any]) -> None:
    if "name" not in workflow:
        raise WorkflowValidationError("'name' camp is mandatory in the workflow.")
    if "steps" not in workflow or not isinstance(workflow["steps"], list):
        raise WorkflowValidationError("'steps' camp is mandatory and needs to be a list.")
    
    for i, step in enumerate(workflow["steps"]):
        if "name" not in step:
            raise WorkflowValidationError(f"Step #{i+1} has no 'name'")
        if "action" not in step:
            raise WorkflowValidationError(f"Step {step['name']} has no 'action'")
        if "required_role" not in step:
            raise WorkflowValidationError(f"Step {step['name']} has no 'required_role'")
