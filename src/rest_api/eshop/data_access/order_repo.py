from typing import List, Optional

from eshop.businsess_logic.order import Order

_orders: List[Order] = []


# Сохранить заказ
def save(order: Order):
    for i in range(len(_orders)):
        # Поиск заказа для обновления
        existed_order = _orders[i]
        if existed_order.id == order.id:
            _orders[i] = order
            break
    else:
        # Выполнится только если цикл не был прерван оператором break
        # Т.е. заказ новый
        _orders.append(order)


# Получить заказ по id, или None если не существует такого
def get_by_id(id: str) -> Optional[Order]:
    return next((o for o in _orders if o.id == id), None)


# Получить список заказов на странице page (на каждой странице limit заказов)
def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _orders[start:end]