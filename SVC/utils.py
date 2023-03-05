from .models import Student, Participant
import uuid

def gen_recruiting_id(vc_id: int):
    vc = Student.objects.get(id=vc_id)
    unq_id = uuid.uuid4().hex
    vc.recruiting_id = unq_id
    vc.save()

def total_recruitments(recruiter: object):
    return recruiter.student_set.all().count()


    
