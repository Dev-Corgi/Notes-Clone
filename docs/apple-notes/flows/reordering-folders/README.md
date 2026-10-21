# Reordering folders from Folders

- Source: [Mobbin flow](https://mobbin.com/flows/e929a163-5ebc-465f-98af-165689d5ecad)
- App: Apple Notes iOS
- Entry surface: Folders
- Screen count: 4
- Capture status: captured

## Flow chart

```mermaid
flowchart LR
  A[Folders] --> B[Edit folders]
  B --> C[Drag folder]
  C --> D[Folders reordered]
```

## Screens

### 1. Folders
![Folders](screenshots/01.webp)

### 2. Edit folders
![Edit folders](screenshots/02.webp)

### 3. Drag folder
![Drag folder](screenshots/03.webp)

### 4. Reordered result
![Reordered result](screenshots/04.webp)

## Observations

- The flow starts from the Folders surface.
- Reordering is a direct manipulation gesture with a visible positional result.
- The final state remains inspectable after the gesture completes.
