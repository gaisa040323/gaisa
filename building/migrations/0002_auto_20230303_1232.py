# Generated by Django 3.2.5 on 2023-03-03 06:32

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

from datetime import datetime, timedelta
import time

def initialization(apps, schema_editor):

    # Суперпользователь id=1
    user = User.objects.create_superuser(username='root',
    email='shop260222@mail.ru',
    password='SsNn5678+-@')
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id=2
    user = User.objects.create_user(username='manager', password='Ss0066+-')
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи id=3...27 
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина')
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова')
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина')
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов')
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев')
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Бауржан', last_name='Арыкбаев')
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Алишер', last_name='Танатаров')
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Мерует', last_name='Искакова')
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Ольга', last_name='Муравьева')
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Ақжарқын', last_name='Сансызбаева')
    print("Созданы простые пользователи")

    ##### Объект строительства  #####

    Construction = apps.get_model("building", "Construction")
    
    construction = Construction()
    construction.title = '8-й этажный жилой дом угол Лермонтова - Мира'
    construction.details = '8-й этажный жилой дом угол Лермонтова - Мира'
    construction.address = 'ул. Лермонтова, 60'
    construction.price = 100000000
    construction.save()
   
    construction = Construction()
    construction.title = '10-й этажный жилой дом угол Лермонтова - Мира'
    construction.details = '10-й этажный жилой дом угол Лермонтова - Мира'
    construction.address = 'ул. Лермонтова, 41'
    construction.price = 120000000
    construction.save()
   
    construction = Construction()
    construction.title = '8-й этажный жилой дом угол Лермонтова - Космонавтов'
    construction.details = '8-й этажный жилой дом угол Лермонтова - Космонавтов'
    construction.address = 'ул. Космонавтов, 7'
    construction.price = 100000000
    construction.save()
   
    construction = Construction()
    construction.title = '10-й этажный жилой дом угол Лермонтова - Космонавтов'
    construction.details = '10-й этажный жилой дом угол Лермонтова - Космонавтов'
    construction.address = 'ул. Космонавтов, 9'
    construction.price = 120000000
    construction.save()
   
    construction = Construction()
    construction.title = '9-й этажный жилой дом улица Авиаторов'
    construction.details = '9-й этажный жилой дом улица Авиаторов'
    construction.address = 'ул. Авиаторов, 7'
    construction.price = 125000000
    construction.save()
   
    construction = Construction()
    construction.title = '16-й этажный жилой дом улица Авиаторов'
    construction.details = '16-й этажный жилой дом улица Авиаторов'
    construction.address = 'ул. Авиаторов, 9'
    construction.price = 160000000
    construction.save()
   
    construction = Construction()
    construction.title = 'Офисное здание пос. Ленинский'
    construction.details = 'Офисное здание пос. Ленинский'
    construction.address = 'ул. Крайняя, 10'
    construction.price = 70000000
    construction.save() 

    construction = Construction()
    construction.title = 'Офисное здание улица Горького'
    construction.details = 'Офисное здание улица Горького'
    construction.address = 'ул. Горького, 20'
    construction.price = 80000000
    construction.save()
    
    construction = Construction()
    construction.title = 'Офисное здание улица Торайгырова'
    construction.details = 'Офисное здание улица Торайгырова'
    construction.address = 'ул. Торайгырова, 30'
    construction.price = 95000000
    construction.save()
    
    construction = Construction()
    construction.title = '16-й этажный жилой дом улица Каирбаева'
    construction.details = '16-й этажный жилой дом улица Каирбаева'
    construction.address = 'ул. Каирбаева, 20'
    construction.price = 95000000
    construction.save()

    print("Инвесторы OK")

    ##### Объект строительства  #####

    Investor = apps.get_model("building", "Investor")
    
    investor = Investor()
    investor.fio = 'Нажмиденов Аслан Жумартович'
    investor.email = 'aslan@mail.ru'
    investor.phone = '+7-701-111-1111'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor1.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Болатова Айзада Кайрболатовна'
    investor.email = 'aizada@mail.ru'
    investor.phone = '+7-701-111-2222'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor2.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Кумарбеков Жантуар Маратович'
    investor.email = 'zhantuar@mail.ru'
    investor.phone = '+7-701-111-3333'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor3.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Тілеулиева Мариам Қанатқызы'
    investor.email = 'mariam@mail.ru'
    investor.phone = '+7-701-111-4444'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor4.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Ануар Данияр Болатұлы'
    investor.email = 'daniyar@mail.ru'
    investor.phone = '+7-701-111-5555'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor5.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Кусаинова Сымбат Усенқызы'
    investor.email = 'symbat@mail.ru'
    investor.phone = '+7-701-111-6666'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor6.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Ерлан Бекасыл Ерланұлы'
    investor.email = 'bekasyl@mail.ru'
    investor.phone = '+7-701-111-7777'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor7.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Альмуханова Жанар Орынғалиқызы'
    investor.email = 'zhanar@mail.ru'
    investor.phone = '+7-701-111-8888'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor8.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Тұратаев Абзал Асқанбекұлы'
    investor.email = 'abzal@mail.ru'
    investor.phone = '+7-701-111-9999'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor9.jpeg'
    investor.save()
    
    investor = Investor()
    investor.fio = 'Серікбай Меруерт Омарқызы'
    investor.email = 'meruert@mail.ru'
    investor.phone = '+7-701-111-1010'
    investor.link = 'https://ru-ru.facebook.com/'
    investor.photo = 'images/investor10.jpeg'
    investor.save()
   
    print("Инвесторы OK")

    ##### Привязка объектов к инвесторам  #####

    Binding = apps.get_model("building", "Binding")
    
    binding = Binding()
    binding.construction_id = 1   
    binding.investor_id = 1   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 2   
    binding.investor_id = 2   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 3   
    binding.investor_id = 3   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 4   
    binding.investor_id = 4   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 5   
    binding.investor_id = 5   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 6   
    binding.investor_id = 6  
    binding.save()
    
    binding = Binding()
    binding.construction_id = 7   
    binding.investor_id = 7  
    binding.save()
    
    binding = Binding()
    binding.construction_id = 8   
    binding.investor_id = 8   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 9   
    binding.investor_id = 9   
    binding.save()
    
    binding = Binding()
    binding.construction_id = 10   
    binding.investor_id = 10   
    binding.save()

    print("Привязка объектов к инвесторам OK")

    ##### Инвестиции  #####

    Investments = apps.get_model("building", "Investments")
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=60)
    investments.construction_id = 1   
    investments.investor_id = 1   
    investments.amount = 20000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=55)
    investments.construction_id = 2   
    investments.investor_id = 2   
    investments.amount = 25000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=50)
    investments.construction_id = 3   
    investments.investor_id = 3   
    investments.amount = 15000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=45)
    investments.construction_id = 4   
    investments.investor_id = 4   
    investments.amount = 20000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=40)
    investments.construction_id = 5   
    investments.investor_id = 5   
    investments.amount = 25000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=35)
    investments.construction_id = 6   
    investments.investor_id = 6   
    investments.amount = 15000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=30)
    investments.construction_id = 7   
    investments.investor_id = 7   
    investments.amount = 20000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=25)
    investments.construction_id = 8   
    investments.investor_id = 8   
    investments.amount = 25000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=20)
    investments.construction_id = 9   
    investments.investor_id = 9   
    investments.amount = 15000000   
    investments.save()
    
    investments = Investments()
    investments.datein = datetime.now() - timedelta(days=15)
    investments.construction_id = 10   
    investments.investor_id = 10   
    investments.amount = 20000000   
    investments.save()

    print("Инвестиции OK")

    ###### Приходные накладные  #####

    Coming = apps.get_model("building", "Coming")
    
    coming = Coming()
    coming.organization = 'AnShah'
    coming.datei = datetime.now() - timedelta(days=45)
    coming.numb = 1
    coming.save()

    coming = Coming()
    coming.organization = 'TRADE CK'
    coming.datei = datetime.now() - timedelta(days=44)
    coming.numb = 2
    coming.save()

    coming = Coming()
    coming.organization = 'Ban Stroy'
    coming.datei = datetime.now() - timedelta(days=43)
    coming.numb = 3
    coming.save()

    coming = Coming()
    coming.organization = 'E-group'
    coming.datei = datetime.now() - timedelta(days=42)
    coming.numb = 4
    coming.save()

    coming = Coming()
    coming.organization = 'ФИВАРУСС,ИП'
    coming.datei = datetime.now() - timedelta(days=41)
    coming.numb = 5
    coming.save()
    
    coming = Coming()
    coming.organization = 'ТОО "AV Chemical"'
    coming.datei = datetime.now() - timedelta(days=40)
    coming.numb = 6
    coming.save()

    coming = Coming()
    coming.organization = 'SB Constructions'
    coming.datei = datetime.now() - timedelta(days=39)
    coming.numb = 7
    coming.save()

    coming = Coming()
    coming.organization = 'Set stroi Consulting'
    coming.datei = datetime.now() - timedelta(days=38)
    coming.numb = 8
    coming.save()

    coming = Coming()
    coming.organization = 'Артерьер'
    coming.datei = datetime.now() - timedelta(days=37)
    coming.numb = 9
    coming.save()

    coming = Coming()
    coming.organization = 'ТОО ТД "КарСтройДом"'
    coming.datei = datetime.now() - timedelta(days=36)
    coming.numb = 10
    coming.save()

    print("Приходные накладные OK")

    ###### Категория товара #####

    Category = apps.get_model("building", "Category")

    category = Category()
    category.title='Кирпич'   
    category.save()
    
    category = Category()
    category.title='Кровельные материалы'   
    category.save()

    category = Category()
    category.title='Теплоизоляционные материалы'   
    category.save()

    category = Category()
    category.title='Фасадные материалы'   
    category.save()

    category = Category()
    category.title='Пиломатериалы'   
    category.save()

    category = Category()
    category.title='Гидроизоляционные материалы'   
    category.save()
    
    category = Category()
    category.title='Железобетонные изделия'   
    category.save()
    
    category = Category()
    category.title='Сухие строительные смеси'   
    category.save()
    
    category = Category()
    category.title='Сыпучие материалы'   
    category.save()
    
    category = Category()
    category.title='Звукоизоляционные материалы'   
    category.save()

    print("Категория товара OK")

    ###### Товар #####
    
    Catalog = apps.get_model("building", "Catalog")

    catalog = Catalog()
    catalog.coming_id = 1
    catalog.category_id = 1
    catalog.title='Керамический красный кирпич пустотелый М150, 400х200х140 мм'
    catalog.details='Керамический кирпич - строительный материал, который традиционно используется много лет и до сих пор остаётся востребованным. Такую популярность керамический кирпич приобрёл благодаря своей практичности и надёжности. Здания, возведённые с помощью этого материала, стоят сотни лет. Керамический кирпич изготавливают из глины с добавками. Благодаря глиняной основе строительный материал обладает ценными характеристиками: экологической безопасностью и прочностью.'
    catalog.price=325
    catalog.quantity=10000
    #catalog.photo='images/catalog01.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 1
    catalog.category_id = 1
    catalog.title='Кирпич строительный М100 250*120*65 мм'
    catalog.details='Кирпич М 100  Доставка по городу за город , форма оплаты любая , доставка в течений часа , полный пакет документов , 100% гарантия качества , бой при выгрузке не более 1% '
    catalog.price=30
    catalog.quantity=10000
    #catalog.photo='images/catalog02.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 2
    catalog.category_id = 2
    catalog.title='Конек кровельный'
    catalog.details='Длина: 2, 2.5, 1.25, 3. Вид: круглый, фигурный, плоский, металлочерепичный, простой, ребро, малый, острый. Материал: оцинкованная сталь, сталь, полимер, полиэстер'
    catalog.price=680
    catalog.quantity=100
    #catalog.photo='images/catalog03.jpg'
    catalog.unit='погонный метр'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 2
    catalog.category_id = 2
    catalog.title='Модульная металлочерепица черепица BRABUS 3D'
    catalog.details='Главные преимущества металлочерепицы BRABUS 3D – это: привлекательный внешний вид, большая цветовая гамма; пожаробезопасный и экологически чистый материал; легкость при монтаже; металл за счет покрытия не подвержен коррозии'
    catalog.price=4860
    catalog.quantity=100
    #catalog.photo='images/catalog04.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 3
    catalog.category_id =3
    catalog.title='Вата огнеупорная МКРР-130'
    catalog.details='МКРР-130 ― Вата (муллито-кремнеземистое волокно) огнеупорная теплоизоляционная производится плавкой в электрической печи материала содержащего чистые оксиды алюминия и кремния с последующим образованием волокна методом раздува. Вата МКРР-130 - эффективный теплоизоляционный материал.'
    catalog.price=1300
    catalog.quantity=1000
    #catalog.photo='images/catalog05.jpg'
    catalog.unit='кг'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 3
    catalog.category_id = 3
    catalog.title='Картон Асбестовый КАОН-1 ГОСТ 2850-95 толщина 5 мм'
    catalog.details='Картон Асбестовый КАОН-1 ГОСТ 2850-95 размер 1000*800*5 мм, предназначен для использования в качестве огнезащитного теплоизоляционного материала при температуре изолируемой поверхности не более 500°С. Изготавливается в листах. '
    catalog.price=520
    catalog.quantity=1000
    #catalog.photo='images/catalog06.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 4
    catalog.category_id = 4
    catalog.title='Фибро-цементная плита 1570*1200*8,0мм текстурная (кирпич)'
    catalog.details='Фиброцементные плиты представляют собой прямоугольные листы с гладкоокрашенной или фактурной лицевой поверхностью. Торцы плиты окрашены в цвет. На внутреннюю сторону плиты (не лицевую) наносится специальный слой грунтовки. Основой плиты является прессованный лист фиброцемента, автоклавированный.'
    catalog.price=10000
    catalog.quantity=100
    #catalog.photo='images/catalog07.jpg'
    catalog.unit='кв.м'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 4
    catalog.category_id = 4
    catalog.title='Искусственный камень'
    catalog.details=' Фасадные панели Идеал ТОО «Идеал Систем» используя передовые технологии европейских стран и свои собственные разработки в области производства строительных материалов наладило производство фасадных панелей «ИДЕАЛ» на основе полимерного фибробетона. '
    catalog.price=2550
    catalog.quantity=100
    #catalog.photo='images/catalog08.jpg'
    catalog.unit='кв.м'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 5
    catalog.category_id = 5
    catalog.title='Фанера Береза 4 мм 1,52*1,52 мм сорт 4/4'
    catalog.details='Фанера Береза 4 мм 1,52*1,52 мм сорт 4/4'
    catalog.price=4000
    catalog.quantity=100
    #catalog.photo='images/catalog09.jpg'
    catalog.unit='лист'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 5
    catalog.category_id = 5
    catalog.title='ДСП (древесно-стружечная плита)'
    catalog.details='Размер: 16. Раскрой: 2.44х1.83, 3.5х1.75.'
    catalog.price=4678
    catalog.quantity=100
    #catalog.photo='images/catalog10.jpg'
    catalog.unit='лист'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 6
    catalog.category_id = 6
    catalog.title='Геомембрана 1мм HDPE/LDPE'
    catalog.details='Геомембрана 1мм HDPE/LDPE'
    catalog.price=1250
    catalog.quantity=100
    #catalog.photo='images/catalog11.jpg'
    catalog.unit='кв.м'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 6
    catalog.category_id = 6
    catalog.title='Гидроизоляция Унифлекс ЭПП'
    catalog.details='Гидроизоляция Унифлекс ЭПП'
    catalog.price=1590
    catalog.quantity=100
    #catalog.photo='images/catalog12.jpg'
    catalog.unit='кв.м'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 7
    catalog.category_id = 7
    catalog.title='Плита ПК 72.15-8'
    catalog.details='Железобетонные плиты перекрытия широко используются для формирования несущей конструкции зданий, поэтому от их качества во многом зависит долговечность и прочность сооружения. Поскольку несущая конструкция должна выдерживать серьезную нагрузку, элементы перекрытия изготавливаются только из высококачественного бетона.'
    catalog.price=170000
    catalog.quantity=100
    #catalog.photo='images/catalog13.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 7
    catalog.category_id = 7
    catalog.title='Плита ПК 30.15-8'
    catalog.details='Железобетонные плиты перекрытия широко используются для формирования несущей конструкции зданий, поэтому от их качества во многом зависит долговечность и прочность сооружения. Поскольку несущая конструкция должна выдерживать серьезную нагрузку, элементы перекрытия изготавливаются только из высококачественного бетона.'
    catalog.price=68095
    catalog.quantity=100
    #catalog.photo='images/catalog14.jpg'
    catalog.unit='шт.'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 8
    catalog.category_id = 8
    catalog.title='Цемент Д-20, ПЦ400, II/А-3 32.5Б'
    catalog.details='Маркировка: д-20, ПЦ400, II/А-3 32.5Б., мешок 50 кг'
    catalog.price=1673
    catalog.quantity=100
    #catalog.photo='images/catalog15.jpg'
    catalog.unit='мешок'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 8
    catalog.category_id = 8
    catalog.title='Противоморозная добавка в бетон Криопласт -15'
    catalog.details='Противоморозная добавка в бетон, применяется в зимнее время.'
    catalog.price=175
    catalog.quantity=100
    #catalog.photo='images/catalog16.jpg'
    catalog.unit='кг'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 9
    catalog.category_id = 9
    catalog.title='Щебень (гранитный, известняковый)'
    catalog.details='Щебень маркировки: 4-8, 5-10, 10-15, 10-20, 11.2-16, 16-22.4, 16-31.5, 20-40, 22.4-31.5, 25-60, 31.5-45, 31.5-63, 4-16, 4-5.6, 40-70, 40-80, 5-20, 5.6-8, 60-150, 70-250, 8-11.2, 8-16'
    catalog.price=520
    catalog.quantity=100
    #catalog.photo='images/catalog17.jpg'
    catalog.unit='куб.м'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 9
    catalog.category_id = 9
    catalog.title='Глина бентонитовая модифицированная ECOS ( измельченная до 5 мкм) К'
    catalog.details='В добывающей промышленности широко применяется бентонитовый глинопорошок. На основе этого продукта изготавливаются растворы для бурения. Свои уникальные свойства раствор получает благодаря тому, что активированной кальцинированной'
    catalog.price=80
    catalog.quantity=100
    #catalog.photo='images/catalog18.jpg'
    catalog.unit='кг'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 10
    catalog.category_id = 10
    catalog.title='Акустический поролон 1х2м'
    catalog.details='Акустический поролон применяется для корректировки акустических характеристик помещений. Снижает интенсивность и предотвращает многократное отражение звука от поверхностей. Улучшает звукоизоляцию и снижает эффект эха и искажения звука. Эффективен в качестве ВЧ и СЧ настенных ловушек и угловых басовых ловушек. Высота волны 20 мм., общая толщина листа 30 мм., размер листа 1х2м.'
    catalog.price=10000
    catalog.quantity=100
    #catalog.photo='images/catalog19.jpg'
    catalog.unit='лист'
    catalog.save()

    catalog = Catalog()
    catalog.coming_id = 10
    catalog.category_id = 10
    catalog.title='Плиты и маты Тилит® ТП'
    catalog.details='Плиты и маты ТИЛИТ® ТП — состоят из плотного пенополистирола, алюминиевой фольги и защитной полимерной пленки со специальной разметкой.'
    catalog.price=2097
    catalog.quantity=100
    #catalog.photo='images/catalog20.jpg'
    catalog.unit='шт.'
    catalog.save()
    
    print("Товар OK")

    ###### Расходные накладные #####

    Outgo = apps.get_model("building", "Outgo")
    
    outgo = Outgo()
    outgo.construction_id = 1
    outgo.dateo = datetime.now() - timedelta(days=10)
    outgo.numb = 1
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 2
    outgo.dateo = datetime.now() - timedelta(days=9)
    outgo.numb = 2
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 3
    outgo.dateo = datetime.now() - timedelta(days=8)
    outgo.numb = 3
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 4
    outgo.dateo = datetime.now() - timedelta(days=7)
    outgo.numb = 4
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 5
    outgo.dateo = datetime.now() - timedelta(days=6)
    outgo.numb = 5
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 6
    outgo.dateo = datetime.now() - timedelta(days=5)
    outgo.numb = 6
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 7
    outgo.dateo = datetime.now() - timedelta(days=4)
    outgo.numb = 7
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 8
    outgo.dateo = datetime.now() - timedelta(days=3)
    outgo.numb = 8
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 9
    outgo.dateo = datetime.now() - timedelta(days=2)
    outgo.numb = 9
    outgo.save()
    
    outgo = Outgo()
    outgo.construction_id = 10
    outgo.dateo = datetime.now() - timedelta(days=1)
    outgo.numb = 10
    outgo.save()

    print("Расходные накладные OK")

    ###### Продажа #####
    
    Sale = apps.get_model("building", "Sale")
    
    sale = Sale()
    sale.outgo_id = 1
    sale.catalog_id = 1
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 1
    sale.catalog_id = 2
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 2
    sale.catalog_id = 3
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 2
    sale.catalog_id = 4
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 3
    sale.catalog_id = 5
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 3
    sale.catalog_id = 6
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 4
    sale.catalog_id = 7
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 4
    sale.catalog_id = 8
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 5
    sale.catalog_id = 9
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 5
    sale.catalog_id = 10
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 6
    sale.catalog_id = 11
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 6
    sale.catalog_id = 12
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 7
    sale.catalog_id = 13
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 7
    sale.catalog_id = 14
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 8
    sale.catalog_id = 15
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 8
    sale.catalog_id = 16
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 9
    sale.catalog_id = 17
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 9
    sale.catalog_id = 18
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 10
    sale.catalog_id = 19
    sale.quantity = 50
    sale.save()
    
    sale = Sale()
    sale.outgo_id = 10
    sale.catalog_id = 20
    sale.quantity = 50
    sale.save()
    
    print("Продажа OK")

    ##### Новости #####
    News = apps.get_model("building", "News")

    news = News()
    news.daten = datetime.now() - timedelta(days=45)
    news.title = 'Будем изымать участки - аким Астаны о точечной застройке'
    news.details = """Аким Астаны Женис Касымбек заявил, что администрация города намерена максимально препятствовать точечной застройке
    На встрече акима с жителями района Байконыр астанчанка подняла вопрос точечной застройки.
    "Сегодня точечная застройка стоит на контроле у Президента страны. Так почему теперь бы не объединиться и не решать эти проблемы? Точечная застройка нарушает все нормы, к уже стоящему дому подключается новый дом, и инженерные сети не выдерживают", - обратилась жительница района.
    Аким столицы заверил, что "по точечной застройке позиция с жителями совпадает".
    "Точечной застройке в городе мы максимально будем препятствовать. По тем объектам, по которым есть проблемные вопросы, по большинству из них мы находим решения с застройщиками. Под государственные нужды будем изымать эти участки. Там, где еще не начато строительство, в основном предполагаются социальные объекты", - пообещал Женис Касымбек во время встречи с жителями."""
    news.photo = 'images/news1.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() - timedelta(days=45)
    news.title = 'Первый муниципальный многоярусный паркинг появится в Алматы'
    news.details = """Первый муниципальный многоярусный паркинг появится в Алматы. Об этом в четверг на встрече с жителями Бостандыкского района сообщил аким города Ерболат Досаев, передает Tengrinews.kz со ссылкой на Almaty.tv.
    "На одной из предыдущих встреч с жителями района поднимался вопрос по объекту незавершенного строительства под паркинг в микрорайоне Коктем-3. Национальный банк передал данный объект на баланс города. Строительство этого первого многоярусного муниципального паркинга на 267 парковочных мест завершится до конца года", - сказал аким Алматы."""
    news.photo = 'images/news2.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() - timedelta(days=40)
    news.title = 'Критику Токаева о хаотичной застройке прокомментировали в акимате Астаны'
    news.details = """Как планируют решить проблему c хаотичными застройками в Астане, рассказали в акимате, передает корреспондент Tengrinews.kz.
    В акимате Астаны сообщили, что согласно дизайн-коду при согласовании эскизных проектов и во избежание хаотичного размещения реклам на первых этажах жилых многоквартирных и общественных зданий проверяются предусмотренные рекламные поля на фасадах, также учитываются применяемые материалы отделки и цветовая палитра объектов.
    "Доступ для входных групп на первых этажах предусматривается с нулевой отметки без ступеней и организации пандусов, что обеспечивает беспрепятственный доступ для маломобильных групп. При реконструкции существующих объектов с организацией входных групп учитывается единое цветовое решение, применение материалов отделки и пандусы для доступа маломобильных групп населения в соответствии с действующими нормами", - сообщили в акимате."""
    news.photo = 'images/news3.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() - timedelta(days=30)
    news.title = 'Форум клиентов BI Group: открытый диалог жителей и девелопера'
    news.details = """В Астане прошел традиционный форум клиентов строительного холдинга BI Group. Впервые после пандемии встреча состоялась в офлайн-формате.
    Более 400 жителей недавно сданных жилых комплексов комфорт- и стандарт-класса: "Поколение", Greenline, "Ару қала", Capital Park, Grand Turan Comfort, Nexpo City, Besterek, Sezim Qala, Jetisu Aqsu получили ответы на все интересующие их вопросы непосредственно от руководства компании. Очередные форумы для новоселов других домов намечены на 25 февраля и 4 марта 2023 года.
    В портфеле девелопера - 109 действующих проектов в 6 регионах - Астане, Алматы, Шымкенте, Атырау, Актау и Ташкенте. За 2022 год построено 1 785 000 квадратных метров жилья. Все обещанные проекты строятся и достраиваются.
    "Когда нет корректной информации, появляется некорректная. Зная эту простую истину, мы - как слышащая компания - всегда стараемся оперативно давать обратную связь своим клиентам. Сейчас в СМИ и соцсетях много компрометирующих сведений о неблагонадежности рынка жилья. Нас этот факт огорчает. Поэтому было принято решение вернуть добрую традицию по проведению встреч с жителями, где каждый может задать вопрос первым руководителям подразделений BI. Мы всегда открыты к диалогу и никогда не оставляем своих клиентов один на один с проблемой", - отметил генеральный директор BI Development Амангельды Омаров."""
    news.photo = 'images/news4.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() - timedelta(days=20)
    news.title = 'Я за разумное строительство в Алматы - аким Досаев'
    news.details = """Аким Алматы Ерболат Досаев пообещал повысить требования к сейсмостойкости строительства, передает корреспондент Tengrinews.kz.
    В ходе встречи с населением Жетысуского района акима Алматы жительница района предложила перенести все многоэтажное строительство из Алматы в Gate City. Это связано и с сейсмоопасностью, и с нагрузкой на инфраструктуру.
    Аким сообщил, что в Алматы уже действует ограничение в 9 этажей в верхней части города, где расположена наиболее сейсмически активная зона и находятся разломы. Это учтено в проекте нового генплана города. Однако также планируется ужесточение требований, касающихся сейсмостойкости строительства в Алматы.
    "Вчера во время моей встречи с Главой государства он одобрил подходы, в рамках которых мы через закон "Об особом статусе города Алматы" усилим требования, связанные со строительством и сейсмостойкостью. Я надеюсь, что в весеннюю сессию уже начнем эту работу, депутаты маслихата поддержат нас, и у нас появятся особые условия, когда город будет сам контролировать то, что необходимо по специальным стандартам. Эти нормы будут внедрены, и, надеюсь, уже с осени это будет работать", - сообщил аким."""
    news.photo = 'images/news5.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() - timedelta(days=10)
    news.title = 'Касымбек поручил ускорить темпы завершения долгостроев в Астане'
    news.details = """Аким столицы Женис Касымбек поручил ускорить темпы строительства долгостроев, передает Tengrinews.kz.
    "В городе насчитывается более 30 ЖК-долгостроев. Каждый многоквартирный жилой комплекс со своей довольно сложной историей. За каждым ЖК - судьбы людей. Поэтапно мы завершим строительство данных ЖК-долгостроев, а дольщики смогут заехать в свои долгожданные квартиры", - написал аким в Instagram."""
    news.photo = 'images/news6.jpeg' 
    news.save()

    news = News()
    news.daten = datetime.now() 
    news.title = 'Cейсмоустойчив ли мой дом? Какие здания Алматы проверяли на подземные толчки?'
    news.details = """Специалист АО "КазНИИСА" рассказала, какие здания в Алматы проходили реальные тесты на устойчивость при землетрясениях и какие типы домов можно назвать наиболее надежными, передает корреспондент Tengrinews.kz.
    По словам управляющего директора по производству АО "КазНИИСА" Ералы Шокбарова, в Алматы основная часть жилых домов делится на несколько типов и была построена еще в советское время, когда здания возводились по типовым сериям. Их испытывали на нагрузки институты, которые разрабатывали эти типы, и после натурных испытаний выводили их в массовое строительство. На сегодня типичными примерами таких зданий являются 308-я серия (трех- и четырехэтажные кирпичные дома 1939-1981 годов постройки) и 275-я серия (кирпичные дома 1951-1956 годов постройки). Далее идут серии крупнопанельных домов серий КЗ-464 (панельные "хрущевки", строившиеся с 1961 года), 69-я и известная "алматинская" серия домов 1-158 (девятиэтажки, строившиеся с 70-х годов). Также в Алматы имеются каркасные дома типовых серий ВП и ВТ, пятиэтажные дома ЖКУ, изготовлявшиеся из сборных каркасов и монтируемые прямо на площадке.
    "Из этих серий самыми надежными домами являются каркасно-панельные и крупнопанельные здания. Они проходили испытания, включая натурные. К ним относятся каркасно-панельные дома ЖКУ, крупнопанельные здания серий Кз и Кзу-464, а также девятиэтажные дома 158-й серии. В 2017 году наш институт проводил паспортизацию застройки в сейсмически активной зоне Алматы. В ходе этого процесса описывались конструктивные решения зданий, объемно-планировочные решения, текущее физическое состояние и конструктивные уязвимости. Всего в перечень вошло более 10 тысяч зданий, включая не только жилые дома, но и социальные объекты, такие как административные здания, школы и поликлиники. В итоге было выяснено, что 30-35 процентов из них не являются сейсмостойкими. По ним были даны рекомендации по сейсмоусилению или замене на новые", - рассказал представитель "КазНИИСА"."""
    news.photo = 'images/news7.jpeg' 
    news.save()

    print("Новости Ok")

class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialization),
        #migrations.RunSQL("""CREATE VIEW view_catalog AS
        #                SELECT catalog.id, catalog.code, catalog.category_id, category.title AS category, catalog.title, catalog.info, catalog.details, catalog.price, catalog.quantity, catalog.photo, 
        #                (SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
        #                (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity,
        #                IIF ((catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) IS NULL, catalog.quantity, (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) ) AS available
        #                FROM catalog LEFT JOIN category ON catalog.category_id = category.id;"""),
        #migrations.RunSQL("""CREATE VIEW view_sale AS
        #                SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, sale.quantity, sale.price*sale.quantity AS total, user_id, rating, sale.details,
        #                (SELECT strftime('%d.%m.%Y',deliveryday) || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
        #                FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
        #                LEFT JOIN auth_user ON sale.user_id = auth_user.id"""),
    ]

