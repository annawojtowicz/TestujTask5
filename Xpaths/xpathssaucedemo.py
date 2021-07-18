class XpathsSauceDemo:
    username = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'
    standard_user = 'standard_user'
    locked_out_user = 'locked_out_user'
    problem_user = 'problem_user'
    performance_glitch_user = 'performance_glitch_user'
    password_input = 'secret_sauce'
    inventory_container = '//div[@id="inventory_container"]'
    error = '//h3[contains(text(), "Sorry, this user has been locked out")]'
    filters = '//span[@class="select_container"]'
    filters_A_to_Z = '//select[@class="product_sort_container"]/option[@value="az"]'
    first_product_on_list = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    remove = '//button[@id="remove-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'
    product_in_shopping_cart = '//div[@class="inventory_item_name"]'
    checkout = '//button[@id="checkout"]'
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'
    finish_button = '//button[@id="finish"]'
    successfull_order = '//div[contains(text(), "Your order has been dispatched, and will arrive just as fast as the pony can get there!")]'
    url = 'https://www.saucedemo.com/'
    inventory_url = 'https://www.saucedemo.com/inventory.html'






