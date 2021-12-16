def menu_print(fruit, price):
  print(f"{fruit}-{price}")


menu_print(**{
  "price": 2.5,
  "fruit": "apple"
})