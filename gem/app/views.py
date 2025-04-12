from django.shortcuts import render
from .response import *
import markdown

# Create your views here.


def IndexView(request):
    if request.method == "POST":
        ques = request.POST.get("ques")
        ans = generate_content(ques)
        html_ans = markdown.markdown(ans)
        dct = {"ques": ques, "ans": html_ans}
        return render(request, "app/index.html", {"ques_lst": dct})
    return render(request, "app/index.html", {})
