from django.shortcuts import render
from django.views import generic
from . import models,forms
from django.conf import settings
from django.core.mail import send_mail
import datetime,pytz

# Create your views here.

def get_today_day():
    tz = pytz.timezone('Asia/Kathmandu')
    days = ["mo", "tu", "we", "th", "fr", "sa","su"]
    num_day = datetime.datetime.now(tz).weekday()
    return days[num_day]

def get_current_time():
    tz = pytz.timezone('Asia/Kathmandu')
    return datetime.datetime.now(tz).strftime("%H:%M")

today = get_today_day()
current_time = get_current_time()

class HomePageView(generic.TemplateView):
    template_name = 'fm_app/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['slides'] = models.SlideModel.objects.all()[1:]
        context['one_slide'] = models.SlideModel.objects.all()[:1]
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['topfournews'] = models.NewsModel.objects.filter(topNews = True).order_by('-published_date')[:4]
        context['local_news'] = models.NewsModel.objects\
                                .filter(newstype__iexact = 'LOCAL')\
                                .order_by('published_date')[:5]
        context['national_news'] = models.NewsModel.objects\
                                    .filter(newstype__iexact = 'NATIONAL')\
                                    .order_by('published_date')[:5]
        context['international_news'] = models.NewsModel.objects\
                                    .filter(newstype__iexact = 'INTERNATIONAL')\
                                    .order_by('published_date')[:5]
        context['sports_news'] = models.NewsModel.objects\
                                    .filter(newstype__iexact = 'SPORTS')\
                                    .order_by('published_date')[:5]
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'fm_app/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutPageView, self).get_context_data(*args, **kwargs)
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context

class ContactFormView(generic.FormView):
    template_name = 'fm_app/contact.html'
    form_class = forms.ContactForm
    success_url = '/fm_app/thanks'

    def form_valid(self, form):
        message="{name}/{email} from {addr} said:".format(
        name=form.cleaned_data.get('name'),
        email=form.cleaned_data.get('email'),
        addr=form.cleaned_data.get('address')
        )
        message+="\n\n{0}".format(form.cleaned_data.get('text'))
        send_mail(
            subject="About Website",
            message = message,
            from_email='contact-form@fm_app.com',
            recipient_list = [settings.LIST_OF_EMAIL_RECIPIENTS]
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context

class NewsListView(generic.ListView):
    model = models.NewsModel
    def get_queryset(self):
        return models.NewsModel.objects.order_by('published_date')

    def get_context_data(self, *args, **kwargs):
        context = super(NewsListView, self).get_context_data(*args, **kwargs)
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context

class OneCategoryView(generic.TemplateView):
    model = models.NewsModel
    template_name = 'fm_app/one_category_news.html'

    def get_context_data(self, **kwargs):
        context= super(OneCategoryView, self).get_context_data(**kwargs)
        context['all_news'] = models.NewsModel.objects\
                                .filter(newstype__iexact = (self.kwargs.get('newstype')).upper())\
                                .order_by('published_date')
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context


class NewsDetailView(generic.DetailView):
    context_object_name = 'news_details'
    model = models.NewsModel

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['nowplaying'] = models.Schedule.objects\
                                    .filter(day__name_of_day = today,
                                            end_time__gt = current_time)\
                                    .order_by('start_time')[:2]
        return context

class Thanks(generic.TemplateView):
    template_name = 'fm_app/thanks.html'

class ProgramSchedule(generic.TemplateView):
    template_name = 'fm_app/program_schedule.html'
    model = models.Schedule

    def get_context_data(self, *args, **kwargs):
        context = super(ProgramSchedule, self).get_context_data(*args, **kwargs)
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['sunday'] = models.Schedule.objects.filter(day__name_of_day = 'su').order_by('start_time')
        context['monday'] = models.Schedule.objects.filter(day__name_of_day = 'mo').order_by('start_time')
        context['tuesday'] = models.Schedule.objects.filter(day__name_of_day = 'tu').order_by('start_time')
        context['wednesday'] = models.Schedule.objects.filter(day__name_of_day = 'we').order_by('start_time')
        context['thursday'] = models.Schedule.objects.filter(day__name_of_day = 'th').order_by('start_time')
        context['friday'] = models.Schedule.objects.filter(day__name_of_day = 'fr').order_by('start_time')
        context['saturday'] = models.Schedule.objects.filter(day__name_of_day = 'sa').order_by('start_time')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context


class ProfileView(generic.TemplateView):
    context_object_name = 'schedule'
    template_name = 'fm_app/profiles.html'
    model = models.PhotoProfile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['pp'] = models.PhotoProfile.objects.all()
        context['recent_news'] = models.NewsModel.objects.filter(flashNews = True).order_by('published_date')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context

class GalleryView(generic.TemplateView):
    template_name = 'fm_app/gallery.html'
    context_object_name = 'gallery'

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryView, self).get_context_data(*args, **kwargs)
        context['gallery_photos'] = models.PhotosModel.objects.all().order_by('uploaded_date')
        context['gallery_videos'] = models.VideosModel.objects.all().order_by('uploaded_date')
        context['nowplaying'] = models.Schedule.objects\
                                .filter(day__name_of_day = today,
                                        end_time__gt = current_time)\
                                .order_by('start_time')[:2]
        return context
