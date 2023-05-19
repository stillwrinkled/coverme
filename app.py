import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = "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"  # Replace with your OpenAI API key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        employer = request.form.get("employer")
        role = request.form.get("role")
        cover_letter_paras = request.form.get("coverLetterParas")
        jd = request.form.get("jd")
        desc1 = request.form.get("desc1")
        desc2 = request.form.get("desc2")
        desc3 = request.form.get("desc3")
        desc4 = request.form.get("desc4")
        cv = request.form.get("cv")

        # Construct the input prompt for the ChatGPT API
        prompt = f"Employer: {employer}\nRole: {role}\nCover Letter Paragraphs: {cover_letter_paras}\nJob Description: {jd}\nDescription 1: {desc1}\nDescription 2: {desc2}\nDescription 3: {desc3}\nDescription 4: {desc4}\nCV:\n{cv}\n"

        # Call the ChatGPT API to generate the cover letter
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,  # Adjust the max tokens as needed
            temperature=0.7,  # Adjust the temperature as needed
            n=1,
            stop=None,
            echo=False
        )

        # Extract the generated cover letter from the API response
        cover_letter = response.choices[0].text.strip()

        return render_template("index.html", output=cover_letter)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
