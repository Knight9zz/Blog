from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.urls import reverse
from django.views import View
# Create your views here.

def index(request):

    obj = Student.get_all()

    if request.method == 'POST':
        # 创建一个form实例
        form = StudentForm(request.POST)

        # 因为指定了StudentForm的Model 所以可以直接调用save
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        myform = StudentForm()
        context = {
            'student':obj,
            'form':myform,
        }
        return render(request, 'student_app/index.html', context=context)

## class based view 模式
## ps：此处未做数据检查
## 写成这样的形式可以定义该url只能通过get或者post的方式访问

class IndexView(View):

    template_name = 'index.html'

    def get_content(self):
        student = Student.get_all()
        content = {
            'student':student,
        }
        return content


    def get(self, request):
        form = StudentForm()
        content = self.get_content()
        content.update({
            'form':form
        })
        return render(request, self.template_name, content)

    def post(self, request):
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

        return HttpResponse('ok 200')

