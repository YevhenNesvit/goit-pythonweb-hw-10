from fastapi import APIRouter, Depends, UploadFile, File
from app.auth.jwt_handler import get_current_user
from app.middleware.rate_limiter import rate_limiter
import cloudinary
import cloudinary.uploader
from app.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserRead)
async def get_current_user_info(current_user: UserRead = Depends(get_current_user)):
    rate_limiter.check_rate_limit(str(current_user.id))
    return current_user
