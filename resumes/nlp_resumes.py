import spacy
import pdfminer.high_level
import docx

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return pdfminer.high_level.extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def extract_resume_info(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "EDUCATION"]]
    return {"skills": skills}
