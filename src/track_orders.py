class TrackOrders:
    def __init__(self) -> None:
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        orders = {}
        for order in self.orders:
            if order[0] == customer:
                dish = order[1]
                if dish in orders:
                    orders[dish] += 1
                else:
                    orders[dish] = 1
        return max(orders, key=orders.get)

    def get_never_ordered_per_customer(self, customer):
        orders = set()
        orders_by_customer = set()

        for order in self.orders:
            orders.add(order[1])

        for order in self.orders:
            if order[0] == customer:
                orders_by_customer.add(order[1])
        return orders - orders_by_customer

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        days_by_customer = set()

        for order in self.orders:
            days.add(order[2])

        for order in self.orders:
            if order[0] == customer:
                days_by_customer.add(order[2])
        return days - days_by_customer

    def get_busiest_day(self):
        days = {}
        for order in self.orders:
            day = order[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for order in self.orders:
            day = order[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1

        return min(days, key=days.get)
