# Generated by Django 3.1.7 on 2021-04-03 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upstat', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('downstat', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedex', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defence', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('type1', models.CharField(default=None, max_length=10)),
                ('type2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('gigantamax_factor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=100)),
                ('name1', models.CharField(max_length=100)),
                ('ability1', models.CharField(max_length=100)),
                ('nature1', models.CharField(max_length=100)),
                ('item1', models.CharField(max_length=100)),
                ('move1_1', models.CharField(max_length=100)),
                ('move2_1', models.CharField(max_length=100)),
                ('move3_1', models.CharField(max_length=100)),
                ('move4_1', models.CharField(max_length=100)),
                ('level1', models.IntegerField()),
                ('hp1', models.IntegerField()),
                ('atk1', models.IntegerField()),
                ('def1', models.IntegerField()),
                ('sp_atk1', models.IntegerField()),
                ('sp_def1', models.IntegerField()),
                ('spd1', models.IntegerField()),
                ('hpEV1', models.IntegerField()),
                ('atkEV1', models.IntegerField()),
                ('defEV1', models.IntegerField()),
                ('sp_atkEV1', models.IntegerField()),
                ('sp_defEV1', models.IntegerField()),
                ('spdEV1', models.IntegerField()),
                ('hpIV1', models.IntegerField()),
                ('atkIV1', models.IntegerField()),
                ('defIV1', models.IntegerField()),
                ('sp_atkIV1', models.IntegerField()),
                ('sp_defIV1', models.IntegerField()),
                ('spdIV1', models.IntegerField()),
                ('name2', models.CharField(max_length=100)),
                ('ability2', models.CharField(max_length=100)),
                ('nature2', models.CharField(max_length=100)),
                ('item2', models.CharField(max_length=100)),
                ('move1_2', models.CharField(max_length=100)),
                ('move2_2', models.CharField(max_length=100)),
                ('move3_2', models.CharField(max_length=100)),
                ('move4_2', models.CharField(max_length=100)),
                ('level2', models.IntegerField()),
                ('hp2', models.IntegerField()),
                ('atk2', models.IntegerField()),
                ('def2', models.IntegerField()),
                ('sp_atk2', models.IntegerField()),
                ('sp_def2', models.IntegerField()),
                ('spd2', models.IntegerField()),
                ('hpEV2', models.IntegerField()),
                ('atkEV2', models.IntegerField()),
                ('defEV2', models.IntegerField()),
                ('sp_atkEV2', models.IntegerField()),
                ('sp_defEV2', models.IntegerField()),
                ('spdEV2', models.IntegerField()),
                ('hpIV2', models.IntegerField()),
                ('atkIV2', models.IntegerField()),
                ('defIV2', models.IntegerField()),
                ('sp_atkIV2', models.IntegerField()),
                ('sp_defIV2', models.IntegerField()),
                ('spdIV2', models.IntegerField()),
                ('name3', models.CharField(max_length=100)),
                ('ability3', models.CharField(max_length=100)),
                ('nature3', models.CharField(max_length=100)),
                ('item3', models.CharField(max_length=100)),
                ('move1_3', models.CharField(max_length=100)),
                ('move2_3', models.CharField(max_length=100)),
                ('move3_3', models.CharField(max_length=100)),
                ('move4_3', models.CharField(max_length=100)),
                ('level3', models.IntegerField()),
                ('hp3', models.IntegerField()),
                ('atk3', models.IntegerField()),
                ('def3', models.IntegerField()),
                ('sp_atk3', models.IntegerField()),
                ('sp_def3', models.IntegerField()),
                ('spd3', models.IntegerField()),
                ('hpEV3', models.IntegerField()),
                ('atkEV3', models.IntegerField()),
                ('defEV3', models.IntegerField()),
                ('sp_atkEV3', models.IntegerField()),
                ('sp_defEV3', models.IntegerField()),
                ('spdEV3', models.IntegerField()),
                ('hpIV3', models.IntegerField()),
                ('atkIV3', models.IntegerField()),
                ('defIV3', models.IntegerField()),
                ('sp_atkIV3', models.IntegerField()),
                ('sp_defIV3', models.IntegerField()),
                ('spdIV3', models.IntegerField()),
                ('name4', models.CharField(max_length=100)),
                ('ability4', models.CharField(max_length=100)),
                ('nature4', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=100)),
                ('move1_4', models.CharField(max_length=100)),
                ('move2_4', models.CharField(max_length=100)),
                ('move3_4', models.CharField(max_length=100)),
                ('move4_4', models.CharField(max_length=100)),
                ('level4', models.IntegerField()),
                ('hp4', models.IntegerField()),
                ('atk4', models.IntegerField()),
                ('def4', models.IntegerField()),
                ('sp_atk4', models.IntegerField()),
                ('sp_def4', models.IntegerField()),
                ('spd4', models.IntegerField()),
                ('hpEV4', models.IntegerField()),
                ('atkEV4', models.IntegerField()),
                ('defEV4', models.IntegerField()),
                ('sp_atkEV4', models.IntegerField()),
                ('sp_defEV4', models.IntegerField()),
                ('spdEV4', models.IntegerField()),
                ('hpIV4', models.IntegerField()),
                ('atkIV4', models.IntegerField()),
                ('defIV4', models.IntegerField()),
                ('sp_atkIV4', models.IntegerField()),
                ('sp_defIV4', models.IntegerField()),
                ('spdIV4', models.IntegerField()),
                ('name5', models.CharField(max_length=100)),
                ('ability5', models.CharField(max_length=100)),
                ('nature5', models.CharField(max_length=100)),
                ('item5', models.CharField(max_length=100)),
                ('move1_5', models.CharField(max_length=100)),
                ('move2_5', models.CharField(max_length=100)),
                ('move3_5', models.CharField(max_length=100)),
                ('move4_5', models.CharField(max_length=100)),
                ('level5', models.IntegerField()),
                ('hp5', models.IntegerField()),
                ('atk5', models.IntegerField()),
                ('def5', models.IntegerField()),
                ('sp_atk5', models.IntegerField()),
                ('sp_def5', models.IntegerField()),
                ('spd5', models.IntegerField()),
                ('hpEV5', models.IntegerField()),
                ('atkEV5', models.IntegerField()),
                ('defEV5', models.IntegerField()),
                ('sp_atkEV5', models.IntegerField()),
                ('sp_defEV5', models.IntegerField()),
                ('spdEV5', models.IntegerField()),
                ('hpIV5', models.IntegerField()),
                ('atkIV5', models.IntegerField()),
                ('defIV5', models.IntegerField()),
                ('sp_atkIV5', models.IntegerField()),
                ('sp_defIV5', models.IntegerField()),
                ('spdIV5', models.IntegerField()),
                ('name6', models.CharField(max_length=100)),
                ('ability6', models.CharField(max_length=100)),
                ('nature6', models.CharField(max_length=100)),
                ('item6', models.CharField(max_length=100)),
                ('move1_6', models.CharField(max_length=100)),
                ('move2_6', models.CharField(max_length=100)),
                ('move3_6', models.CharField(max_length=100)),
                ('move4_6', models.CharField(max_length=100)),
                ('level6', models.IntegerField()),
                ('hp6', models.IntegerField()),
                ('atk6', models.IntegerField()),
                ('def6', models.IntegerField()),
                ('sp_atk6', models.IntegerField()),
                ('sp_def6', models.IntegerField()),
                ('spd6', models.IntegerField()),
                ('hpEV6', models.IntegerField()),
                ('atkEV6', models.IntegerField()),
                ('defEV6', models.IntegerField()),
                ('sp_atkEV6', models.IntegerField()),
                ('sp_defEV6', models.IntegerField()),
                ('spdEV6', models.IntegerField()),
                ('hpIV6', models.IntegerField()),
                ('atkIV6', models.IntegerField()),
                ('defIV6', models.IntegerField()),
                ('sp_atkIV6', models.IntegerField()),
                ('sp_defIV6', models.IntegerField()),
                ('spdIV6', models.IntegerField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.userprofile')),
            ],
        ),
    ]
