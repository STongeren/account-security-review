# How my email got hacked, and how I investigated it like a SOC case

I've had the same email address since I was a kid. Back then I used one password everywhere. It ended up in data breaches, my address showed up on [Have I Been Pwned](https://haveibeenpwned.com), and anyone with that password could log in. That's how my Epic Games account got taken over.

About a year ago I fixed the basics: new passwords and two-factor authentication (2FA) on everything important. In November 2026, now studying cyber security, I went back and investigated the account properly, the way a SOC analyst investigates a compromised mailbox.

This repo has three parts:
- **[The investigation](#the-investigation)** of my own account (below)
- **[A 15-minute checklist](CHECKLIST.md)** so you can check your own account
- **[A leaked-password checker](tools/check_password.py)** that tells you if a password is in known breaches, without ever sending the password

Personal details (addresses, phone numbers, codes, device names) are left out on purpose.

---

## Timeline

| When | What happened |
|---|---|
| Years ago | One password reused on many sites. One of them gets breached |
| After that | My address appears in breach lists. Accounts get taken over, including Epic Games |
| September 2025 | I change my passwords and turn on 2FA on the important accounts |
| July 2026 | Epic Games sends me a "new device" sign-in code that I didn't request |
| November 2026 | I investigate the account as a SOC case (this repo) |

The July 2026 email is the most interesting part. A 2FA code is only sent **after** the right password is entered. So someone still had a working Epic Games password, but **2FA stopped them**.

---

## The investigation

### What I checked, and why

| Area | Why attackers care |
|---|---|
| Sign-in activity (30 days) | Shows logins from unknown countries or devices |
| Inbox rules | Attackers add rules that hide or delete security emails ([MITRE T1564.008](https://attack.mitre.org/techniques/T1564/008/)) |
| Forwarding | Attackers forward all mail to themselves ([MITRE T1114.003](https://attack.mitre.org/techniques/T1114/003/)) |
| POP and IMAP | Old mail protocols let apps read the mailbox |
| Apps with access | A granted app keeps access even after a password change |
| Verification methods | Unknown or weak recovery methods are a way back in |
| Linked devices | Unknown devices tied to the account |

### Findings

| # | Finding | Assessment |
|---|---|---|
| 1 | Only 2 sign-ins in 30 days, both from my own PC and country, during this review | No sign of someone else inside |
| 2 | No inbox rules | Clean |
| 3 | Forwarding off | Clean |
| 4 | POP and IMAP on, but not used by me | Unneeded attack surface |
| 5 | 2FA on | Good |
| 6 | SMS still a verification method | SMS codes can be stolen with a SIM swap |
| 7 | 8 apps with access, several unused for years (oldest from 2016), including 3 mail apps | Old grants are a quiet way back in |
| 8 | One linked device: my own PC, still on Windows 10 (out of support) | Mine, but needs an upgrade |
| 9 | Epic Games "new device" code I didn't request (July 2026) | Someone had a working password there ([credential stuffing, T1110.004](https://attack.mitre.org/techniques/T1110/004/)). 2FA blocked it |
| 10 | A software vendor told me my password appeared in a leak | Confirms an old password is out there |
| 11 | Lots of fake delivery and "subscription" phishing, with letters split by dashes and dots | Phishing that tries to slip past spam filters ([T1566](https://attack.mitre.org/techniques/T1566/)). Not proof of a hack: the address is on spam lists |

### What I think happened

An old reused password was breached. Attackers tried the same email and password on other sites (credential stuffing). That explains the old takeovers, the code from Epic Games and the leak warning. The spam is a separate problem: the address sits in leaked lists, and that doesn't go away.

### Actions

| Action | Status |
|---|---|
| New passwords and 2FA on important accounts | Done (September 2025) |
| Checked rules, forwarding, sign-ins, devices | Done, nothing suspicious |
| Turned off POP and IMAP | Done, verified after reload |
| New unique password on Epic Games | To do |
| Remove apps I no longer use | To do |
| Replace SMS with an authenticator app or passkey | To do |
| New recovery code, stored offline | To do |
| Upgrade the PC from Windows 10 | To do |

### What I learned

- **Spam is not a compromise.** Sign-in logs, rules, forwarding and app grants tell you whether someone is actually inside.
- **2FA works.** In July 2026 an attacker had a working password and still couldn't get in.
- **A new password isn't enough.** App grants and old protocols can keep a door open.
- **Reuse turns one breach into many.** Unique passwords from a password manager stop credential stuffing.
- These are the same checks a SOC runs for a business email compromise, just on a personal account.
