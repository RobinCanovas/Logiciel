import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary_and_quiz(text):
    prompt = f"""
    Tu es un assistant étudiant. Voici un texte de cours :
    {text}

    1) Fais un résumé clair et concis.
    2) Propose 3 questions de quiz basées sur ce texte.
    Format réponse : JSON avec "summary" et "quiz" (liste de questions).
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    result_text = response.choices[0].message.content
    return result_text

def generate_summary_and_quiz2(text):
    return {
        "summary": "Ceci est un résumé factice pour test.",
        "quiz": [
            "Question 1 ?", 
            "Question 2 ?", 
            "Question 3 ?"
        ]
    }