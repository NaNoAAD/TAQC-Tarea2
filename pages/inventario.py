from playwright.async_api import Page

class PaginaInventario:
    def __init__(self, page: Page):
        #Definicion de selectores iniciales
        self.page = page
        self.backpack_add_button = "#add-to-cart-sauce-labs-backpack"   #Mochila Objetivo
        self.cart_link = ".shopping_cart_link"  #boton de carrito luego de agregar la mochila
    
    async def mochila_a_carrito(self):
        #Agrega la mochila al carrito
        await self.page.click(self.backpack_add_button)
        print("Mochila agregada al carrito")
    
    async def ir_a_carrito(self):
        #Navega al carrito de compras
        await self.page.click(self.cart_link)
        print("Navegando al carrito")