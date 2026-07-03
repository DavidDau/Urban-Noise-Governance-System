from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """User login request schema"""
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    """User login response schema"""
    access_token: str
    token_type: str
    user_id: int


class RegisterRequest(BaseModel):
    """User registration request schema"""
    email: EmailStr
    password: str
    full_name: str


class Token(BaseModel):
    """Token schema"""
    access_token: str
    token_type: str
