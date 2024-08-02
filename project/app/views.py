from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def book(request):  
    books = Book.objects.all()  
    return render(request,"book.html",{'books':books})  

def create(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('book')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'create.html',{'form':form})  

def update(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('book')  
            except Exception as e: 
                pass    
    return render(request,'update.html',{'form':form})  

# def delete(request, id):
#     book = Book.objects.get(id=id)
#     try:
#         book.delete()
#     except:
#         pass
#     return redirect('book')

def delete(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        try:
            book.delete()
            return redirect('book')
        except Exception as e:
            # Handle error if needed
            pass
    return render(request, 'delete.html', {'book': book})
