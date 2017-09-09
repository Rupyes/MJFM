from django.contrib import admin
from .models import (NewsModel,
                    SlideModel, PhotoProfile,
                    PhotosModel,Day, Schedule,
                    VideosModel)

# Register your models here.


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'newstype', 'published_date')

admin.site.register(NewsModel, NewsModelAdmin)
admin.site.register(SlideModel)
admin.site.register(PhotosModel)
admin.site.register(VideosModel)

@admin.register(PhotoProfile)
class PhotoProfileAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title','day','host','start_time','end_time')

admin.site.register(Schedule, ScheduleAdmin)

class ScheduleInline(admin.TabularInline):
    model = Schedule

class DayAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    list_display = ('get_name_of_day_display', 'created_time')

admin.site.register(Day, DayAdmin)
# admin.site.register(Schedule)
#admin.site.register(Day)
