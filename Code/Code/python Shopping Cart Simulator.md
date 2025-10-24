catalog = {"apple": 1.5, "banana": 0.8, "milk": 2.0, "bread": 2.5}

cart = []

def add(product, qty):

    for i, (p, q) in enumerate(cart):

        if p == product:

            cart[i] = (p, q + qty)

            return

    cart.append((product, qty))

def remove(product):

    global cart

    cart[:] = [item for item in cart if item[0] != product]

def total():

    return sum(catalog[p] * q for p, q in cart if p in catalog)

add("apple", 3)

add("apple", 2)

add("milk", 1)

remove("milk")

print("Cart:", cart)

print("Total:", total())


1. catalog = {"apple": 1.5, "banana": 0.8, "milk": 2.0, "bread": 2.5} - перемеенная где мы сохраняем словарь товаров.
2. cart = [] - переменная, корзина покупок в которую мы добавляем пустой список, в который мы будем добавлять товары.
3. def add(product, qty):
    for i, (p, q) in enumerate(cart):
        if p == product:
            cart[i] = (p, q + qty)
            return
    cart.append((product, qty)) - функция создания корзины в которой мы будем добавлять товар, туда у нас идёт имя товара (product) и количество (qty). Далее идёт перебираение элементов (card), enumerate даёт и индекс i, и сам товар (p, q), р - название товара в корзине, q - его количество. 
4.  if p == product:
    cart[i] = (p, q + qty)
    return      -    если товар уже в корзине (p == product), то: обновляем его количество: q + qty. , return — выход из функции,  добавление закончено.
5.  cart.append((product, qty)) - если товара ещё нет в корзине — добавляем (product, qty).
6. def remove(product):
    global cart
    cart = [item for item in cart if item[0] != product]  - сначала идёт функция remove которая удаляет товар из корзины. За тем мы создаём новый список оставляя только те товары, имя которых не равно product.
То есть — удаляем нужный товар.
7. def total():
    return sum(catalog[p] * q for p, q in cart if p in catalog) - функция total() возвращает общую сумму заказа. sum(...) — складывает всё, что внутри. for p, q in cart — проходимся по всем товарам и их количеству. catalog[p] — получаем цену товара из каталога. catalog[p] * q — считаем стоимость товара: цена × количество. if p in catalog - только если товар есть в каталоге (на всякий случай)
8. add("apple", 3)
add("apple", 2)
add("milk", 1)
remove("milk") - Добавляем 3 яблока - потом ещё 2 - итого 5 яблок. Добавляем 1 молоко. Удаляем молоко.
9. print("Cart:", cart)
print("Total:", total()) - показываем что в корзине 5 яблок и итог.