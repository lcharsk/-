recipes = {}
with open("recipes.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        recipe_name, ingredients_str = line.split(":", 1)
        clean_ingredients = []
        for item in ingredients_str.split(","):
            clean_ingredients.append(item.strip())
        recipes[recipe_name.strip()] = clean_ingredients

print("\n=== КНИГА РЕЦЕПТОВ ===")
print(f"Количество рецептов в книге: {len(recipes)}")
print("Список рецептов:")
for name in recipes:
    print(f"- {name}")
    
def find_by_products(products, recipes):
    products = [p.strip().lower() for p in products.split(",")]
    available = {}
    partial = {}
    
    for recipe_name, ingredients in recipes.items():
        present = [ing for ing in ingredients if ing in products]
        missing = [ing for ing in ingredients if ing not in products]
        if not missing:
            available[recipe_name] = ingredients
        elif present:
            partial[recipe_name] = missing    
    return available, partial

def find_by_name(search, recipes):
    search = search.strip().lower()
    found = {}
    for recipe_name, ingredients in recipes.items():
        if search in recipe_name.lower():
             found[recipe_name] = ingredients
    return found

print("\nВыберите режим: \n1 - Поиск по продуктам \n2 - Поиск по названию")
choice = input("\nВаш выбор: ")

if choice == "1":
    user_products = input("Введите продукты (через запятую): ")
    available, partial = find_by_products(user_products, recipes)

    print("\n=== РЕЗУЛЬТАТ ===")
    if available:
        print("\n✅ Можно приготовить:\n")
        for recipe, ingredients in available.items():
            print(f"• {recipe}")
            print(f"  Ингредиенты: {', '.join(ingredients)}")
 
    if partial:
        print("\n🛒 Нужно докупить:\n")
        for recipe, missing in partial.items():
            print(f"• {recipe}")
            print(f"  Не хватает: {', '.join(missing)}")

    if not available and not partial:
        print("\n❌ Подходящих рецептов нет")

elif choice == "2":
    search = input("\nВведите название рецепта: ")
    found = find_by_name(search, recipes)

    print("\n=== РЕЗУЛЬТАТ ===")
    if found:
        for recipe, ingredients in found.items():
            print(f"\n• {recipe}")
            print(f"  Ингредиенты: {', '.join(ingredients)}")

    else:
        print("\n❌ Рецепт не найден")

else:
    print("\n❌ Неверный выбор")
