from django.contrib import admin
from .models import studentInfo,Alumni
from .models import graduateForm
from .models import Event
from .models import JobFair
from .models import Yearbook

class studentInfoAdmin(admin.ModelAdmin):
    list_display = ('studID', 'lastname',)

class graduateFormAdmin(admin.ModelAdmin):
    list_display = ('get_alumniID', 'dategraduated', 'firstname', 'lastname', 'alumniaddress')

    def get_alumniID(self, obj):
        return obj.alumniID.alumniID
    get_alumniID.short_description = 'Alumni ID'


class AlumniAdmin(admin.ModelAdmin):
    list_display = ('alumniID', 'student_id', 'firstname','lastname','degree','alumniaddress')

    def get_firstname(self, obj):
        return obj.student.fname
    get_firstname.short_description = 'First Name'

    def get_lastname(self, obj):
        return obj.student.lname
    get_lastname.short_description = 'Last Name'

    
class EventAdmin(admin.ModelAdmin):
    list_display = ('eventID', 'eventsName', 'eventsDate', 'eventsLocation')
    
class JobFairAdmin(admin.ModelAdmin):
    list_display = ('jobfair_id', 'jobtitle','companyname', 'joblocation','employmenttype','jobsalary')
class YearbookAdmin(admin.ModelAdmin):
    list_display = ('yearbookID','yearbookFirstname', 'yearbookLastname', 'yearbookGender', 'yearbookAddress', 'yearbookCourse' ,'yearbookYearGrad')

admin.site.register(Yearbook, YearbookAdmin)
admin.site.register(JobFair, JobFairAdmin)
admin.site.register(Event, EventAdmin)   
admin.site.register(graduateForm, graduateFormAdmin)
admin.site.register(studentInfo, studentInfoAdmin)
admin.site.register(Alumni, AlumniAdmin)