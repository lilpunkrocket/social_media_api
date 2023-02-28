from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(tags=["Authetication"])

@router.post('/login', response_model=schemas.Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                        detail=f'Invalid Credentials')

    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                        detail=f'Invalid Credentials')
    
    # create a token
    acces_token = oauth2.create_acces_token(data={"user_id": user.id})
    return {"acces_token": acces_token, "token_type": "beaber"}