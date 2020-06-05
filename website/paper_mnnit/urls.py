from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from paper_mnnit import views
from django.conf.urls import include

app_name = 'paper_mnnit'

urlpatterns = [
    url (r'^computer/$', views.computer, name='computer'),
    url (r'^comp_lab_assignments/$', views.comp_lab_assignments, name='comp_lab_assignments'),
    url (r'^comp_books/$', views.comp_books, name='comp_books'),
    url (r'^comp_papers/$', views.comp_papers, name='comp_papers'),
    url (r'^comp_notes/$', views.comp_notes, name='comp_notes'),

    url (r'^mathsI/$', views.mathsI, name='mathsI'),
    url (r'^mathsI_books/$', views.mathsI_books, name='mathsI_books'),
    url (r'^mathsI_papers/$', views.mathsI_papers, name='mathsI_papers'),
    url (r'^mathsI_notes/$', views.mathsI_notes, name='mathsI_notes'),
    url (r'^mathsI_tutsheets/$', views.mathsI_tutsheets, name='mathsI_tutsheets'),

    url (r'^mathsII/$', views.mathsII, name='mathsII'),
    url (r'^mathsII_books/$', views.mathsII_books, name='mathsII_books'),
    url (r'^mathsII_papers/$', views.mathsII_papers, name='mathsII_papers'),
    url (r'^mathsII_notes/$', views.mathsII_notes, name='mathsII_notes'),
    url (r'^mathsII_tutsheets/$', views.mathsII_tutsheets, name='mathsII_tutsheets'),

    url (r'^physicsI/$', views.physicsI, name='physicsI'),
    url (r'^physicsI_books/$', views.physicsI_books, name='physicsI_books'),
    url (r'^physicsI_papers/$', views.physicsI_papers, name='physicsI_papers'),
    url (r'^physicsI_notes/$', views.physicsI_notes, name='physicsI_notes'),
    url (r'^physicsI_tutsheets/$', views.physicsI_tutsheets, name='physicsI_tutsheets'),

    url (r'^physicsII/$', views.physicsII, name='physicsII'),
    url (r'^physicsII_books/$', views.physicsII_books, name='physicsII_books'),
    url (r'^physicsII_papers/$', views.physicsII_papers, name='physicsII_papers'),
    url (r'^physicsII_notes/$', views.physicsII_notes, name='physicsII_notes'),
    url (r'^physicsII_tutsheets/$', views.physicsII_tutsheets, name='physicsII_tutsheets'),

    url (r'^chem/$', views.chem, name='chem'),
    url (r'^chem_books/$', views.chem_books, name='chem_books'),
    url (r'^chem_papers/$', views.chem_papers, name='chem_papers'),
    url (r'^chem_notes/$', views.chem_notes, name='chem_notes'),
    url (r'^chem_tutsheets/$', views.chem_tutsheets, name='chem_tutsheets'),

    url (r'^workshop/$', views.wk, name='wk'),
    url (r'^workshop_books/$', views.wk_books, name='wk_books'),
    url (r'^workshop_papers/$', views.wk_papers, name='wk_papers'),
    url (r'^workshop_notes/$', views.wk_notes, name='wk_notes'),
    url (r'^workshop_lab/$', views.wk_lab, name='wk_lab'),

    url (r'^ed/$', views.ed, name='ed'),
    url (r'^ed_books/$', views.ed_books, name='ed_books'),
    url (r'^ed_papers/$', views.ed_papers, name='ed_papers'),
    url (r'^ed_notes/$', views.ed_notes, name='ed_notes'),

    url (r'^ecology/$', views.eco, name='eco'),
    url (r'^ecology_papers/$', views.eco_papers, name='eco_papers'),
    url (r'^ecology_notes/$', views.eco_notes, name='eco_notes'),
    url (r'^ecology_pdfs/$', views.eco_pdfs, name='eco_pdfs'),
    url (r'^ecology_assignments/$', views.eco_assignments, name='eco_assignments'),

    url (r'^csw/$', views.csw, name='csw'),
    url (r'^csw_papers/$', views.csw_papers, name='csw_papers'),
    url (r'^csw_notes/$', views.csw_notes, name='csw_notes'),

    url (r'^mechanics/$', views.mechanics, name='mechanics'),
    url (r'^mechanics_books/$', views.mechanics_books, name='mechanics_books'),
    url (r'^mechanics_papers/$', views.mechanics_papers, name='mechanics_papers'),
    url (r'^mechanics_notes/$', views.mechanics_notes, name='mechanics_notes'),
    url (r'^mechanics_tutsheets/$', views.mechanics_tutsheets, name='mechanics_tutsheets'),

    url (r'^emglish/$', views.eng, name='eng'),
    url (r'^english_literature/$', views.eng_literature, name='eng_literature'),
    url (r'^english_papers/$', views.eng_papers, name='eng_papers'),
    url (r'^english_language/$', views.eng_language, name='eng_language'),
]
