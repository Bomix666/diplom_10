from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(max_length=20, choices=[('pending', 'Непроверенное'), ('approved', 'Проверенное')], default='pending'),
        ),
    ]
