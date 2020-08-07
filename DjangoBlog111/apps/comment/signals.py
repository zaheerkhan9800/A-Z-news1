from django.db.models.signals import post_save
from notifications.signals import notify
from django.utils.html import strip_tags
from .models import Comment
from django.dispatch import receiver

# @receiver(post_save,sender=Comment)
# def send_notification(sender,instance,**kwargs):
#     # Send notification
#     # Determine if the comment is a blog or
#     if instance.reply_to is None:
#         # 接受者是文章
#         recipient = instance.content_object.get_user()
#         if instance.content_type.model == 'post':
#             blog = instance.content_object
#             verb = '{0} Commented on your article：《{1}》'.format(instance.user, blog.title)
#         else:
#             raise Exception('Unknown comment')
#
#     else:
#         # The recipient is the author
#         recipient = instance.reply_to
#         verb = '{0} Commented on your comment：{1}'.format(instance.user, strip_tags(instance.parent.text))
#     url = instance.content_object.get_absolute_url() + '#comment_'+str(instance.pk)
#
#     notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance,url=url)


@receiver(post_save, sender=Comment)
def send_notification(sender, instance, **kwargs):
    # Send notification
    # Determine if the comment is a blog or
    if instance.reply_to is None:
        # The recipient is the article
        recipient = instance.content_object.get_user()
        if instance.content_type.model == 'post':
            blog = instance.content_object
            verb = "{0} Commented on your article：《{1}》".format(instance.user, blog.title)
        elif instance.content_type.model == 'messages':
            verb = '{0} Leave a message for you'.format(instance.user)
        else:
            raise Exception('unknown messages')
    else:
        # The recipient is the author
        recipient = instance.reply_to
        verb = '{0} Commented on your comment：{1}'.format(instance.user, strip_tags(instance.parent.text))
    url = instance.content_object.get_absolute_url() + '#comment_'+str(instance.pk)

    notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance,url=url)