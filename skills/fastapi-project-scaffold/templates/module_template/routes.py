from fastapi import APIRouter, Depends, status
from src.modules.{{ module_name }}.dependencies import get_service
from src.modules.{{ module_name }}.schemas import {{ module_class }}Create, {{ module_class }}Read
from src.modules.{{ module_name }}.service import {{ module_class }}Service

router = APIRouter(prefix="/{{ module_name }}", tags=["{{ module_name }}"])


@router.post("", response_model={{ module_class }}Read, status_code=status.HTTP_201_CREATED)
async def create_item(
    payload: {{ module_class }}Create,
    service: {{ module_class }}Service = Depends(get_service),
) -> {{ module_class }}Read:
    return await service.create(payload)
