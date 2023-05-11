from peewee import *

db = PostgresqlDatabase('notes', user='justinsotolongo', password='1234', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    content = CharField()

def note_taker():
    db.create_tables([Note])
    user_input = input('Welcome to Note Taker! What would you like to do while here?\nCreate a note (type: create),\nUpdate a note (type: update),\nDelete a note (type: delete),\nor view all notes (type: view)\nor exit (type: exit)?:\n')
    # user_input2 = input('What else would you like to do while here?\ncreate, update, delete, view, or exit?:\n')
    if user_input.lower() == 'create':
        note_title = input('Note Title: ')
        note_contents = input('Note Contents: ')
        note1 = Note(title= f'{note_title}', content= f'{note_contents}')
        note1.save()
        print(note1.content)
        note_taker()
    elif user_input.lower() == 'update':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_update_input = input("What note would you like to edit?\n")
        note_update = Note.get(Note.title == f'{note_update_input}')
        note_update_detail = input("Do you want to edit the title or the content?\n")
        if note_update_detail.lower() == 'title':
            note_update_title = input("What would you like to to be instead?\n")
            note_update.title = note_update_title
            note_update.save()
        elif note_update_detail.lower() == 'content':
            note_update_content = input("What would you like to to be instead?\n")
            note_update.content = note_update_content
            note_update.save()
        note_taker()
    elif user_input.lower() == 'delete':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_delete_input = input("What note would you like to delete? Input the title of the note\n")
        note_delete = Note.get(Note.title == f'{note_delete_input}')
        note_delete.delete_instance()
        note_taker()
    elif user_input.lower() == 'view':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_find_title = input("Which note would you like to view:\n")
        note_title = Note.select().where(Note.title == f'{note_find_title}')
        if note_title.exists():
            print([note.content for note in note_title])
        else :
            print('Does not exist. Check spelling')
        note_taker()
    elif user_input.lower() == 'exit':
        print('Bye Bye')
        return
    else:
        print('Please type in a valid response!')
        note_taker()
        
note_taker()