import csv


def get_joao_orders(data):
    joao_dishes = set()
    joao_days = set()

    for order in data:
        if order['cliente'] == 'joao':
            joao_dishes.add(order['pedido'])
            joao_days.add(order['dia'])

    all_dishes = set(order['pedido'] for order in data)
    all_days = set(order['dia'] for order in data)

    return all_dishes - joao_dishes, all_days - joao_days


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
    joao_dishes, joao_days = get_joao_orders(data)

    with open('data/mkt_campaign.txt', mode='w') as file:
        new_file = '\n'.join([
            maria,
            str(arnaldo),
            str(joao_dishes),
            str(joao_days)
        ])
        file.write(new_file)
