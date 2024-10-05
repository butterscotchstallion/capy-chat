from fastapi import APIRouter

user_router = APIRouter()


@user_router.post("/user/sign-on")
def user_sign_on():
    return {"status": "OK"}
