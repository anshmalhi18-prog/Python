student_data={"id1":{"name":"Sarah","Class":5,"Subject":"Math, English, Science"},
              "id2":{"name":"Ansh","Class":5,"Subject":"Math, English, Science"},
              "id3":{"name":"Sarah","Class":5,"Subject":"Math, English, Science"},
              "id4":{"name":"Josh","Class":5,"Subject":"Math, English, Science"}}

result={}
seen_keys=[]

for student_id,details in student_data.items():
    unique_key=(details["name"],details["Class"],details["Subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

for k,v in result.items():
    print(k,":",v)