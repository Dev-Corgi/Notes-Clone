# Apple Notes iOS flows

Source: [Mobbin — Apple Notes iOS flows](https://mobbin.com/apps/apple-notes-ios-201a63f1-7499-4ebe-b92d-401605aa41bb/1782dd26-1259-4ebf-b402-384a81685971/flows)

Mobbin 페이지에는 총 76개 플로우가 표시됩니다. 카테고리를 펼쳐 원본 플로우 이름과 링크를 확인했습니다. 아래 문서는 현재 저장한 레퍼런스와 앞으로 스크린샷을 채울 카탈로그를 구분합니다.

## 플로우 카탈로그

| # | 플로우 | 상태 | 문서 |
|---:|---|---|---|
| 01 | Reordering folders | screenshots captured | [열기](reordering-folders/README.md) |
| 02 | Deleting a tag | screenshots captured | [열기](deleting-a-tag/README.md) |
| 03–76 | Mobbin 전체 플로우 카탈로그 | names and source links captured | 아래 목록 |

## 확인한 플로우 목록

### Notes

Notes; Searching Apple Notes; Searching Apple Notes (voice input); Creating a note; Editing text format; Adding a checklist; Checking off a checklist; Adding a table; Deleting a row; Adding a link; Scanning text; Scanning a document; Setting up camera; Quick look; Switching to small view; Renaming a scanned document; Deleting a scanned document; Opening gallery view; Taking a photo; Recording an audio; Showing transcript; Renaming a recording; Deleting a recording; Playing a recording; Adding a file attachment; Editing a note (marker); Showing a ruler; Selecting a color; Saving a color; Adding a sticker; Adding text; Changing text color; Editing text; Converting text to handwriting; Adding a signature; Changing a label; Adding a shape; Editing a shape; Adding a loupe; Pinning a note; Locking a note; Opening a locked note; Finding in a note; Moving a note; Opening a recent note; Solving a math equation; Changing a number; Inserting a space above; Removing a result; Adding lines & grids; Switching attachment view to large; Deleting a note; Switching to gallery view; Sorting notes; Turning off group by date; View attachments.

### Folders

Folders; Recently deleted; Tags; Adding a new folder; Creating a new smart folder; Moving a note to folder; Renaming a folder; Deleting a folder; Converting to smart folder; Reordering folders; Deleting a tag.

## 상태 기준

- `screenshots captured`: 원본 화면을 저장하고 플로우 문서에 연결했습니다.
- `names and source links captured`: Mobbin 원본 목록과 링크를 확인했으며, 개별 문서와 스크린샷을 순차적으로 채울 수 있는 상태입니다.

## 기록 규칙

각 플로우 문서는 관찰 사실, 화면 순서, 사용자 동작, 분기를 구분합니다. Mermaid는 화면 간 전이를 요약하고, 원본 스크린샷은 `screenshots/`에 번호 순서로 저장합니다.

```mermaid
flowchart LR
  A[Start] --> B[Screen]
  B --> C[Action]
  C --> D[Next screen]
```

