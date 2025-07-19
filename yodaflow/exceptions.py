class WorkflowValidationError(Exception):
    """Error when validating a workflow structure (Invalid YAML, lacking fields etc)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
