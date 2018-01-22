# Generated by Django 2.0.1 on 2018-01-05 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20171228_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='schoolexam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Schoolexam', verbose_name='在某学校的考试'),
        ),
    ]
