#!/usr/bin/env python3
import argparse
from app import app
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bind", type=str, required=True, action="store", help="listen addr"
    )
    parser.add_argument(
        "--port", type=int, required=True, action="store", help="listen port"
    )
    args = parser.parse_args()
    sys.exit(app.run(host=args.bind, port=args.port))
