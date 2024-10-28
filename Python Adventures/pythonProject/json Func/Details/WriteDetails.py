import json

my_data = {
    "people":[
        {
            'Name': 'Md Aftab',
            'Dept': 'Cse-Ds',
            'Roll No': '22/cse-ds/032',
            'Age': 21, 'CGPA': 8.5
        },
        {
            'Name': 'Md Aftab',
            'Dept': 'Cse-Ds',
            'Roll No': '22/cse-ds/032',
            'Age': 21, 'CGPA': 8.5
        },
        {
            'Name': 'Md Aftab',
            'Dept': 'Cse-Ds',
            'Roll No': '22/cse-ds/032',
            'Age': 21, 'CGPA': 8.5
        }
    ]
}
data = json.dumps(my_data, indent=4)
with open("Details.json", "w") as f:
    f.write(data)