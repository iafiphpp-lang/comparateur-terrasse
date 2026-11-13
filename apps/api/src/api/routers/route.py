from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

_COMPARATEUR = Path(__file__).resolve().parent.parent / "static" / "comparateur-terrasse.html"


@router.get("/", operation_id="comparateur_home", summary="Comparateur de terrasse", include_in_schema=False)
async def comparateur_home() -> FileResponse:
    return FileResponse(_COMPARATEUR, media_type="text/html", filename="comparateur-terrasse.html")
