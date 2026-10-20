# Joker live tuning

`tuning.json` changes how Joker Poker Club looks **without a new app build**. Merge a change to `main` and
every phone picks it up the next time the game opens (GitHub caches raw files for about five minutes).

| Setting | What it does | Range |
|---|---|---|
| `phone.exposure` | Extra brightness for the lobby and table on phones, in stops. 0 = as built, +1 = twice as bright. | -2 to 3 |
| `phone.fill` | Lifts the shadows on phones. 1 = as built, 2 = shadows twice as light. | 0.2 to 6 |
| `desktop.exposure`, `desktop.fill` | The same, on a computer. | |
| `scale.account` | Size of the sign-in / sign-up screen. 1 = as built, 1.2 = a fifth bigger. | 0.5 to 2 |
| `scale.creator` | Size of the character creator's controls. | 0.5 to 2 |
| `scale.lobby` | Size of the lobby's buttons and cards. | 0.5 to 2 |
| `scale.table` | Size of the table's buttons and labels. | 0.5 to 2 |

The check on every pull request refuses a broken file or a value out of range, so a typo can't reach phones.
This repo is public: never put anything private in it.
