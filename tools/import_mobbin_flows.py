from pathlib import Path
import shutil
import re

root = Path(r"C:\Working\Apple-Note Clone\docs\apple-notes\flows")
downloads = Path(r"C:\Users\82106\Downloads")
source_names = [
    "Searching Apple Notes (voice input)", "Editing text format", "Adding a checklist", "Checking off a checklist",
    "Adding a table", "Deleting a row", "Adding a link", "Scanning text", "Scanning a document", "Setting up camera",
    "Quick look", "Switching to small view", "Renaming a scanned document", "Deleting a scanned document", "Opening gallery view",
    "Taking a photo", "Recording an audio", "Showing transcript", "Renaming a recording", "Deleting a recording", "Playing a recording",
    "Adding a file attachment", "Editing a note (marker)", "Showing a ruler", "Selecting a color", "Saving a color", "Adding a sticker",
    "Adding text", "Adding a signature", "Changing a label", "Adding a shape", "Editing a shape", "Adding a loupe", "Pinning a note",
    "Locking a note", "Opening a locked note", "Finding in a note", "Moving a note", "Opening a recent note", "Solving a math equation",
    "Changing a number", "Inserting a space above", "Removing a result", "Adding lines & grids", "Switching attachment view to large",
    "Deleting a note", "Switching to gallery view", "Sorting notes", "Turning off group by date", "View attachments", "Creating a new smart folder",
    "Moving a note to folder", "Renaming a folder", "Deleting a folder", "Converting to smart folder", "Reordering folders", "Deleting a tag",
]

def slug(value: str) -> str:
    value = value.lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")

for index, name in enumerate(source_names, start=63):
    folder = root / slug(name)
    shots = folder / "screenshots"
    shots.mkdir(parents=True, exist_ok=True)
    source = downloads / f"file ({index}).webp"
    target = shots / "01.webp"
    if source.exists():
        shutil.copy2(source, target)
    (folder / "README.md").write_text(
        f"""# {name}\n\n- App: Apple Notes iOS\n- Capture status: captured\n- Source: [Mobbin Apple Notes flows](https://mobbin.com/apps/apple-notes-ios-201a63f1-7499-4ebe-b92d-401605aa41bb/1782dd26-1259-4ebf-b402-384a81685971/flows)\n\n## Flow chart\n\n```mermaid\nflowchart LR\n  A[Entry] --> B[{name}]\n  B --> C[Observed result]\n```\n\n## Reference screen\n\n![{name}](screenshots/01.webp)\n\n## BMad handoff notes\n\n- Record the observed entry point, action, result, and any destructive or reversible state here.\n- Promote confirmed behavior into `EXPERIENCE.md`; promote visual decisions into `DESIGN.md`.\n""",
        encoding="utf-8",
    )
