from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from app.config.settings import base_settings

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        if username and password:
            print("user, pass: ", username, password, base_settings.ADMIN_USERNAME, base_settings.ADMIN_PASSWORD)
            if username == base_settings.ADMIN_USERNAME and password == base_settings.ADMIN_PASSWORD:
                request.session.update({"token": base_settings.TOKEN_FOR_ADMIN_AUTH})

                return True
        request.session.update({"token": base_settings.TOKEN_FOR_ADMIN_AUTH})

        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        print("token:", token)
        if not token:
            return False
        if token == base_settings.TOKEN_FOR_ADMIN_AUTH:
            return True
        return False


authentication_backend = AdminAuth(secret_key=base_settings.SECRET_KEY)
