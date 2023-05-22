import os
import openai
from flask import Flask, render_template, request
import pyperclip

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


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

        # Modify the generated cover letter based on the feedback
        cover_letter = cover_letter.replace("Paragraph 1", "")
        cover_letter = cover_letter.replace("Paragraph 2", "")
        cover_letter = cover_letter.replace("Dear Hiring Manager,", "Dear recruiter,\nFirst of all a big thank you!")
        cover_letter = cover_letter.replace("Dear Hiring Manager ,", "Dear recruiter,\nFirst of all a big thank you!")
        cover_letter = cover_letter.replace("Dear Hiring Manager,", "Dear recruiter,\nFirst of all a big thank you!")
        cover_letter = cover_letter.replace("Dear Hiring Manager ,", "Dear recruiter,\nFirst of all a big thank you!")

        # Extract the subject from the cover letter
        subject = ""
        if "Subj:" in cover_letter:
            subject_start_index = cover_letter.find("Subj:") + len("Subj:")
            subject_end_index = cover_letter.find("\n", subject_start_index)
            subject = cover_letter[subject_start_index:subject_end_index].strip()

        # Copy the cover letter to the clipboard
        pyperclip.copy(cover_letter)

        return render_template("index.html", output=cover_letter, subject=subject)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
