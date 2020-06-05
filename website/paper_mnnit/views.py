from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'paper_mnnit/index.html')


# computer
def computer(request):
    return render(request,'paper_mnnit/computer/computer.html')
def comp_books(request):
    return render(request,'paper_mnnit/computer/comp_books.html')
def comp_lab_assignments(request):
    return render(request,'paper_mnnit/computer/comp_lab_assignments.html')
def comp_papers(request):
    return render(request,'paper_mnnit/computer/comp_papers.html')
def comp_notes(request):
    return render(request,'paper_mnnit/computer/comp_notes.html')


#mathsI
def mathsI(request):
    return render(request,'paper_mnnit/mathsI/mathsI.html')
def mathsI_notes(request):
    return render(request,'paper_mnnit/mathsI/mathsI_notes.html')
def mathsI_books(request):
    return render(request,'paper_mnnit/mathsI/mathsI_books.html')
def mathsI_tutsheets(request):
    return render(request,'paper_mnnit/mathsI/mathsI_tutsheets.html')
def mathsI_papers(request):
    return render(request,'paper_mnnit/mathsI/mathsI_papers.html')

#mathsII
def mathsII(request):
    return render(request,'paper_mnnit/mathsII/mathsII.html')
def mathsII_notes(request):
    return render(request,'paper_mnnit/mathsII/mathsII_notes.html')
def mathsII_books(request):
    return render(request,'paper_mnnit/mathsII/mathsII_books.html')
def mathsII_tutsheets(request):
    return render(request,'paper_mnnit/mathsII/mathsII_tutsheets.html')
def mathsII_papers(request):
    return render(request,'paper_mnnit/mathsII/mathsII_papers.html')

#physicsI
def physicsI(request):
    return render(request,'paper_mnnit/physicsI/physicsI.html')
def physicsI_notes(request):
    return render(request,'paper_mnnit/physicsI/physicsI_notes.html')
def physicsI_books(request):
    return render(request,'paper_mnnit/physicsI/physicsI_books.html')
def physicsI_tutsheets(request):
    return render(request,'paper_mnnit/physicsI/physicsI_tutsheets.html')
def physicsI_papers(request):
    return render(request,'paper_mnnit/physicsI/physicsI_papers.html')

#physicsII
def physicsII(request):
    return render(request,'paper_mnnit/physicsII/physicsII.html')
def physicsII_notes(request):
    return render(request,'paper_mnnit/physicsII/physicsII_notes.html')
def physicsII_books(request):
    return render(request,'paper_mnnit/physicsII/physicsII_books.html')
def physicsII_tutsheets(request):
    return render(request,'paper_mnnit/physicsII/physicsII_tutsheets.html')
def physicsII_papers(request):
    return render(request,'paper_mnnit/physicsII/physicsII_papers.html')

#chemistry
def chem(request):
    return render(request,'paper_mnnit/chem/chem.html')
def chem_notes(request):
    return render(request,'paper_mnnit/chem/chem_notes.html')
def chem_books(request):
    return render(request,'paper_mnnit/chem/chem_books.html')
def chem_tutsheets(request):
    return render(request,'paper_mnnit/chem/chem_tutsheets.html')
def chem_papers(request):
    return render(request,'paper_mnnit/chem/chem_papers.html')

# workshop

def wk(request):
    return render(request,'paper_mnnit/workshop/wk.html')
def wk_books(request):
    return render(request,'paper_mnnit/workshop/wk_books.html')
def wk_lab(request):
    return render(request,'paper_mnnit/workshop/wk_lab.html')
def wk_papers(request):
    return render(request,'paper_mnnit/workshop/wk_papers.html')
def wk_notes(request):
    return render(request,'paper_mnnit/workshop/wk_notes.html')

# ed
def ed(request):
    return render(request,'paper_mnnit/ed/ed.html')
def ed_books(request):
    return render(request,'paper_mnnit/ed/ed_books.html')
def ed_papers(request):
    return render(request,'paper_mnnit/ed/ed_papers.html')
def ed_notes(request):
    return render(request,'paper_mnnit/ed/ed_notes.html')

#mechanics
def mechanics(request):
    return render(request,'paper_mnnit/mechanics/mechanics.html')
def mechanics_notes(request):
    return render(request,'paper_mnnit/mechanics/mechanics_notes.html')
def mechanics_books(request):
    return render(request,'paper_mnnit/mechanics/mechanics_books.html')
def mechanics_tutsheets(request):
    return render(request,'paper_mnnit/mechanics/mechanics_tutsheets.html')
def mechanics_papers(request):
    return render(request,'paper_mnnit/mechanics/mechanics_papers.html')

# csw
def csw(request):
    return render(request,'paper_mnnit/csw/csw.html')
def csw_papers(request):
    return render(request,'paper_mnnit/csw/csw_papers.html')
def csw_notes(request):
    return render(request,'paper_mnnit/csw/csw_notes.html')

# eco
def eco(request):
    return render(request,'paper_mnnit/eco/eco.html')
def eco_papers(request):
    return render(request,'paper_mnnit/eco/eco_papers.html')
def eco_notes(request):
    return render(request,'paper_mnnit/eco/eco_notes.html')
def eco_pdfs(request):
    return render(request,'paper_mnnit/eco/eco_pdfs.html')
def eco_assignments(request):
    return render(request,'paper_mnnit/eco/eco_assignments.html')    

# eng
def eng(request):
    return render(request,'paper_mnnit/eng/eng.html')
def eng_literature(request):
    return render(request,'paper_mnnit/eng/eng_literature.html')
def eng_papers(request):
    return render(request,'paper_mnnit/eng/eng_papers.html')
def eng_language(request):
    return render(request,'paper_mnnit/eng/eng_language.html')
