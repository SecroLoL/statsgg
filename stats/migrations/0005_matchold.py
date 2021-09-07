# Generated by Django 3.1.7 on 2021-09-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_match_totaldamagedealt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matchold',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('champion', models.IntegerField()),
                ('championName', models.CharField(max_length=30)),
                ('spell1', models.IntegerField()),
                ('spell2', models.IntegerField()),
                ('win', models.BooleanField()),
                ('kills', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('totalDamageDealt', models.IntegerField(default=0)),
                ('goldEarned', models.IntegerField()),
                ('champLevel', models.IntegerField()),
                ('totalMinionsKilled', models.IntegerField()),
                ('item0', models.IntegerField()),
                ('item1', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
