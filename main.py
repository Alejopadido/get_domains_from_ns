import json
import requests

def run():

    # Welcome message
    print("\nWelcome to Reverse NS Lookup Tool - By Alejandro P.D.\n")

    # Ask user for information
    print("Please enter the following information: \n")

    name_server = input("Name server(ns): ")
    api_key = input("API KEY: ")

    # Make the GET request
    response = requests.get(f"https://api.viewdns.info/reversens/?ns={name_server}&apikey={api_key}&output=json")

    # Check if the request was successful
    if response.status_code == 200:

        with open("response.json", "w") as r:
            r.write(response.content.decode("utf-8"))
            
        # Print the response content
        # print(response.content.decode("utf-8"))
    else:
        print("Request failed with status code", response.status_code)


    # Load JSON data from file
    with open("response.json", "r") as f:
        data = json.load(f)

    # Extract the value of the 'domain' key
    value = data["response"]

    # Print number of domains found in the dictionary 'value'
    domains_number = value["domain_count"]
    # print(f"\nDomains found: {domains_number}\n")

    # Save a list of key/value pairs with the domains
    domains = value["domains"]

    # Print and save each domain found in 'domains' list in a file
    with open("domains.txt", "w") as o:

        for item in domains:

            domain = item["domain"]

            o.write(str(domain) + "\n")
    
    print(f"\n{domains_number} domains successfully saved in domains.txt")


if __name__ == '__main__':
    run()