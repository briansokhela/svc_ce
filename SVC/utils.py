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
    f_hours = [0, 0, 0]
    sl_hours = 0
    oo_hours = 0
    cbr_hours = 0

    for champ in champions:
        if champ.vc.faculty == faculty:
                print(sl_hours)
                print(champ.project)
                if champ.project.project_type == 'Service Learning':
                    sl_hours += champ.project.expected_duration
                    print(sl_hours)
                if champ.project.project_type == 'Organised Outreach':
                    oo_hours += champ.project.expected_duration
                if champ.project.project_type == 'Community-Based Research':
                    cbr_hours += champ.project.expected_duration
    f_hours = [sl_hours, oo_hours, cbr_hours]
    return  f_hours
           


            
    


