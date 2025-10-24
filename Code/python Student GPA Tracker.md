class CourseTracker:
    def __init__(self, name):
        self.course_name = name
        self.grades = {}

    def add_grade(self, assignment, score):
        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            print("Error: Score must be a number between 0 and 100.")
            return
        self.grades[assignment] = score

    def remove_grade(self, assignment):
        if assignment in self.grades:
            del self.grades[assignment]
            print(f"Removed grade for {assignment}.")
        else:
            print(f"Error: Assignment '{assignment}' not found.")

    def gpa(self):
        if not self.grades:
            return 0.0

        total_points = sum(self.grades.values())
        average_score = total_points / len(self.grades)

        if average_score >= 90:
            return 4.0
        elif average_score >= 80:
            return 3.0
        elif average_score >= 70:
            return 2.0
        elif average_score >= 60:
            return 1.0
        else:
            return 0.0

Разбор: 

1. class CourseTracker: - трекер оценок
2. def __init__(self, name):
    self.course_name = name
    self.grades = {} - name - имя курса, self.course_name - сохраняет имя курса, self.grades - словарь, ключи это название заданий 
3. def add_grade(self, assignment, score):
    if not isinstance(score, (int, float)) or not (0 <= score <= 100):
        print("Error: Score must be a number between 0 and 100.")
        return
    self.grades[assignment] = score - Проверяет, что оценка число от 0 до 100, если проверка не пройдена — выводит ошибку, если всё корректно  добавляет задание в словаре
4. def remove_grade(self, assignment):
    if assignment in self.grades:
        del self.grades[assignment]
        print(f"Removed grade for {assignment}.")
    else:
        print(f"Error: Assignment '{assignment}' not found.") - если задание найдено то удаляется, если такого задания нет выводится ошибка
5.  def gpa(self):
    if not self.grades:
        return 0.0

    total_points = sum(self.grades.values())
    average_score = total_points / len(self.grades)

    if average_score >= 90:
        return 4.0
    elif average_score >= 80:
        return 3.0
    elif average_score >= 70:
        return 2.0
    elif average_score >= 60:
        return 1.0
    else:
        return 0.0 - если оценок нет возвращает 0.0 или считает среднее значение всех оценок или возвращает GPA 


