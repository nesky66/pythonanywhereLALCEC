
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.post.models import Post,Categoria
from .forms import PostForm, FormCategoria


# Create your views here.

def post(request):
    
    parametro_categoria = request.GET.get("categoria")
    
    post = Post.objects.filter(activo=True)
    cat = {}
    if post :
        for x in post:
            cat[x.categoria_id] = x.categoria
        if not parametro_categoria:
            context = {'blog':post, 'cat':cat}
        else:
            cate = Categoria.objects.get(id=parametro_categoria)
            post = Post.objects.filter(activo=True,categoria_id=parametro_categoria)
            context = {'blog':post,'categ':cate.categoria,'cat':cat}
    
    else:
        context = {'vacio':'No hay posts disponibes'}
        
    return render(request,'post_blog.html', context)
    

def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_new(request):
    post = {'form':PostForm(initial={'usuario':request.user})}
    if request.method == 'POST':
        formulario = PostForm(request.POST,request.FILES)
      
        # formulario = PostForm(data = request.POST)
        # form = PostForm(request.POST) 
        if formulario.is_valid():
            # post = form.save(commit=False)
            # form.usuario = request.user
           
            # post.save()
            # return redirect('post_detail', pk=post.pk)
            formulario.save()
            post['mensaje']='Post guardado'
        else:
            post['form']=formulario
    # else:
    #     form = PostForm()
    #  return render(request, 'post_edit.html', {'form' : post})
    post['titulo']='Posteo Nuevo'
    return render(request, 'post_edit.html',post)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post) 
        if form.is_valid():
            post = form.save(commit=False)
     
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('vista_post')
    else:
        form = PostForm(instance=post)
    post = {'titulo':'Editar Posteo'}
    post['form']=form
    return render(request, 'post_edit.html', post)

@login_required
def post_delete(request, pk):
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('vista_post')
   
  

@login_required
def admincategorias(request):
    data = {'form': FormCategoria()}
   
    if request.method=="GET":
        
        if  request.GET :
            id_cat=request.GET.get('lista')
            cat = Categoria.objects.get(id=id_cat)
            cat.delete()
            data['mensaje2']='CATEGORIA ELIMINADA CON EXITO'
            data['mensaje1']='' 
        else:
            data['mensaje1']=""
            data['mensaje2']=""
       
    c = obtieneCategorias()
 
    if request.method == 'POST':
        formulario = FormCategoria(data=request.POST)
        if formulario.is_valid():
            valido = True
            for k,v in c.items(): 
                if request.POST['categoria'].upper() == v.upper():        
                    valido = False
            if valido:
                formulario.save()
                data['mensaje1']='CATEGORIA GUARDADA'
                c = obtieneCategorias()      
            else:
                data['mensaje1']='CATEGORIA EXISTENTE'
            data['mensaje2']='' 
        else:
            data['form']= formulario
            
    data['cat']=  c    
    return render(request,'adminCategoria.html',data)
        
@login_required      
def vistasPost(request):
    if request.user.is_superuser:
        blogs = Post.objects.filter()
    else:
        blogs = Post.objects.filter(usuario=request.user)
    
    return render(request,'post_vista.html',{'post':blogs})
    





def obtieneCategorias():
    categoria = Categoria.objects.all().order_by('categoria')
    categ = {}
    for x in categoria:
            categ[x.id] = x.categoria
    return categ

