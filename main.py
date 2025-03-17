import asyncio
from playwright.async_api import async_playwright

async def main():

    print("Empezando")

    async with async_playwright() as p:
        #Lanzamiento browser
        browser = await p.chromium.launch(headless=False,
                                          args=["--start-maximixed"])

        #Instancia de nueva pagina
        pagina = await browser.new_page()

        # Ir a a Swaglab
        await pagina.goto("https://www.saucedemo.com/")
        print("Ingreso a pagina")

        #Llenado de formulario Login
        await pagina.fill("#user-name", "standard_user")
        await pagina.fill("#password", "secret_sauce")

        #click en Login
        await pagina.click("#login-button")

        #Click boton para agregar mochila sauce-labs-backpack
        await pagina.click("#add-to-cart-sauce-labs-backpack")

        #Click para ver el carrito de compra
        await pagina.click(".shopping_cart_link")

        #Espera explicita para ver resultados
        await asyncio.sleep(2)

        #Click para menu despegable
        await pagina.click("#react-burger-menu-btn")

        #Click para logout
        await pagina.click("#logout_sidebar_link")

        #Espera explicita para ver resultados
        await asyncio.sleep(1)
        
# Ejecutar la función principal (Necesario para iniciar la prueba)
if __name__ == "__main__":
    asyncio.run(main())