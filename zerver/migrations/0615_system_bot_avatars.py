# Generated by Django 5.0.9 on 2024-10-14 23:22

from django.conf import settings
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def set_system_bot_avatar_source_user(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    UserProfile = apps.get_model("zerver", "UserProfile")
    UserProfile.objects.filter(
        email__in=[
            settings.EMAIL_GATEWAY_BOT,
            settings.NOTIFICATION_BOT,
            settings.WELCOME_BOT,
        ]
    ).update(avatar_source="U")


def set_system_bot_avatar_source_gravatar(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    UserProfile = apps.get_model("zerver", "UserProfile")
    UserProfile.objects.filter(
        email__in=[
            settings.EMAIL_GATEWAY_BOT,
            settings.NOTIFICATION_BOT,
            settings.WELCOME_BOT,
        ]
    ).update(avatar_source="G")


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0614_remove_realm_move_messages_between_streams_policy"),
    ]

    operations = [
        migrations.RunPython(
            set_system_bot_avatar_source_user,
            elidable=True,
            reverse_code=set_system_bot_avatar_source_gravatar,
        ),
    ]