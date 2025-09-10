import requests

r = requests.get('https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID=an238&section=103')
print(r.json())
