# Generated by Django 3.2.23 on 2023-12-20 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0044_auto_20230907_0155'),
        ('projects', '0026_auto_20231103_0020'),
        ('io_storages', '0016_add_aws_sse_kms_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApertureDBExportStorage',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('last_sync', models.DateTimeField(
                    blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync')),
                ('last_sync_count', models.PositiveIntegerField(
                    blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count')),
                ('last_sync_job', models.CharField(blank=True, help_text='Last sync job ID',
                 max_length=256, null=True, verbose_name='last_sync_job')),
                ('status', models.CharField(choices=[('initialized', 'Initialized'), ('queued', 'Queued'), (
                    'in_progress', 'In progress'), ('failed', 'Failed'), ('completed', 'Completed')], default='initialized', max_length=64)),
                ('traceback', models.TextField(
                    blank=True, help_text='Traceback report for the last failed sync', null=True)),
                ('meta', models.JSONField(
                    default=dict, help_text='Meta and debug information about storage processes', null=True, verbose_name='meta')),
                ('title', models.CharField(blank=True, help_text='Cloud storage title',
                 max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(
                    blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                 help_text='Creation time', verbose_name='created at')),
                ('synchronizable', models.BooleanField(
                    default=True, help_text='If storage can be synced', verbose_name='synchronizable')),
                ('can_delete_objects', models.BooleanField(
                    blank=True, help_text='Deletion from storage enabled', null=True, verbose_name='can_delete_objects')),
                ('hostname', models.TextField(
                    blank=True, help_text='ApertureDB host name', null=True, verbose_name='hostname')),
                ('port', models.PositiveIntegerField(
                    blank=True, help_text='ApertureDB host port', null=True, verbose_name='port')),
                ('username', models.TextField(
                    blank=True, help_text='ApertureDB user name', null=True, verbose_name='username')),
                ('password', models.TextField(
                    blank=True, help_text='ApertureDB user password', null=True, verbose_name='password')),
                ('token', models.TextField(
                    blank=True, help_text='ApertureDB user token', null=True, verbose_name='token')),
                ('use_ssl', models.BooleanField(
                    default=True, help_text='Use SSL when communicating with ApertureDB', verbose_name='use_ssl')),
                ('project', models.ForeignKey(help_text='A unique integer value identifying this project.',
                 on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_aperturedbexportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApertureDBImportStorage',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('last_sync', models.DateTimeField(
                    blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync')),
                ('last_sync_count', models.PositiveIntegerField(
                    blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count')),
                ('last_sync_job', models.CharField(blank=True, help_text='Last sync job ID',
                 max_length=256, null=True, verbose_name='last_sync_job')),
                ('status', models.CharField(choices=[('initialized', 'Initialized'), ('queued', 'Queued'), (
                    'in_progress', 'In progress'), ('failed', 'Failed'), ('completed', 'Completed')], default='initialized', max_length=64)),
                ('traceback', models.TextField(
                    blank=True, help_text='Traceback report for the last failed sync', null=True)),
                ('meta', models.JSONField(
                    default=dict, help_text='Meta and debug information about storage processes', null=True, verbose_name='meta')),
                ('title', models.CharField(blank=True, help_text='Cloud storage title',
                 max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(
                    blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                 help_text='Creation time', verbose_name='created at')),
                ('synchronizable', models.BooleanField(
                    default=True, help_text='If storage can be synced', verbose_name='synchronizable')),
                ('hostname', models.TextField(
                    blank=True, help_text='ApertureDB host name', null=True, verbose_name='hostname')),
                ('port', models.PositiveIntegerField(
                    blank=True, help_text='ApertureDB host port', null=True, verbose_name='port')),
                ('username', models.TextField(
                    blank=True, help_text='ApertureDB user name', null=True, verbose_name='username')),
                ('password', models.TextField(
                    blank=True, help_text='ApertureDB user password', null=True, verbose_name='password')),
                ('token', models.TextField(
                    blank=True, help_text='ApertureDB user token', null=True, verbose_name='token')),
                ('use_ssl', models.BooleanField(
                    default=True, help_text='Use SSL when communicating with ApertureDB', verbose_name='use_ssl')),
                ('limit', models.PositiveIntegerField(
                    blank=True, help_text='Maximum number of tasks', null=True, verbose_name='limit')),
                ('constraints', models.TextField(
                    blank=True, help_text='ApertureDB FindImage constraints (see https://docs.aperturedata.io/query_language/Reference/shared_command_parameters/constraints)', null=True, verbose_name='constraints')),
                ('as_format_jpg', models.BooleanField(default=False,
                 help_text='Convert images to JPEG format', verbose_name='as_format_jpg')),
                ('predictions', models.BooleanField(default=False,
                 help_text='Load bounding box predictions from ApertureDB?', verbose_name='predictions')),
                ('pred_constraints', models.TextField(
                    blank=True, help_text='ApertureDB constraints on bounding box predictions (see https://docs.aperturedata.io/query_language/Reference/shared_command_parameters/constraints)', null=True, verbose_name='constraints')),
                ('project', models.ForeignKey(help_text='A unique integer value identifying this project.',
                 on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_aperturedbimportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApertureDBImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(
                    help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(
                    default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                 help_text='Creation time', verbose_name='created at')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='links', to='io_storages.aperturedbimportstorage')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 related_name='io_storages_aperturedbimportstoragelink', to='tasks.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApertureDBExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(
                    default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                 help_text='Creation time', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True,
                 help_text='Update time', verbose_name='updated at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 related_name='io_storages_aperturedbexportstoragelink', to='tasks.annotation')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='links', to='io_storages.aperturedbexportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
