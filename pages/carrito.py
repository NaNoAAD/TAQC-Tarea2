from playwright.async_api import Page

class PaginaCarrito:
    def __init__(self, page: Page):
        #Definicion de selectores (sin selectores, solo revision)
        self.page = page
        self.mochila_carrito = ".inventory_item_name"

    async def mochila_visible(self, page):
        try:
            is_visible = await self.page.is_visible(self.mochila_carrito)
            return is_visible
        except:
            return False