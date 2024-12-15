from django.http import *
from django.shortcuts import *
from app.models import *

def simple(request):
    return redirect('/file_upload')

def stream(request):
    response_content=("Это", "функция", "передает", "все", "частями")
    response = StreamingHttpResponse(response_content, content_type="text/plain; charset=utf-8")
    return response

def file_upload(request):
    file_name = r'/Users/azizali/Desktop/Python/Django/Lesson-10/static/tyan.jpeg'
    return FileResponse(open(file_name, 'rb'), as_attachment=True)

def get_object(request, id):
    b = get_object_or_404(Crypto, id=id)
    return HttpResponse(b.name)

def get_list(request, school_id):
    bbs = get_list_or_404(Student, school=school_id)
    return HttpResponse(bbs)

def fet_pdf(request):
    file_name = r''

def create_comment(request):
    if request.method == 'POST':
        content = request.POST['content']
        author = request.POST['author']
        Comment.objects.create(content=content, author=author)
        return redirect('/create_comment')
    else:
        return HttpResponse(render(request, 'comment.html'))

def get_comment(request):
    if request.method == 'POST':
        return redirect(f'/view_comment/{request.POST['id']}')
    return HttpResponse(render(request, 'get_comment.html'))

def view_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    context = {'comment': comment}
    return HttpResponse(render(request, 'view_comment.html', context))
