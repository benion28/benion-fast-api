from pydantic import BaseModel
from typing import Optional, List


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[any] = None
    error: Optional[str] = None
    errors: Optional[List[dict]] = None
    pagination: Optional[dict] = None
