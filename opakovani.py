# from source_data import MENU
# from source_data import resources
#
# # === Základní nastavení ===
# espresso_price = MENU["espresso"]["cost"]
# latte_price = MENU["latte"]["cost"]
# cappuccino_price = MENU["cappuccino"]["cost"]
#
# # === Funkce ===
# def report(data):
#     print(f"Voda: {data['water']}")
#     print(f"Mléko: {data['milk']}")
#     print(f"Káva: {data['coffee']}")
#
# def coins():
#     print("Prosím vložte mince 1, 2, 5, 10, 20, 50")
#     kc1 = int(input("Kolik 1 Kč chcete vložit?: "))
#     kc2 = int(input("Kolik 2 Kč chcete vložit?: ")) * 2
#     kc5 = int(input("Kolik 5 Kč chcete vložit?: ")) * 5
#     kc10 = int(input("Kolik 10 Kč chcete vložit?: ")) * 10
#     kc20 = int(input("Kolik 20 Kč chcete vložit?: ")) * 20
#     kc50 = int(input("Kolik 50 Kč chcete vložit? ")) * 50
#     suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
#     print(f"Celkem jste vložili: {suma} Kč")
#     return suma
#
# def calculate_change(user_sum_coins, price):
#     refund = user_sum_coins - price
#     if refund >= 0:
#         print("Nápoj se připravuje")
#         if refund > 0:
#             print(f"Zde jsou peníze zpět: {refund} Kč")
#     else:
#         print(f"Nevhodili jste dostatek peněz. Ještě je zapotřebí vložit {price - user_sum_coins} Kč")
#
# def fill_in_ingredients():
#     return resources
#
# def consumption_ingredience(name_of_drink, ingredients):
#     ingredients["water"] = ingredients["water"] - MENU[name_of_drink]["ingredients"]["water"]
#     ingredients["milk"] = ingredients["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
#     ingredients["coffee"] = ingredients["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
#     print(f"zbylé ingredience: {ingredients}")
#
# def calculate_ingredients(drink_name):
#     if drink_name == "espresso":
#         consumption_ingredience("espresso", rest_of_ingredience)
#     elif drink_name == "latte":
#         consumption_ingredience("latte", rest_of_ingredience)
#     elif drink_name == "cappuccino":
#         consumption_ingredience("cappuccino", rest_of_ingredience)
#
# def ingredient_check(in_water, in_milk, in_coffee):
#     if in_water < 0:
#         print("Nemáme dostatek ingrediencí na tento nápoj")
#         return False
#     elif in_milk < 0:
#         print("Nemáme dostatek ingrediencí pro tento nápoj")
#         return False
#     elif in_coffee < 0:
#         print("Nemáme dostatek ingrediencí pro tento nápoj")
#         return False
#     else:
#         print("Na Váš nápoj máme dostatek ingrediencí")
#         return True
#
#
# # === Kód automatu ===
# # Načítáme původní množství ingrediencí
# rest_of_ingredience = fill_in_ingredients()
#
# lets_continue = True
#
# while(lets_continue):
#     # Volba uživatele - jaký chce nápoj
#     user_choice = input("Co by ste si dal/a (espresso/latte/cappuccino): ")
#
#     # Kontrolní report
#     if user_choice == "report":
#         report(rest_of_ingredience)
#
#     # Kontrola, zda máme dostatek ingrediencí
#     if user_choice != "report":
#         lets_continue = ingredient_check(rest_of_ingredience["water"], rest_of_ingredience["milk"], rest_of_ingredience["coffee"])
#
#     # Má kód dále pokračovat?
#     if lets_continue == False:
#         break
#
#     # Vypočítá kolik zbývá ingrediencí
#     calculate_ingredients(user_choice)
#
#
#     # Hlavní kód automatu
#     if user_choice == "espresso":
#         pay = coins()
#         print(f"cena espressa je {espresso_price}")
#         calculate_change(pay, espresso_price)
#     elif user_choice == "latte":
#         pay = coins()
#         print(f"cena latte je {latte_price}")
#         calculate_change(pay, latte_price)
#     elif user_choice == "cappuccino":
#         pay = coins()
#         print(f"cena cappuccino je {cappuccino_price}")
#         calculate_change(pay, cappuccino_price)

