import yaml
from typing import Dict

_roles_cache: Dict[str, list] = {}

def load_roles(yaml_path: str = "roles.yaml") -> Dict[str, list]:
    global _roles_cache
    if _roles_cache:
        return _roles_cache

    try:
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        roles = data.get("roles", {})
        _roles_cache = {
            role: perms.get("allowed_actions", [])
            for role, perms in roles.items()
        }

        return _roles_cache

    except FileNotFoundError:
        raise FileNotFoundError("roles.yaml file was not founded.")
    except yaml.YAMLError as e:
        raise RuntimeError(f"Error when reading roles.yaml: {e}")
    
def can_execute(role: str, action: str) -> bool:
    roles = load_roles()
    allowed_actions = roles.get(role, [])
    return action in allowed_actions
