from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt

from config import JWT_SECRET, JWT_ALGORITHM

security = HTTPBearer()

def get_current_user(token: str = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload

    except Exception:
        raise HTTPException(status_code=401, detail='Invalid token')