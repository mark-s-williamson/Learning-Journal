from dataclasses import dataclass
from typing import Callable, Dict, Any
from faker import Faker
from dataclasses import dataclass
from datetime import datetime, timezone
import random

fake = Faker()
random.seed(42)

@dataclass
class Schema:
    name: str
    generator: Callable[[int], Dict[str, Any]]

def _now():
    return datetime.now(timezone.utc).isoformat()

def clicks_schema() -> Schema:
    def gen(i: int) -> Dict[str, Any]:
        return {
            "event_type": "click",
            "event_id": f"clk-{i:08d}",
            "ts": _now(),
            "user_id": fake.uuid4(),
            "page": random.choice(["/", "/search", "/product", "/cart", "/checkout"]),
            "device": random.choice(["mobile", "desktop", "tablet", "smart_tv", "smarterToaster"])                           
        }
    return Schema(name="clicks", generator=gen)

def orders_schema() -> Schema:
    def gen(i: int) -> Dict[str, Any]:
        return {
            "event_type": "order",
            "event_id": f"ord-{i:08d}",
            "ts": _now(),
            "customer_id": fake.uuid4(),
            "amount": round(random.uniform(5.0, 500.0), 2)
        }
    return Schema(name="orders", generator=gen)

def sensors_schema() -> Schema:
    def gen(i: int) -> Dict[str, Any]:
        return {
            "event_type": "sensor",
            "event_id": f"sns-{i:08d}",
            "ts": _now(),
            "sensorid": random.randint(1,50),
            "sensor_value": random.randint(1,100)
        }
    return Schema(name="sensors", generator=gen)


SCHEMAS = {"clicks": clicks_schema(), "orders": orders_schema(), "sensors": sensors_schema()}


