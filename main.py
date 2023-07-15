from note_manager import create_note, update_note, delete_note, save_notes, load_notes


def main():
    notes = load_notes()
    while True:
        print("1. Список заметок")
        print("2. Создать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            for note in notes:
                print(note.to_dict())
        elif choice == '2':
            id = input("Введите идентификатор заметки: ")
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes = create_note(notes, id, title, body)
        elif choice == '3':
            id = input("Введите идентификатор заметки: ")
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            notes = update_note(notes, id, title, body)
        elif choice == '4':
            id = input("Введите идентификатор заметки, которую хотите удалить: ")
            notes = delete_note(notes, id)
        elif choice == '5':
            save_notes(notes)
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == '__main__':
    main()
