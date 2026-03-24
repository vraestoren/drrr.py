<h1>
  <img src="https://github.com/user-attachments/assets/281fba2f-ab2e-489b-ae30-6074165b45e1" width="28" style="vertical-align:middle;" />
  drrr.py
</h1>

> Web-API for [drrr.com](https://drrr.com) to interact with the Durarara!! Dollars chatroom

<p align="center">
  <img src="https://pbs.twimg.com/media/Ed4-RWsUEAAmmci.jpg" alt="Drrr.com" width="400"/>
</p>

---

## Quick Start

```python
from drrr import Drrr

drrr = Drrr()

# Login with a nickname and icon
drrr.login(nickname="Dollars", icon="kuromu-2x")

# Browse available rooms
lounge = drrr.get_lounge()
print(lounge)
```

> On instantiation, `Drrr` automatically fetches the auth and session tokens — no manual setup needed before calling `login()`.

---

## Features

- 🔐 **Auth** — automatic token handling, login with nickname and icon
- 🏠 **Rooms** — create, join, leave, and edit chat rooms
- 💬 **Messaging** — send public or private messages, share URLs
- 🎵 **Music** — play music in rooms
- 👥 **Moderation** — kick, ban, transfer host
- 📋 **Lounge** — browse all available rooms
- 👤 **Profile** — get your current session info

---

## Usage

### Auth

```python
drrr = Drrr(language="en-US")

# Login (must be called before any room actions)
drrr.login(nickname="Dollars", icon="kuromu-2x")

# Get your current session/profile
drrr.get_current_session()
```

### Available Icons

Some valid icon values: `kuromu-2x`, `setton-2x`, `walker-2x`, `erika-2x`, `simon-2x`, `dotachin-2x`, `anri-2x`, `celty-2x`, `izaya-2x`, `shizuo-2x`

### Rooms

```python
# Browse the lounge (all available rooms)
drrr.get_lounge()

# Create a room
drrr.create_room(
    name="Dollars HQ",
    description="Welcome to the Dollars.",
    users_limit=10,
    music=True,
    adult=False,
    conceal=False,
)

# Join a room by ID
drrr.join_room(room_id="abc123")

# Get current room info
drrr.get_room_info()

# Edit current room
drrr.edit_room(title="New Name", description="New description")

# Leave current room
drrr.leave_room(room_id="abc123")
```

### Messaging

```python
# Send a public message
drrr.send_message(message="Hello Dollars!")

# Send a private message to a user
drrr.send_message(message="Hey", to="user_id_here")

# Send a message with a URL
drrr.send_message(message="Check this out", url="https://example.com")
```

### Music

```python
drrr.play_music_in_room(name="Track Name", url="https://example.com/track.mp3")
```

### Moderation (host only)

```python
# Kick a user
drrr.kick_user(user_id="user_id_here")

# Ban a user
drrr.ban_user(user_id="user_id_here")

# Transfer host to another user
drrr.transfer_host(user_id="user_id_here")
```

---

## API Reference

| Method                | Description                                    |
|-----------------------|------------------------------------------------|
| `login`               | Sign in with nickname and icon                 |
| `get_current_session` | Get your profile and session info              |
| `get_lounge`          | List all available rooms                       |
| `get_room_info`       | Get info about the current room                |
| `create_room`         | Create a new chat room                         |
| `join_room`           | Join a room by ID                              |
| `leave_room`          | Leave the current room                         |
| `edit_room`           | Edit the current room's name or description    |
| `send_message`        | Send a message (public or private)             |
| `play_music_in_room`  | Share music in the current room                |
| `kick_user`           | Kick a user from the room (host only)          |
| `ban_user`            | Ban a user from the room (host only)           |
| `transfer_host`       | Transfer host privileges to another user       |

---
