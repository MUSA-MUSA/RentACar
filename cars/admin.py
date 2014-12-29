from django.contrib import admin
from cars.models import Car, Question, UserProfile

class CarAdmin(admin.ModelAdmin):
    list_display = ("Modele", "Year", "ADay","AWeek","AMounth","Company","Phone","Location","Notes")
admin.site.register(Car, CarAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("Username","Email", "Question",)
admin.site.register(Question, QuestionAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("Username" ,"Surname","Password","Date_of_Birth", "Email", "Address", "Post_Code")
admin.site.register(UserProfile, UserProfileAdmin)

