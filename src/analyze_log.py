import csv
from collections import Counter


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            data = [
                info for info in csv.DictReader(
                    file, fieldnames=["cliente", "pedido", "dia"]
                )]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_orders = {}

    for order in data:
        if order['cliente'] == 'maria':
            dish = order['pedido']
            if dish in maria_orders:
                maria_orders[dish] += 1
            else:
                maria_orders[dish] = 1

    maria_most_ordered_dish = max(maria_orders, key=maria_orders.get)

    print(maria_most_ordered_dish)
