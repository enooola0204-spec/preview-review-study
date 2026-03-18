# 1)

# # 학생별 평균을 저장할 빈 딕셔너리 생성 -> {이름: 평균점수}

# def calculate_student_averages(students:list) -> dict:

#     averages = {}

# ​

# # students 리스트 안에 있는 각 학생 정보를 하나씩 꺼냄

# # 한 명씩 반복 처리

#     for student in students:

# # 현재 학생의 "name" 값을 가져와 name 변수에 저장

#         name = student["name"]

# # 현재 학생의 "subjects" 딕셔너리를 가져옴

#         subjects = student["subjects"]

# # 평균

#         average = sum(subjects.values()) / len(subjects)

# # 소수점 둘째 자리 반올림

#         averages[name] = round(average, 2)

# ​

# # 평균 딕셔너리 반환  

#     return averages

# ​

# print(calculate_student_averages(students))

# ​

# ​

# 2)

# ​

# students = [

#     {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},

#     {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},

#     {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},

#     {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}

# ]

# ​

# # students:list 학생 정보가 들어있는 리스트

# # subjects_name:str 평균을 구할 과목 이름

# # 이 함수는 실수 값을 반환

# def calculate_subject_average(students:list, subject_name:str) -> float:

# # 해당 과목의 총 점수를 저장할 변수

#     total_score = 0

# # 해당 과목을 듣는 학생 수를 세기 위한 변수

#     student_count = 0

# ​

# # students 리스트에서 학생을 한 명씩 꺼내 반복

#     for student in students:

# # 현재 학생이 그 과목을 듣고 있는지 확인

#         if subject_name in student["subjects"]:

# # 해당 과목 점수 가져와 total_score에 더함

#             total_score += student["subjects"][subject_name]

# # 해당 과목을 수강하는 학생 수를 1 증가

#             student_count += 1

# # 만약 그 과목을 듣는 학생이 한명도 없다면

#     if student_count == 0:

# # 0 반환

#         return 0

# # 평균, 소수점 둘째 자리까지 반올림

#     return round (total_score / student_count, 2)

# ​

# print(calculate_subject_average(students, "과학"))

# print(calculate_subject_average(students, "수학"))

# print(calculate_subject_average(students, "영어"))

# ​

# 3)

# students = [

#     {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},

#     {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},

#     {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},

#     {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}

# ]

# ​

# ​

# # students 리스트를 받아서

# # 가장 평균 점수가 높은 학생 정보를 딕셔너리로 반환

# def find_top_student(students: list) -> dict:

#     # 만약 students 리스트가 비어 있다면

#     # 비교할 학생이 없으므로 None 반환

#     if not students:

#         return None

# ​

#     # max() 함수로 students 중에서 가장 큰 값을 찾기

#     # 큰 값은 key 조건에 의해 결정

#     top = max(

#         students, #비교 대상은 students 리스트 전체

#         # 각 student의 평균 점수를 계산해서

#         # 평균 기준으로 가장 큰 값을 선택

#         key=lambda student: sum(student["subjects"].values()) / len(student["subjects"])

#     )

# ​

#     # top 평균 반환용으로 다시 계산

#     average = sum(top["subjects"].values()) / len(top["subjects"])

# ​

#     # 딕셔너리 형태로 결과 반환

#     return {

#         "name": top["name"],

#         "average": round(average, 2)

#     }

# ​

# print(find_top_student(students))

# ​

# 4)

# students = [

#     {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},

#     {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},

#     {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},

#     {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}

# ]

# ​

# def find_excellent_students(students:list, threshold:int=80) -> list:

#     excellent_students = []

    

#     for student in students:

#         name = student["name"]

#         subjects = student["subjects"]

        

#         # 모든 과목의 점수가 기준점수 이상인지 확인

#         all_above_threshold = all(score >= threshold for score in subjects.values())

        

#         if all_above_threshold:

#             excellent_students.append(name)

    

#     return excellent_students

# ​

# print(find_excellent_students(students))