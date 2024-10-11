from typing import Dict

# A utility function to register any number of functions
def register_function(
    func_name: str, description: str, params: Dict[str, Dict[str, str]]
) -> Dict[str, Dict[str, Dict[str, Dict[str, str]]]]:
    """
    A utility function to register any number of functions.

    Args:
        func_name: The name of the function to register.
        description: A description of the function.
        params: A dictionary of parameters for the function, with keys as the
            parameter names and values as dictionaries with two keys: 'type' and
            'description'.

    Returns:
        A JSON object that represents the function registration.
    """
    return {
        'type': 'function',
        'function': {
            'name': func_name,
            'description': description,
            'parameters': {
                'type': 'object',
                'properties': params,
                'required': list(params.keys()),
            }
        }
    }
