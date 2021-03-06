# Generated by Django 3.2.3 on 2021-06-21 02:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_sessions_setup_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('view', models.CharField(max_length=50)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tenant')),
            ],
            options={
                'verbose_name': 'AppPermission',
                'verbose_name_plural': 'AppPermissions',
            },
        ),
        migrations.AddConstraint(
            model_name='apppermission',
            constraint=models.UniqueConstraint(fields=('tenant', 'view'), name='app_permission_tenant_unique'),
        ),
    ]
