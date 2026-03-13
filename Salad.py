def make_recovery_salad(head_hurts=False):
    ingredients = ["огурец", "авокадо", "много_зелени", "фета"]
    dressing = "оливковое_масло + лимонный_сок"
    
    if head_hurts:
        ingredients.append("кедровые_орешки")
        print("Нарезать всё кубиками, залить лимоном, съесть в тишине.")
    return "Status: I will survive"

make_recovery_salad()