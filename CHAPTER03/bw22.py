# 딕셔너리와 튜플보다는 헬퍼 클래스로 관리하자

class SimpleGradebook(object):
	"""docstring for SimpleGradebook"""
	def __init__(self):
		# super(SimpleGradebook, self).__init__()
		# self.arg = arg
		self._grades = {}

	def add_student(self, name):
		self._grades[name] = []

	def report_grade(self, name, score):
		self._grades[name].append(score)

	def average_grade(self, name):
		grades = self._grades[name]
		return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)

print(book.average_grade('Isaac Newton'))


# Example

class BySubjectGradebook(object):
	def __init__(self):
		self._grades = {}

	def add_student(self, name):
		self._grades[name] = {}

	def report_grade(self, name, subject, grade):
		by_subject = self._grades[name]
		grade_list = by_subject.setdefault(subject, [])
		grade_list.append(grade)

	def average_grade(self, name):
		by_subject = self._grades[name]
		total, count = 0, 0
		for grades in by_subject.values():
			total += sum(grades)
			count += len(grades)
		return total / count


book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))


# 클래스 리팩토링
grades = []
grades.append((95, 0.45))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
print (average_grade)

# Example
grades = []
grades.append((95, 0.45, 'Great job'))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grade = total / total_weight
print (average_grade)


# Example
import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
	def __init__(self):
		self._grades = []

	def report_grade(self, score, weight):
		self._grades.append(Grade(score, weight))

	def average_grade(self):
		total, total_weight = 0, 0
		for grade in self._grades:
			total += grade.score * grade.weight
			total_weight += grade.weight
		return total / total_weight


class Student(object):
	def __init__(self):
		self._subjects = {}

	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()
		return self._subjects[name]

	def average_grade(self):
		total, count = 0, 0
		for subject in self._subjects.values():
			total += subject.average_grade()
			count += 1
		return total / count


class Gradebook(object):
    def __init__(self):
    	self._students = {}

    def student(self, name):
    	if name not in self._students:
    		self._students[name] = Student()
    	return self._students[name]

book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(80, 0.10)
math.report_grade(70, 0.80)
gym = albert.subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())
