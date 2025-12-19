import requests
import sys

def fuzz():
    url = input("Enter the url to fuzz: ").strip()
    wordlist = input("Enter the wordlist path: ").strip()


    try:
        with open(wordlist, "r") as f:
            payloads = f.read().splitlines()
    except FileNotFoundError:
        print("[-] Wordlist not found")
        sys.exit()
    except PermissionError:
        print("[-] Permission denied for wordlist")
        sys.exit()

    for payload in payloads:
        fuzzed_url = url.rstrip("/") + "/" + payload
        response = requests.get(fuzzed_url)

        # 🔹 Skip 404 responses
        if response.status_code == 404:
            continue

        content_type = response.headers.get("Content-Type", "")

        print(f"\n[+] Endpoint Found: {fuzzed_url}")
        print(f"[+] Status Code: {response.status_code}")

        if "application/json" in content_type:
            try:
                print("[+] JSON Response:")
                print(response.json())
            except ValueError:
                print("[-] Invalid JSON response")
        else:
            print("[+] HTML / Text Response:")
            print(response.text[:500])  # limit output

fuzz()
