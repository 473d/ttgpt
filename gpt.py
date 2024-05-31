import openai

# استبدل 'your-api-key' بمفتاح API الفعلي الخاص بك من OpenAI
openai.api_key = 'your-api-key'

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # استخدم gpt-4-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# مسار الملف النصي
file_path = 'path/to/your/file.txt'

# قراءة محتوى الملف النصي
file_content = read_text_file(file_path)

# إرسال النص إلى النموذج
response = ask_gpt(file_content)

print("Response from GPT-4:")
print(response)

