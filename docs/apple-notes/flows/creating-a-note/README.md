# Creating a note

- Source: [Mobbin detail flow](https://mobbin.com/flows/243b2ee1-b668-4d16-a4af-70fabe323188)
- App: Apple Notes iOS
- Device: iOS 393×852
- Screen count: 6
- Capture status: verified

## Flow chart

```mermaid
flowchart LR
  A[Notes empty state] -->|Tap compose| B[Blank note editor]
  B -->|Type note content| C[UI/UX content entered]
  C -->|Continue editing| D[Content editor with keyboard]
  D -->|Dismiss keyboard| E[Content editor with bottom toolbar]
  E -->|Back to Notes| F[Notes list with new note]
```

## Screens

### 1. Notes — empty state

![Notes empty state](screenshots/01.webp)

The Notes list is empty and exposes the compose button beside the bottom search field.

### 2. Blank note editor

![Blank note editor](screenshots/02.webp)

A new note opens in edit mode. The keyboard is visible, with formatting controls above it and the done button in the top right.

### 3. Note content entered

![Note content entered](screenshots/03.webp)

The note contains the headings `UI/UX`, `UI (User Interface)`, and `UX (User Experience)`. The insertion point remains in the editor while the keyboard and inline formatting controls are available.

### 4. Content editor with keyboard

![Content editor with keyboard](screenshots/04.webp)

The same content remains editable with the keyboard open. The formatting row exposes bold, italic, underline, strikethrough, drawing, link, and list controls.

### 5. Content editor with bottom toolbar

![Content editor with bottom toolbar](screenshots/05.webp)

After the keyboard is dismissed, the note stays in edit mode and the bottom toolbar exposes checklist, attachment, and markup actions.

### 6. Notes list with new note

![Notes list with new note](screenshots/06.webp)

Returning to the list shows the newly created `UI/UX` note among the notes grouped under `Today`.

## BMad handoff notes

- Entry state: Notes has no notes and shows the compose action.
- Primary interaction: create a note, enter multiline content, dismiss the keyboard, and return to the list.
- Expected result: the new note is persisted and appears in the Notes list under the current date group.
- Reversible state: the note remains editable from the list after creation.
