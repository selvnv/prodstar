class Delivery:

  is_started: bool = False
  driver_lon: float = 0.0
  driver_lat: float = 0.0

  def __init__(
    self,
    product1: str,
    amount1: int,
    product2: str,
    amount2: str
  ):
    self.product1 = product1
    self.amount1 = amount1
    self.product2 = product2
    self.amount2 = amount2


class Driver:

  def __init__(self, lon: float, lat: float):
    self.lon = lon
    self.lat = lat

  def start_delivery(self, delivery: Delivery):
    delivery.is_started = True
    self.update_delivery(delivery)

  def update_delivery(self, delivery: Delivery):
    delivery.driver_lon = self.lon
    delivery.driver_lat = self.lat


class Customer:

    def __init__(self, address: str):
      self.address = address

    def get_delivery_status(self, delivery: Delivery) -> str:
      if delivery.is_started:
        location = geocode(self.address)
        p = math.pi/180
        a =\
          0.5 - math.cos((location.lat-delivery.driver_lat)*p)/2 +\
          math.cos(location.lat*p) * math.cos(delivery.driver_lat*p) *\
          (1-math.cos((location.lon-delivery.driver_lon)*p))/2
        distance =  12742 * math.asin(math.sqrt(a))
        return f"Driver is {distance:.1f} km away"
      else:
        return "Delivery hasn't been started yet"

    def update_order(self, delivery: Delivery, product: str, amount: str) -> str:
      if delivery.is_started:
        return "Cannot modify started delivery"
      elif delivery.product1 == product:
        delivery.amount1 = amount
        return "Success"
      elif delivery.product2 == product:
        delivery.amount2 = amount
        return "Success"
      else:
        return "Delivery cannot contain more than 2 products"


def delivery_scenario():
  customer = Customer("Moscow, Ulitsa Pyatnitskaya, 3")
  delivery = Delivery("apples", 1, "oranges", 2)
  customer.get_delivery_status(delivery)
  # 'Delivery hasn't been started yet'
  customer.update_order(delivery, "apples", 3)
  # 'Success'
  customer.update_order(delivery, "peaches", 5)
  # 'Delivery cannot contain more than 2 products'

  driver = Driver(37.1, 55.2)
  driver.start_delivery(delivery)

  customer.get_delivery_status(delivery)
  # 'Driver is 22.0 km away'
  customer.update_order(delivery, "apples", 4)
  # 'Cannot modify started delivery'

  driver.lon = 37.2
  driver.lat = 55.3
  driver.update_delivery(delivery)

  customer.get_delivery_status(delivery)
  # 'Driver is 12.7 km away'
