# 공통 데이터
students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}},
]


# 📌 평균 계산 함수 (재사용용)
def get_average(subjects: dict) -> float:
    return sum(subjects.values()) / len(subjects)


# 1️⃣ 학생별 평균
def calculate_student_averages(students: list) -> dict:
    averages = {}

    for student in students:
        name = student["name"]
        avg = get_average(student["subjects"])
        averages[name] = round(avg, 2)

    return averages


# 2️⃣ 특정 과목 평균
def calculate_subject_average(students: list, subject_name: str) -> float:
    scores = [
        student["subjects"][subject_name]
        for student in students
        if subject_name in student["subjects"]
    ]

    if not scores:
        return 0

    return round(sum(scores) / len(scores), 2)


# 3️⃣ 최고 평균 학생
def find_top_student(students: list) -> dict:
    if not students:
        return None

    top = max(students, key=lambda s: get_average(s["subjects"]))
    avg = get_average(top["subjects"])

    return {
        "name": top["name"],
        "average": round(avg, 2),
    }


# 4️⃣ 우수 학생 (모든 과목 기준 이상)
def find_excellent_students(students: list, threshold: int = 80) -> list:
    return [
        student["name"]
        for student in students
        if all(score >= threshold for score in student["subjects"].values())
    ]


# ✅ 실행
print(calculate_student_averages(students))
print(calculate_subject_average(students, "과학"))
print(find_top_student(students))
print(find_excellent_students(students))