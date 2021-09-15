from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from core.models import Tweet, Hashtag, Like

# Create your views here.


def splash(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request, "splash.html", {})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
    return render(request, "login.html", {})


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'])
        auth_login(request, user)
        return redirect("/")
    return render(request, "signup.html", {})


def logout(request):
    auth_logout(request)
    return redirect("/login")


def home(request):
    if request.method == "POST":
        note = request.POST["note"]
        post = Tweet.objects.create(note=note, author=request.user)

        tagged = post.split_post()
        for word in tagged:
            if word[0] == "#":
                ht, created = Hashtag.objects.get_or_create(tag=word[1:])
                ht.save()
                ht.posts.add(post)
                ht.save()
            if tagged[word]:
                word1 = word[1:]
                note = note.replace(word, '<a href="/hashtag/'
                                    + word1 + '/">' + '#' + word1 + '</a>')
                post.set_note(note)
                post.save()
        post.set_note(note)
        post.save()

    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "home.html", {"tweets": tweets})


def my_profile(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    tweets = Tweet.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "profile.html", {"tweets": tweets})


def del_post(request):
    if request.method == "POST":
        post_id = request.POST["tweet_id"]
        tweet = Tweet.objects.get(id=post_id)
        tweet.delete()
    return redirect("/profile")


def user_profs(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        author_name = request.POST['author_name']
        current = str(request.user)
        if author_name == current:
            return redirect("/profile")
        poster = User.objects.get(username=author_name).id
        tweets = Tweet.objects.filter(author=poster).order_by('-created_at')
    return render(request, "user_profs.html", {"tweets": tweets,
                                               "author_name": author_name})


def hashtag(request, hashtag):
    if not request.user.is_authenticated:
        return redirect('/login')
    ht = Hashtag.objects.filter(tag=hashtag)
    for item in ht:
        print(item.posts.all())
    tweets = ht[0].posts.all().order_by('-created_at')
    return render(request, "hashtag.html", {"tweets": tweets})


def like_post(request):
    if request.method == "POST":
        post_id = request.POST["tweet_id"]
        print("POST ID IS: ")
        print(post_id)
        tweet = Tweet.objects.get(id=post_id)
        newlike, created = Like.objects.get_or_create(user=request.user,
                                                      post=tweet)
        newlike.save()
        if not created:
            newlike.delete()
    return redirect("/home/")
