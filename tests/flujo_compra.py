import asyncio
from playwright.async_api import async_playwright
from pages.login import PaginaLogin
from pages.inventario import PaginaInventario
from pages.carrito import PaginaCarrito
from pages.menuDesplegable import MenuDesplegable

async def Flujo_compra():
    print("Empezando prueba de flujo de compra")

    async with async_playwright() as p:
        # Lanzamiento navegador
        browser = await p.chromium.launch(headless=False,
                                          args=["--start-maximixed"])

        # Instancia de nueva página
        page = await browser.new_page()
        
        # Inicialización de las páginas/componentes
        login = PaginaLogin(page)
        inventario = PaginaInventario(page)
        carrito = PaginaCarrito(page)
        menu = MenuDesplegable(page)
        
        # Inicio de Prueba
        await login.navegar()
        await login.login("standard_user", "secret_sauce")
        
        await inventario.mochila_a_carrito()
        await inventario.ir_a_carrito()
        
        # Espera explicita para ver resultados
        await asyncio.sleep(2)

        if carrito.mochila_visible:
            print("Prueba EXITOSA: Mochila agregada\n")
        else:
            print("Prueba FALLIDA: Mochila no encontrada en carrito\n")
        
        await menu.logout()
        
        # Espera explicita para ver resultados
        await asyncio.sleep(1)
        
        # Cerrar el navegador
        await browser.close()

# Ejecutar la prueba
if __name__ == "__main__":
    asyncio.run(Flujo_compra())