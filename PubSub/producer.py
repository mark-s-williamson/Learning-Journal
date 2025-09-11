import json
import time
import random
import argparse
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def make_event(i: int):
    return {
        "event_type": "click",
        "event_id": f"clk-{i:08d}",
        "ts": now_iso(),
        "user_id": fake.uuid4(),
        "page": random.choice(["/", "/search", "/product", "/cart", "/checkout"] ),
        "device": random.choice(["desktop", "mobile", "tablet", "smart_tv"])
    }

def main():
    p =argparse.ArgumentParser()
    p.add_argument("--max", type=int, default=20, help="How many events to emit (0 = infinite)")
    p.add_argument("--rate", type=float, default=10.0, help="Events per second")
    p.add_argument("--dest", choices=["stdout", "file"], default="file", help="Where to send events")
    p.add_argument("--filepath", default="stream.jsonl", help="File path to write events if --dest=file")
    args = p.parse_args()

    i = 0
    sleep_s = (1.0 / args.rate if args.rate > 0 else 0)
    out = open(args.filepath, "a", encoding="utf-8") if args.dest == "file" else None

    for i in range(args.max + 1) if args.max > 0 else iter(int, 1):
            line = json.dumps(make_event(i)) + "\n"
            if out:
                out.write(line)
            else:
                print(line, end="")

            if sleep_s > 0:
                time.sleep(sleep_s)    

    if out:
        out.close()


if __name__ == "__main__":
    main()
