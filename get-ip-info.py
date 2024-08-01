#!/usr/bin/env python3

import sys
import requests


def main(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    ip_data = response.json()

    if ip_data['status'] != 'success':
        print("Введите верный айпи-адрес.")
    else:
        print(
            f"{ip_address}:"
            f"\n  - Address: {ip_data['country']}, {ip_data['regionName']} ({ip_data['region']}), {ip_data['city']}"
            f"\n  - Timezone: {ip_data['timezone']}"
            f"\n  - Organization: {ip_data['org']}"
            f"\n"
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Используйте: get_ip_info <айпи-адрес>")
    else:
        main(sys.argv[1])
