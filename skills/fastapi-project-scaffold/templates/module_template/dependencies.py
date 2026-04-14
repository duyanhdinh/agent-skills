from src.modules.{{ module_name }}.service import {{ module_class }}Service


def get_service() -> {{ module_class }}Service:
    return {{ module_class }}Service()
