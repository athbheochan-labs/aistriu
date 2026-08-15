from typing import Annotated

from fastapi import Depends, Request

from app.domains.weblate.manager import WeblateManager


def get_weblate_manager(request: Request) -> WeblateManager:
    return request.app.state.weblate_manager


WeblateManagerDep = Annotated[WeblateManager, Depends(get_weblate_manager)]
