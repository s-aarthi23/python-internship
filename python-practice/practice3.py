marks = {
    "Maths":85,
    "Python":92,
    "DAA":78,
    "OS":88
}
def get_top_subjects(marks):
    for subject,mark in marks.items():
        if mark > 80:
            print("Subject:",subject, "Mark:",mark)        
get_top_subjects(marks)            