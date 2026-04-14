from src.modules.{{ module_name }}.schemas import {{ module_class }}Create, {{ module_class }}Read


class {{ module_class }}Service:
    async def create(self, payload: {{ module_class }}Create) -> {{ module_class }}Read:
        # Replace with real persistence logic.
        return {{ module_class }}Read(id=1)
