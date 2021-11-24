import pickle

class What_To_Do:
    def __init__(self, action, lib, bookstatus):
        self.action = action

    def save(self, lib, bookstatus):
        with open('venv/lib.pickle', 'wb') as f:
            pickle.dump(lib, f)

        with open('venv/bookstatus.pickle', 'wb') as bst:
            pickle.dump(bookstatus, bst)

    def writerbook(self):
        print("Введите писателя:")
        pisatelb = input()
        print("Введите название книги (можно нескольких, через ';'):")
        imya = input().split(";")

        if self.action == 1:
            print("Введите статус книги (можно нескольких, через ';')")
            wihwb = input().split(";")
            return pisatelb, imya, wihwb
        return pisatelb, imya

    def add_book(self, lib, bookstatus, wtd):
        writer, name, st = wtd.writerbook()

        if writer not in lib.keys():
            lib[writer] = name
            for i in range(len(name)):
                print(f"Книга '{name[i]}' успешно добавлена")
                bookstatus[name[i]] = st[i]
        else:
            for i in range(len(name)):
                if name[i] in lib[writer]:
                    print(f"Книга '{name[i]}' уже добавлена")
                else:
                    lib[writer].append(name[i])
                    print(f"Книга '{name[i]}' успешно добавлена")
                    bookstatus[name[i]] = st[i]
                    print(lib)
                    print(bookstatus)

    def remove_book(self, lib, bookstatus, wtd):
        writer, name = wtd.writerbook()
        for i in name:
            if i not in lib[writer]:
                print(f"Книги '{i}' нет")
            else:
                del lib[writer][lib[writer].index(i)]
                print(f"Книга '{i}' успешно удалена")
                del bookstatus[i]
        if not lib[writer]:
            del lib[writer]
    def remove_writer(self, lib, bookstatus):
        print("Введите писателя:")
        writer = input()
        if writer in lib.keys():
            for i in lib[writer]:
                del bookstatus[i]
            del lib[writer]
            print("Писатель успешно удален")
        else:
            print("Такого писателя нет")

    def check_collection(self, lib):
        if lib.keys():
            for i in sorted(lib):
                if lib[i]:
                    print(f"{i}:", '; '.join(sorted(lib[i])))
        else:
            print("Вы не добавили ни одной книги")

    def check_statuses(self, bookstatus):
        if bookstatus.keys():
            for i in sorted(bookstatus):
                print(f"{i}: {bookstatus[i]}")
        else:
            print("Вы не добавили ни одной книги")