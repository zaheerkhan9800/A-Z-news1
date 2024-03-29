from notifications.models import Notification
from django.shortcuts import render, redirect, reverse, get_object_or_404


# Message notification page
def my_notifications(request):
    context = {}
    return render(request, 'notice/my_notifications.html', context)


# Unread to read, jump to the message adding page
def my_notification(request, my_notifications_pk):
    my_notification = get_object_or_404(Notification, pk=my_notifications_pk)
    my_notification.unread = False
    my_notification.save()
    return redirect(my_notification.data['url'])


# Delete all read
def delete_my_read_notifications(request):
    notifications = request.user.notifications.read()
    notifications.delete()
    return redirect(reverse('notice:my_notifications'))
