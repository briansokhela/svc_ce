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
    for vc in champions:
        for pr in vc.participant_set.all():

            
    


