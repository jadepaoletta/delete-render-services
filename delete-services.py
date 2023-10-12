#!/usr/bin/env python3
import requests
import argparse
import sys

def get_services(namespace, suspended=False):
    limit = 100
    data = []
    url = "https://api.render.com/v1/services"
    payload = { "limit": limit, "ownerId": namespace }

    if suspended:
        payload["suspended"] = "suspended"

    print("Retrieving services for namespace: {}".format(namespace))
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()

    # Get any additional pages
    while len(response.json()) == limit:
        payload["cursor"] = data[-1]["cursor"]
        response = requests.get(url, headers=headers, params=payload)
        data += response.json()

    print("Retrieved {} services\n".format(len(data)))
    return data


def iterate_services(service_data):
    for i in service_data:
        print("Id: " + i["service"]["id"])
        print("Name: " + i["service"]["name"])
        print("Suspended?: " + i["service"]["suspended"])
        print("Namespace: " + i["service"]["ownerId"] + "\n")

        delete_service(i["service"]["id"])


def delete_service(service_id):
    delete = input("Delete service {}? (y/n) (q to quit): ".format(service_id))

    if delete == "y":
        print("Deleting service: {}".format(service_id))

        url = "https://api.render.com/v1/services/{}".format(service_id)
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print("Service deleted successfully\n")
        else:
            print("Error deleting service: {}\n".format(response.status_code))
    if delete == "q":
        print("Exiting...")
        sys.exit()
    else:
        print("Skipping deleting service: {}\n".format(service_id))
    

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--namespace', required=True)
    parser.add_argument('-k', '--api_key', required=True)
    parser.add_argument('--suspended', action='store_true')
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    global headers 
    headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {}".format(args.api_key)
    }
    iterate_services(get_services(args.namespace, args.suspended))
    