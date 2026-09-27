# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.assigned_subjects = set()
        self.can_teach_subjects = can_teach_subjects


def create_schedule(subjects, teachers):

    uncovered_subjects = set(subjects)
    selected_teachers = []

    while uncovered_subjects:
        best_teacher = None
        best_coverage = 0

        for teacher in teachers:
            coverage = len(uncovered_subjects.intersection(teacher.can_teach_subjects))

            if coverage > 0 and (
                coverage > best_coverage
                or (
                    coverage == best_coverage
                    and (best_teacher is None or teacher.age < best_teacher.age)
                )
            ):

                best_coverage = coverage
                best_teacher = teacher

        if best_teacher is None:

            return None  # Неможливо покрити всі предмети

        best_teacher.assigned_subjects = uncovered_subjects.intersection(
            best_teacher.can_teach_subjects
        )
        selected_teachers.append(best_teacher)
        uncovered_subjects -= best_teacher.can_teach_subjects

    return selected_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.gritsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
