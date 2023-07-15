import json

from note import Note


def save_notes(notes, filename='notes.json'):
    notes_dicts = [note.to_dict() for note in notes]
    with open(filename, 'w') as f:
        json.dump(notes_dicts, f)


def load_notes(filename='notes.json'):
    try:
        with open(filename, 'r') as f:
            notes_dicts = json.load(f)
        return [Note.from_dict(note_dict) for note_dict in notes_dicts]
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump([], f)
        return []


def create_note(notes, id, title, body):
    note = Note(id, title, body)
    notes.append(note)
    return notes


def update_note(notes, id, title, body):
    for note in notes:
        if note.id == id:
            note.update(title, body)
    return notes


def delete_note(notes, id):
    notes = [note for note in notes if note.id != id]
    return notes
