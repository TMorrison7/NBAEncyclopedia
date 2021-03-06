# Generated by Django 2.0.7 on 2018-11-27 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('record', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='record_image')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRecords',
            fields=[
                ('records_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='NBAE.Records')),
                ('player_dob', models.DateField(blank=True, null=True)),
                ('player_birthplace', models.CharField(blank=True, max_length=30, null=True)),
                ('player_nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('player_highschool', models.CharField(blank=True, max_length=40, null=True)),
                ('player_college', models.CharField(blank=True, max_length=40, null=True)),
                ('player_currentteam', models.CharField(blank=True, max_length=30, null=True)),
                ('player_allteams', models.CharField(blank=True, max_length=40, null=True)),
                ('player_bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('player_profile', models.TextField(blank=True, max_length=500, null=True)),
                ('player_accolades', models.TextField(blank=True, max_length=500, null=True)),
                ('player_references', models.TextField(blank=True, max_length=500, null=True)),
            ],
            bases=('NBAE.records',),
        ),
        migrations.CreateModel(
            name='SeasonRecords',
            fields=[
                ('records_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='NBAE.Records')),
                ('season_league', models.CharField(blank=True, max_length=50, null=True)),
                ('season_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('season_not', models.CharField(blank=True, max_length=10, null=True)),
                ('season_allteams', models.TextField(blank=True, max_length=500, null=True)),
                ('season_mvp', models.CharField(blank=True, max_length=50, null=True)),
                ('season_roy', models.CharField(blank=True, max_length=50, null=True)),
                ('season_doy', models.CharField(blank=True, max_length=50, null=True)),
                ('season_smoy', models.CharField(blank=True, max_length=50, null=True)),
                ('season_mip', models.CharField(blank=True, max_length=50, null=True)),
                ('season_coy', models.CharField(blank=True, max_length=50, null=True)),
                ('season_champion', models.CharField(blank=True, max_length=50, null=True)),
                ('season_fmvp', models.CharField(blank=True, max_length=50, null=True)),
                ('season_bio', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            bases=('NBAE.records',),
        ),
        migrations.CreateModel(
            name='TeamRecords',
            fields=[
                ('records_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='NBAE.Records')),
                ('team_conference', models.CharField(blank=True, max_length=50, null=True)),
                ('team_division', models.CharField(blank=True, max_length=50, null=True)),
                ('team_founded', models.DateField(blank=True, null=True)),
                ('team_arena', models.CharField(blank=True, max_length=50, null=True)),
                ('team_location', models.CharField(blank=True, max_length=50, null=True)),
                ('team_gm', models.CharField(blank=True, max_length=50, null=True)),
                ('team_coach', models.CharField(blank=True, max_length=50, null=True)),
                ('team_owner', models.CharField(blank=True, max_length=50, null=True)),
                ('team_accolades', models.TextField(blank=True, max_length=500, null=True)),
                ('team_roster', models.TextField(blank=True, max_length=500, null=True)),
                ('team_bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('team_reference', models.TextField(blank=True, max_length=500, null=True)),
            ],
            bases=('NBAE.records',),
        ),
        migrations.AddField(
            model_name='records',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='NBAE.Records'),
        ),
    ]
