from .models import Student, Participant
import uuid

def gen_recruiting_id(vc_id: int):
    vc = Student.objects.get(id=vc_id)
    unq_id = uuid.uuid4().hex
    vc.recruiting_id = unq_id
    vc.save()

def total_recruitments(recruiter: object):
    return recruiter.student_set.all().count()


def get_hours(faculty: str, champions):
    sl_hours = 0
    oo_hours = 0
    cbr_hours = 0

    for champ in champions:
        if champ.vc.faculty == faculty:
            if champ.occurrence.project.project_type == 'Service Learning':
                sl_hours += champ.occurrence.expected_duration
            if champ.occurrence.project.project_type == 'Organised Outreach':
                oo_hours += champ.occurrence.expected_duration
            if champ.occurrence.project.project_type == 'Community-Based Research':
                cbr_hours += champ.occurrence.expected_duration
    f_hours = [sl_hours, oo_hours, cbr_hours]
    return  f_hours
           


            
    


