from django.shortcuts import render, get_object_or_404, redirect


from .forms import ContactForms

from django.core.mail import send_mail

# Create your views here.

from django.core.paginator import Paginator

from .models import Article, ContactForm

def articles_list(request):
    # Récupérer tous les articles
    articles = Article.objects.all()

    # Filtrer les articles par terme de recherche s'il y en a un
    search_query = request.GET.get('q')
    if search_query:
        articles = articles.filter(nom__icontains=search_query)

    # Pagination
    paginator = Paginator(articles, 6)  # 6 articles par page

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'auto/articles_list.html', {'page_obj': page_obj, 'search_query': search_query})



def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'auto/article_detail.html', {'article': article})



def search_articles(request):

    search_query = request.GET.get('q')

    articles = Article.objects.filter(nom__icontains=search_query) if search_query else []
    return render(request, 'auto/search_results.html', {'articles': articles, 'search_query': search_query})




# contact form


def contact_view(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForms()
    return render(request, 'auto/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'auto/contact_success.html')