from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages
from django.views.generic import TemplateView,ListView,DetailView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import userUpdateForm, profileUpdateForm, MatricUpdateForm
from lms.models import Course, Module

from .forms import userUpdateForm, profileUpdateForm
from django.contrib.auth import authenticate, login, logout




def UserRegistration(request):
    registered = False
    if request.method == 'POST':
        u_form = userUpdateForm(data=request.POST)
        profile_form = profileUpdateForm(data=request.POST)
        if u_form.is_valid() and profile_form.is_valid():
            password = u_form.cleaned_data['password']
            user = u_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            p_form = profile_form.save(commit=False)
            p_form.user = user
            p_form.save()
            registered = True
            return redirect(reverse('user:profile'))
            messages.success(request, 'Thanks for registering {}'.format(user.username))
        else:
            # user_form = UserCreationForm(data=request.GET)
            messages.error(request, u_form.errors)

            print(u_form.errors)
    else:
        u_form = userUpdateForm()
        profile_form = profileUpdateForm()
    context={'u_form':u_form,
            'profile_form':profile_form,
            }
    return render(request,'account/signup.html',context)    




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('user:profile'))
            else:
                form = AuthenticationForm(request.POST)
                return HttpResponse("Your account is inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given... They used email: {} and password: {}".format(username,password))
    else:
        return render(request, 'account/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))



@login_required
def Profile_Page(request):
    print(request.user.id)
    profile = get_object_or_404(Profile, id=request.user.id)
    context={'profile':profile, 'my_courses':my_courses, 'user':user}
    return render(request,'university/profile_page.html',context)



def get_user_profile(request):
    user_profile_qs = Profile.objects.filter(user=request.user)
    return user_profile_qs.first()

def get_user_courses(request):
    user_courses_qs = request.user.courses_joined.values()
    return user_courses_qs



def get_teachers_courses(request):
    teachers_courses_qs = request.user.courses_created.all()
    return teachers_courses_qs



@login_required
def myprofile(request):
    user_profile = get_user_profile(request)
    user_courses = get_user_courses(request)
    # teachers_courses = get_teachers_courses(request)
    teachers_courses= Course.objects.filter(owner=request.user)
    if request.method== 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        # profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully',
            extra_tags='alert alert-success  alert-dismissible fade show')
            return redirect('user:profile')
        else:
            messages.error(request, 'Error updating your profile', extra_tags='alert alert-error  alert-dismissible fade show')
            return redirect('user:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user) 

    context= {
        
        'user_profile':user_profile,
        'user_courses':user_courses,
        'teachers_courses':teachers_courses,
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile/profile.html',context)



def matric_edit_view(request):

    try:
        profile = request.user
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = Profile(request.POST, instance=profile)
        if m_form.is_valid():
            m_form.save()
            return redirect('account_login')
            messages.error(request, 'Error your matric number has to ba in the form 140211***')
        
        else:
            m_form = MatricUpdateForm(instance=request.user)
        context= {'m_form':m_form,}
        return render(request,'university/edit_matric.html',context)

# def matric_edit_view(request):

#     if request.method=='POST':
#         new_user = get_object_or_404(Profile, user=request.user)
#         m_form = MatricUpdateForm(request.POST)
#         print('initialized form')
#         if m_form.is_valid():
#             print('form is valid')
#             new_user = m_form.save(commit = False)
#             print('commited false')
#             # new_user = Profile(
#             #                 user = request.user,
#             #                 )
#             new_user.user = request.user #get_object_or_404(Profile, user=request.user)
#             print('appnden the user to the form')
#             new_user.save()
#             print('saved')
#             messages.success(request, 'matric number updated successfully ')
#         else:
#             messages.error(request, 'Error your matric number has to ba in the form 140211***')
#         return redirect('account_login')
#     else:
#         m_form = MatricUpdateForm(instance=request.user)
#     context= {'m_form':m_form,}
#     return render(request,'university/edit_matric.html',context)


# def matric_edit_view(request):

#     if request.method=='POST':
#         new_user = get_object_or_404(Profile, user=request.user)
#         m_form = MatricUpdateForm(request.POST)
#         print('initialized form')
#         if m_form.is_valid():
#             print('form is valid')
#             new_user = m_form.save(commit = False)
#             print('commited false')
#             # new_user = Profile(
#             #                 user = request.user,
#             #                 )
#             new_user.user = request.user #get_object_or_404(Profile, user=request.user)
#             print('appnden the user to the form')
#             new_user.save()
#             print('saved')
#             messages.success(request, 'matric number updated successfully ')
#         else:
#             messages.error(request, 'Error your matric number has to ba in the form 140211***')
#         return redirect('account_login')
#     else:
#         m_form = MatricUpdateForm(instance=request.user)
#     context= {'m_form':m_form,}
#     return render(request,'university/edit_matric.html',context)
    


###this is for a custom userform so that a blank profie can be created in other to avoid empty querying when checking a profile
# Profile.objects.create(user=new_user)
    