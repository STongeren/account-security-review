# 15-minute account check

The same checks I ran on my own account. Do them for your main email, because whoever owns your email can reset every other password.

## Microsoft (Outlook, Hotmail, Live)

| # | Check | Where | Red flag |
|---|---|---|---|
| 1 | Recent sign-ins | [account.live.com/Activity](https://account.live.com/Activity) | A country, device or time that isn't you |
| 2 | Inbox rules | Outlook → Settings → Mail → Rules | A rule you didn't make, especially one that deletes, moves or marks mail as read |
| 3 | Forwarding | Outlook → Settings → Mail → Forwarding and IMAP | Forwarding to an address you don't know |
| 4 | POP and IMAP | same page | On, while you don't use a mail app that needs it |
| 5 | Apps with access | [account.live.com/consent/Manage](https://account.live.com/consent/Manage) | Apps you don't recognize or haven't used in years |
| 6 | Verification methods and 2FA | [account.microsoft.com/security](https://account.microsoft.com/security) | 2FA off, or a phone number or email that isn't yours |
| 7 | Devices | [account.microsoft.com/devices](https://account.microsoft.com/devices) | A device you don't own |

## Google (Gmail)

| # | Check | Where | Red flag |
|---|---|---|---|
| 1 | Recent security activity and devices | [myaccount.google.com/security](https://myaccount.google.com/security) | Sign-ins or devices that aren't you |
| 2 | Filters and forwarding | Gmail → Settings → See all settings → "Filters and Blocked Addresses" and "Forwarding and POP/IMAP" | A filter or forwarding address you didn't make |
| 3 | Apps with access | [myaccount.google.com/connections](https://myaccount.google.com/connections) | Apps you don't recognize |
| 4 | 2-Step Verification | [myaccount.google.com/signinoptions/twosv](https://myaccount.google.com/signinoptions/twosv) | Off |

## For every account

- [ ] Is your address in a breach? Check [haveibeenpwned.com](https://haveibeenpwned.com)
- [ ] Is your password in a breach? Use [the checker in this repo](tools/check_password.py) or [haveibeenpwned.com/Passwords](https://haveibeenpwned.com/Passwords)
- [ ] One unique password per site, from a password manager (for example [Bitwarden](https://bitwarden.com), free)
- [ ] 2FA with an authenticator app or passkey, not SMS
- [ ] A recovery code, stored offline

## Found something?

1. Change the password from a device you trust.
2. Sign out everywhere (Microsoft: Security → Advanced security options → Sign out everywhere).
3. Delete the rule, forwarding address or app you don't recognize.
4. Turn on 2FA.
5. Change the password on every other site where you used the same one.
