# Generated by Django 3.2.5 on 2023-03-03 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'binding',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='catalog_title')),
                ('details', models.TextField(blank=True, null=True, verbose_name='catalog_details')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('unit', models.CharField(max_length=32, verbose_name='unit')),
            ],
            options={
                'db_table': 'catalog',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='category_title')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Coming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=256, verbose_name='organization')),
                ('datei', models.DateTimeField(verbose_name='datei')),
                ('numb', models.IntegerField(verbose_name='numb')),
            ],
            options={
                'db_table': 'coming',
                'ordering': ['datei'],
            },
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('details', models.TextField(verbose_name='construction_details')),
                ('address', models.CharField(max_length=256, verbose_name='address')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='price')),
            ],
            options={
                'db_table': 'construction',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datein', models.DateTimeField(verbose_name='datein')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='amount')),
            ],
            options={
                'db_table': 'investments',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=256, verbose_name='fio')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=64, verbose_name='phone')),
                ('link', models.URLField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='investor_photo')),
            ],
            options={
                'db_table': 'investor',
                'ordering': ['fio'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daten', models.DateTimeField(verbose_name='daten')),
                ('title', models.CharField(max_length=256, verbose_name='title_news')),
                ('details', models.TextField(verbose_name='details_news')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='photo_news')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['daten'],
            },
        ),
        migrations.CreateModel(
            name='Outgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateo', models.DateTimeField(verbose_name='dateo')),
                ('numb', models.IntegerField(verbose_name='numb')),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgo_construction', to='building.construction')),
            ],
            options={
                'db_table': 'outgo',
                'ordering': ['dateo'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_catalog', to='building.catalog')),
                ('outgo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_outgo', to='building.outgo')),
            ],
            options={
                'db_table': 'sale',
                'ordering': ['outgo'],
            },
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['daten'], name='news_daten_a29edb_idx'),
        ),
        migrations.AddIndex(
            model_name='investor',
            index=models.Index(fields=['fio'], name='investor_fio_b5ad33_idx'),
        ),
        migrations.AddField(
            model_name='investments',
            name='construction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments_construction', to='building.construction'),
        ),
        migrations.AddField(
            model_name='investments',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments_investor', to='building.construction'),
        ),
        migrations.AddIndex(
            model_name='construction',
            index=models.Index(fields=['title'], name='constructio_title_719893_idx'),
        ),
        migrations.AddIndex(
            model_name='coming',
            index=models.Index(fields=['datei'], name='coming_datei_3ee650_idx'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_category', to='building.category'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='coming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_coming', to='building.coming'),
        ),
        migrations.AddField(
            model_name='binding',
            name='construction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='binding_construction', to='building.construction'),
        ),
        migrations.AddField(
            model_name='binding',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='binding_investor', to='building.construction'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['outgo'], name='sale_outgo_i_ce5f86_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['catalog'], name='sale_catalog_6f4233_idx'),
        ),
        migrations.AddIndex(
            model_name='outgo',
            index=models.Index(fields=['construction'], name='outgo_constru_6fa0d8_idx'),
        ),
        migrations.AddIndex(
            model_name='outgo',
            index=models.Index(fields=['dateo'], name='outgo_dateo_4b33f6_idx'),
        ),
        migrations.AddIndex(
            model_name='investments',
            index=models.Index(fields=['construction'], name='investments_constru_3ec8ac_idx'),
        ),
        migrations.AddIndex(
            model_name='investments',
            index=models.Index(fields=['investor'], name='investments_investo_7aa318_idx'),
        ),
        migrations.AddIndex(
            model_name='catalog',
            index=models.Index(fields=['title'], name='catalog_title_a1bae3_idx'),
        ),
        migrations.AddIndex(
            model_name='binding',
            index=models.Index(fields=['construction'], name='binding_constru_140998_idx'),
        ),
        migrations.AddIndex(
            model_name='binding',
            index=models.Index(fields=['investor'], name='binding_investo_1e5d5f_idx'),
        ),
    ]
