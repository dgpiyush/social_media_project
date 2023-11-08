
from django.shortcuts import render, get_object_or_404, redirect
from .models import Like, Message, Comment
from .forms import MessageForm, CommentForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('message_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def comment_list(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    comments = Comment.objects.filter(message=message)
    return render(request, 'comment_list.html', {'message': message, 'comments': comments})



@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Assign the currently logged-in user
            message.save()
            return redirect('message_list')  # Redirect to the message list page
    else:
        form = MessageForm()
    return render(request, 'create_message.html', {'form': form})

@login_required
def create_comment(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.message = message
            comment.save()
            return redirect('comment_list', message_id=message_id)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form, 'message': message})



@login_required
def update_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.user == message.user:
        if request.method == 'POST':
            form = MessageForm(request.POST, instance=message)
            if form.is_valid():
                form.save()
                return redirect('message_list')
        else:
            form = MessageForm(instance=message)
        return render(request, 'update_message.html', {'form': form, 'message': message})
    else:
        return redirect('message_list')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.user == message.user:
        message.delete()
    return redirect('message_list')



@login_required
def like_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, liked_message=message)
    if not created:
        like.delete()
    return redirect('message_list')

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, liked_comment=comment)
    if not created:
        like.delete()
    return redirect('comment_list', message_id=comment.message.id)