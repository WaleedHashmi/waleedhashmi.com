# Generated by Django 2.1.1 on 2018-09-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180915_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(blank=True, choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JS', 'JavaScript'), ('Web-Dev', 'Web Development'), ('front-end', 'Front End'), ('back-end', 'Back End'), ('ML', 'Machine Learning'), ('R', 'R'), ('Python', 'Python'), ('Data Visualisation', 'Data Visualisation'), ('Processing', 'Processing'), ('Game Development', 'Game Development'), ('Bootstrap', 'Bootstrap'), ('C++', 'C++'), ('Swift', 'Swift'), ('p5.js', 'p5.js'), ('node.js', 'node.js'), ('Angular', 'Angular'), ('React', 'React'), ('Vue', 'Vue'), ('Django', 'Django'), ('Graphic Design', 'Graphic Design'), ('Logo', 'Logo Design'), ('Poster', 'Poster Design'), ('Illustrator', 'Illustrator'), ('Photoshop', 'Photoshop'), ('typography', 'typography'), ('Mobile App', 'Mobile App'), ('UX', 'UX design')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='top_two_tags',
            field=models.CharField(blank=True, choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JS', 'JavaScript'), ('Web-Dev', 'Web Development'), ('front-end', 'Front End'), ('back-end', 'Back End'), ('ML', 'Machine Learning'), ('R', 'R'), ('Python', 'Python'), ('Data Visualisation', 'Data Visualisation'), ('Processing', 'Processing'), ('Game Development', 'Game Development'), ('Bootstrap', 'Bootstrap'), ('C++', 'C++'), ('Swift', 'Swift'), ('p5.js', 'p5.js'), ('node.js', 'node.js'), ('Angular', 'Angular'), ('React', 'React'), ('Vue', 'Vue'), ('Django', 'Django'), ('Graphic Design', 'Graphic Design'), ('Logo', 'Logo Design'), ('Poster', 'Poster Design'), ('Illustrator', 'Illustrator'), ('Photoshop', 'Photoshop'), ('typography', 'typography'), ('Mobile App', 'Mobile App'), ('UX', 'UX design')], max_length=1, null=True),
        ),
    ]
