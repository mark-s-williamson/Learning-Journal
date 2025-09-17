import json, time, argparse
from schemas import SCHEMAS



def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max", type = int, default=10, help="how many events to emit (0 = infinite)")
    p.add_argument("--rate", type = float, default=5.0, help="events per second")
    p.add_argument("--dest", choices=["stdout", "file"], default="stdout", help="where to send events")
    p.add_argument("--file-path", default= "stream.jsonl", help="where to record events if --dest=file")
    p.add_argument("--schema", choices=SCHEMAS.keys(), default="clicks")
    p.add_argument("--updatetype", choices=["a", "w"], default="a", help="append or write when using --dest=file")
    args = p.parse_args()

    i, sleep_s = 0, (1.0 / args.rate if args.rate > 0 else 0.0)
    #out = open(args.file_path, "w", encoding="utf-8") if args.dest == "file" else None
    out = open(args.file_path, "a" if args.updatetype == "a" else "w", encoding="utf-8") if args.dest == "file" else None

    try:
        for i in range(1, args.max + 1) if args.max > 0 else iter(int, 1):
            payload = SCHEMAS[args.schema].generator(i)
            if args.dest == "stdout":
                print (json.dumps(payload))
            else:
                out.write(json.dumps(payload) + "\n")
                out.flush()
           # print (json.dumps(payload))
            if sleep_s > 0:
                time.sleep(sleep_s)
    finally:
        if out: out.close()

if __name__ == "__main__":
    main()



