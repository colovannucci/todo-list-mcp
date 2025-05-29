from fastapi import HTTPException, status

def raise_404_if_none(resource, detail: str = "Resource not found"):
    if resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    return resource
