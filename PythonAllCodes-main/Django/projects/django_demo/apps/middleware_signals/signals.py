from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.models_demo.models import BlogPost
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=BlogPost)
def blogpost_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f"BlogPost created: {instance.pk} - {instance.title}")
    else:
        logger.info(f"BlogPost updated: {instance.pk} - {instance.title}")


@receiver(post_delete, sender=BlogPost)
def blogpost_deleted(sender, instance, **kwargs):
    logger.info(f"BlogPost deleted: {instance.pk} - {instance.title}")
