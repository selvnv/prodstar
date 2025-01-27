class Driver:

  def __init__(self, lon: float, lat: float):
    self.lon = lon
    self.lat = lat

  def update_position(self, lon: float, lat: float):
    self.lon = lon
    self.lat = lat


class DistanceService:

  def get_distance(self, lon: float, lat: float, address: str) -> float:
    location = geocode(address)
    p = math.pi/180
    a =\
      0.5 - math.cos((location.lat-lat)*p)/2 +\
      math.cos(location.lat*p) * math.cos(lat*p) *\
      (1-math.cos((location.lon-lon)*p))/2
    return 12742 * math.asin(math.sqrt(a))


class Delivery:

  driver: Optional[Driver] = None
  distance_service = DistanceService()

  def validate_order(order: Dict[str, int]):
    if not (len(order) > 0 and len(order) <= 2):
      raise ValueError("Delivery cannot contain more than 2 products")

  def __init__(self, order: Dict[str, int], address: str):
    Delivery.validate_order(order)
    self.order = order
    self.address = address

  def start(self, driver):
    self.driver = driver

  def is_started(self) -> bool:
    return self.driver is not None

  def get_status(self) -> str:
    if self.is_started():
      distance = 
        self.distance_service.get_distance(
          driver.lon,
          driver.lat,
          self.address
        )
      return f"Driver is {distance:.1f} km away"
    else:
      return "Delivery hasn't been started yet"

  def update_order(self, product: str, amount: str) -> str:
    if self.is_started():
      return "Cannot modify started delivery"
    else:
      new_order = self.order.copy()
      new_order[product] = amount
      try:
        Delivery.validate_order(new_order)
      except ValueError as e:
        return str(e)
      self.order = new_order
      return "Success"


class Customer:

    delivery: Optional[Delivery] = None

    def __init__(self, address: str):
      self.address = address

    def order_delivery(self, order: Dict[str, int]) -> Delivery:
      self.delivery = Delivery(order, self.address)
      return self.delivery

    def get_delivery_status(self) -> str:
      if self.delivery is not None:
        return self.delivery.get_status()
      else:
        return "No delivery ordered"

    def update_order(self, product: str, amount: str) -> str:
      if self.delivery is not None:
        return self.delivery.update_order(product, amount)
      else:
        return "No delivery ordered"


def delivery_scenario_v2():
  customer = Customer("Moscow, Ulitsa Pyatnitskaya, 3")
  delivery = customer.order_delivery({"apples": 1, "oranges": 2})
  customer.get_delivery_status()
  customer.update_order("apples", 3)
  customer.update_order("peaches", 5)

  driver = Driver(37.1, 55.2)
  delivery.start(driver)

  customer.get_delivery_status()
  customer.update_order("apples", 4)

  driver.update_position(37.2, 55.3)
  customer.get_delivery_status()
