# purplechoc

Simple password generator. It takes three entries from the user:
- The website requesting a password
- A easy-to-remember password
- Some optional information to be used as salt

The script combines the entries into a single string and uses SHA256 as a hashing algorithm to generate another password, longer and a bit stronger. Aditionally, user can set a upper limit to the length of the password (because some websites limit it anyways.)

You can check it out [clicking here](https://purplechoc.streamlit.app/)

Example:

User enters:
```
target='gmail'
password='my password'
optional='my salt'
```

an shall receive:
```
svd0B7Qfsi0lmhX1PZ1CZEC8cyjta6c90H5iuJPWZNE=
```

## Next steps:
- [ ] Make it so the final result also contain symbols