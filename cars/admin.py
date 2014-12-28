from django.contrib import admin
from cars.models import Car, Question, UserProfile

class CarAdmin(admin.ModelAdmin):
    list_display = ("Modele", "Year", "ADay","AWeek","AMounth","Company","Phone","Location","Notes")
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("Username","Email", "Question",)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("Username" ,"Surname","Password","Date_of_Birth", "Email", "Address", "Post_Code")

admin.site.register(Car, CarAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)