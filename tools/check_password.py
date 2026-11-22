"""Check if a password appears in known data breaches, without sending the password.

How it stays safe (k-anonymity):
  1. The password is hashed on your own computer with SHA-1.
  2. Only the first 5 characters of that hash are sent to the Pwned Passwords API.
  3. The API answers with every leaked hash that starts with those 5 characters
     (usually hundreds), plus how often each one was seen in breaches.
  4. This script looks for the rest of your hash in that list, locally.

So the API never sees your password or even your full hash.
API: https://haveibeenpwned.com/API/v3#PwnedPasswords

Run:  python tools/check_password.py      (Mac/Linux: python3)
Your typing is hidden while you enter the password.
"""
import getpass
import hashlib
import sys
import urllib.request

API = "https://api.pwnedpasswords.com/range/"


def times_pwned(password: str) -> int:
    digest = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = digest[:5], digest[5:]
    req = urllib.request.Request(API + prefix, headers={"User-Agent": "account-security-review-checker", "Add-Padding": "true"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode("utf-8")
    for line in body.splitlines():
        candidate, _, count = line.partition(":")
        if candidate == suffix:
            return int(count)
    return 0


def main() -> None:
    password = getpass.getpass("Password to check (hidden): ")
    if not password:
        sys.exit("No password entered.")
    try:
        count = times_pwned(password)
    except OSError as exc:
        sys.exit(f"Could not reach the API: {exc}")
    if count:
        print(f"Found in breaches {count:,} times. Don't use this password anywhere.")
    else:
        print("Not found in known breaches. Still: use it on one site only.")


if __name__ == "__main__":
    main()
