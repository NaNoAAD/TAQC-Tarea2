from playwright.async_api import Page
import asyncio

class MenuDesplegable:
    def __init__(self, page: Page):
        #Definicion de selectores
        self.page = page
        self.burger_menu_button = "#react-burger-menu-btn"  #Boton menu desplegable
        self.logout_link = "#logout_sidebar_link"   #Boton logout
    
    async def logout(self):
        #Realiza el logout desde el menú lateral
        await self.page.click(self.burger_menu_button)
        # Pequeña espera para dar tiempo a despleguie de menu
        await asyncio.sleep(1)
        await self.page.click(self.logout_link)
        print("Logout completado")