from django.contrib import admin
from app1.models import students
from app1.models import classroom
from app1.models import teacher
from app1.models import marks
# Register your models here.
admin.site.register(students)
admin.site.register(classroom)
admin.site.register(teacher)
admin.site.register(marks)
