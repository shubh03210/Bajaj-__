import requests
submission_url = " https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
auth_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTEyNyIsIm5hbWUiOiJTaHViaGFtIEt1c2h3YWhhIiwiZW1haWwiOiJzaHViaGFta3VzaHdhaGEyMjA3ODhAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYzNTAyLCJleHAiOjE3NDY5NjQ0MDJ9.5VpJmVbTkU55kmh4EoKJTbuddE_X5eji93lOW7YN83o"

query_text = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

headers_info = {
    "Authorization": auth_token,
    "Content-Type": "application/json"
}

payload_data = {
    "finalQuery": query_text
}

submission_response = requests.post(submission_url, headers=headers_info, json=payload_data)

print(f"Status Code: {submission_response.status_code}")
print(f"Response: {submission_response.text}")
