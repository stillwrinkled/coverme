# app.py

from flask import Flask, request, render_template
import openai

openai.api_key = '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'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        employer = request.form.get('employer')
        role = request.form.get('role')
        coverLetterParas = request.form.get('coverLetterParas')
        jd = request.form.get('jd')
        cv = request.form.get('cv')
        desc1 = request.form.get('desc1')
        desc2 = request.form.get('desc2')
        desc3 = request.form.get('desc3')
        desc4 = request.form.get('desc4')
        desc5 = request.form.get('desc5')

        # Construct the message to send to ChatGPT API
        message = f"I am applying for the role of {role} at {employer}. Here are some details about me: {desc1}, {desc2}, {desc3}, {desc4}, {desc5}. The job description is as follows: {jd}. My CV is as follows: {cv}. Please generate a cover letter with {coverLetterParas} paragraphs."

        response = openai.Completion.create(
          engine="davinci-codex",
          prompt=message,
          temperature=0.5,
          max_tokens=1000
        )

        output = response.choices[0].text.strip()

        return render_template('index.html', output=output)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
