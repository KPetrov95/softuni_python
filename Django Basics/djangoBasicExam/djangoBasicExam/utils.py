from djangoBasicExam.authors.models import Author


def get_author():
    return Author.objects.first()