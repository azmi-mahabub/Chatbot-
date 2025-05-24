from django.shortcuts import render
from .models import *
from .forms import QueryForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def home(request):
    results = []
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            pieces = Piece.objects.all()
            corpus = [f"{p.reference} {p.designation} {p.volume} {p.material} {p.type} {p.family} {p.group} {p.keywords}" for p in pieces]
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform(corpus + [query])
            similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
            sorted_indices = np.argsort(similarity)[::-1][:5]
            for idx in sorted_indices:
                part = pieces[int(idx)]
                match = round(similarity[idx] * 100, 2)
                results.append({
                    'reference': part.reference,
                    'designation': part.designation,
                    'image': part.image.url if part.image and hasattr(part.image, 'url') else '',
                    'match': match,
                })
    else:
        form = QueryForm()
    return render(request, 'chatbotFolder/home.html', {'form': form, 'results': results})

