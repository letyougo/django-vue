# Generated by Django 2.0 on 2017-12-23 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20171214_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='admin_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='考办管理员'),
        ),
        migrations.AddField(
            model_name='office',
            name='admin_phone',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='考办联系电话'),
        ),
        migrations.AddField(
            model_name='school',
            name='admin_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='学校管理员'),
        ),
        migrations.AddField(
            model_name='school',
            name='admin_phone',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='学校联系电话'),
        ),
        migrations.AlterField(
            model_name='schoolexam',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.School', verbose_name='监考学校'),
        ),
        migrations.AlterField(
            model_name='teacherexam',
            name='schoolexam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Schoolexam', verbose_name='在某学校的考试'),
        ),
    ]
