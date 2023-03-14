import csv


def get_maria_most_ordered(data):
    maria_orders = {}

    for order in data:
        if order['cliente'] == 'maria':
            dish = order['pedido']
            if dish in maria_orders:
                maria_orders[dish] += 1
            else:
                maria_orders[dish] = 1

    return max(maria_orders, key=maria_orders.get)


def get_arnaldo_hamburguer_orders(data):
    arnaldo_hamburguers = 0

    for order in data:
        if order['cliente'] == 'arnaldo' and order['pedido'] == 'hamburguer':
            arnaldo_hamburguers += 1

    return arnaldo_hamburguers


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

    maria = get_maria_most_ordered(data)
    arnaldo = get_arnaldo_hamburguer_orders(data)