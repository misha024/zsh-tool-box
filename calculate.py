#!/usr/bin/env python3
import os
import sys


def main():
    result = None
    while True:
        try:
            if result is None:
                expression = input(" - ").strip()
                result = eval(expression)
            else:
                expression = input(f" - {result:.2f} ").strip()

                if expression.startswith("="):
                    result = eval(expression[1:].strip())
                    continue

                if expression.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    result = None
                    continue

                if expression:
                    expression = f"{result} {expression}" if expression[0] in "+-*/%" else expression
                    result = eval(expression)

        except KeyboardInterrupt:
            sys.exit(0)

        except Exception:
            pass


if __name__ == "__main__":
    main()
