scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

passed_students = []
total_score = 0
max_score = -1
top_student = ""

print("--- وضعیت دانشجویان ---")
for name, score in scores.items():

  if score >= 17:
    status = "عالی"
  elif score >= 14:
    status = "خوب"
  elif score >= 10:
    status = "قبول"
  else:
    status = "مردود"

  print(f"{name}: {score} - {status}")

  if score >= 10:
    passed_students.append(name)

  total_score += score

  if score > max_score:
    max_score = score
    top_student = name

print("\nقبول شده ها:", passed_students)

class_average = total_score / len(scores)
print(f"میانگین کلاس {class_average}")

print(f"نفر اول : {top_student}")