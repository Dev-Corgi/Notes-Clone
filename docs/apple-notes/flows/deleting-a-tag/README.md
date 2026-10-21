# Deleting a tag from Folders

- Source: [Mobbin flow](https://mobbin.com/flows/00973aef-3c12-49e9-9e96-a8e8b3aa690c)
- App: Apple Notes iOS
- Entry surface: Folders
- Screen count: 5
- Capture status: captured

## Flow chart

```mermaid
flowchart LR
  A[Folders] --> B[Open tag controls]
  B --> C[Delete tag]
  C --> D{Confirm deletion?}
  D -->|Cancel| B
  D -->|Confirm| E[Tag removed]
```

## Screens

### 1. Folders
![Folders](screenshots/01.webp)

### 2. Tag controls
![Tag controls](screenshots/02.webp)

### 3. Delete action
![Delete action](screenshots/03.webp)

### 4. Confirmation state
![Confirmation state](screenshots/04.webp)

### 5. Result
![Tag removed](screenshots/05.webp)

## Observations

- Deletion is a destructive action with a confirmation branch.
- Cancel returns to the tag context without changing the list.
- Confirm ends in a visibly updated Folders state.
