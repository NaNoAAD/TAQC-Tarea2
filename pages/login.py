from playwright.async_api import Page

class PaginaLogin:
    def __init__(self, page: Page):
        self.page = page
        # Definicion de los selectores que se usan el Login
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.url = "https://www.saucedemo.com/"
    
    async def navegar(self):
        #Acceso a la pagin ade login
        await self.page.goto(self.url)
        print("Ingreso a página de login")
    
    async def login(self, username, password):
        #Se ingresan los datos a la pagina de login, para finalmente dar click a boton Login
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)
        await self.page.click(self.login_button)
        print(f"Login completado con usuario: {username}")