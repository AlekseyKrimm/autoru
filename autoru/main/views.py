from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.http import Http404
from django.core.paginator import Paginator

# Словарь с данными автомобилей
cars_data = {
    'bmw_x8': {
        'name': 'BMW X8',
        'description': 'BMW X8 description',
        'image': static('main/img/bmw.x8.webp'),
    },
    'audi_q7': {
        'name': 'Audi Q7',
        'description': 'Audi Q7 description',
        'image': static('main/img/audi.q7.jpg'),
    },
    'audi_rs6': {
        'name': 'Audi RS6',
        'description': 'Audi RS6 description',
        'image': static('main/img/audi.rs6.jpg'),
    },
    'bmw_m5': {
        'name': 'BMW m5',
        'description': 'BMW M5 description',
        'image': static('main/img/bmw.m5.webp'),
    },
    'mercedes_cls': {
        'name': 'Mercedes CLS',
        'description': 'Mercedes CLS description',
        'image': static('main/img/mercedes.cls.jpg'),
    },
     'mercedes_gls': {
        'name': 'Mercedes GLS',
        'description': 'Mercedes GLS description',
        'image': static('main/img/mercedes.gls.jpg'),
    },

}


creators_data = {
    'audi': {
        'name': 'Audi',
        'image': static('main/img/audi.lable.jpg'),
        'cars': ['audi_q7', 'audi_rs6']  
    },
    'bmw': {
        'name': 'BMW',
        'image': static('main/img/bmw.lable.jpg'),
        'cars': ['bmw_x8', 'bmw_m5']
    },
    'mercedes': {
        'name': 'Mercedes',
        'image': static('main/img/mercedes.lable.jpg'),
        'cars': ['mercedes_cls', 'mercedes_gls']
    },
}


def creators(request):
    context = {
        'creators': creators_data.keys(),  
    }
    
    return render(request, 'main/creators_page.html', context)


def creators_list(request):
    return render(request, 'main/creators_list.html')

def car_page(request, car):
    if car in cars_data:
        car_data = cars_data[car]
        context = {
            'name': car_data['name'],
            'description': car_data['description'],
            'image': car_data['image'],
        }
        return render(request, 'main/car_page.html', context)
    else:
        raise Http404("Нет такой тачки")

def creators_page(request, creator):
    if creator in creators_data:
        creator_data = creators_data[creator]
        context = {
            'name': creator_data['name'],
            'image': creator_data['image'],
            'cars': [
                {
                    'key': car_key,
                    **cars_data[car_key]
                }
                for car_key in creator_data['cars']
                if car_key in cars_data
            ],
        }
        return render(request, 'main/creators_page.html', context)
    else:
        raise Http404("Нет такого производителя")

def home(request):
    popular_brands = [
        {'name': 'BMW', 'logo': 'main/img/bmw.lable.jpg', 'count': 1234},
        {'name': 'Mercedes', 'logo': 'main/img/mercedes.lable.jpg', 'count': 987},
        {'name': 'Audi', 'logo': 'main/img/audi.lable.jpg', 'count': 756},
        
    ]
    
    recommended_cars = [
        {
            'name': 'BMW X8',
            'image': 'main/img/bmw.x8.webp',
            'year': 2021,
            'engine': '3.0 л',
            'transmission': 'Автомат',
            'mileage': 45000,
            'price': 4500000,
            'location': 'Москва'
        },
        {
            'name': 'Mercedes CLS',
            'image': 'main/img/mercedes.cls.jpg',
            'year': 2020,
            'engine': '2.0 л',
            'transmission': 'Автомат',
            'mileage': 32000,
            'price': 3200000,
            'location': 'Санкт-Петербург'
        },
        # Добавьте больше автомобилей...
    ]
    
    context = {
        'popular_brands': popular_brands,
        'recommended_cars': recommended_cars,
    }
    
    return render(request, 'main/home.html', context)

def catalog(request):
    return render(request, 'main/catalog.html')
def catalog(request):
    cars = [
        {
            'id': 1,
            'name': 'BMW X8',
            'main_image': 'main/img/bmw.x8.webp',
            'thumbnails': ['main/img/bmw.x8.webp', 'main/img/bmw.x8.webp', 'main/img/bmw.x8.webp'],
            'images_count': 15,
            'year': 2021,
            'mileage': 45000,
            'engine': '3.0 л дизель',
            'transmission': 'Автомат',
            'drive': 'Полный',
            'description': 'Автомобиль в отличном состоянии, один владелец, полная сервисная история, не битый, не крашеный.',
            'location': 'Москва',
            'price': 4500000,
            'old_price': 4800000,
            'price_note': 'Возможен торг',
            'seller_type': 'Частное лицо',
            'seller_name': 'Александр',
            'seller_rating': 5,
            'is_new': False,
            'is_verified': True,
            'created_at': '2023-12-01'
        },
        {
            'id': 2,
            'name': 'Mercedes GLS',
            'main_image': 'main/img/mercedes.gls.jpg',
            'thumbnails': ['main/img/mercedes.gls.jpg', 'main/img/mercedes.gls.jpg'],
            'images_count': 12,
            'year': 2020,
            'mileage': 32000,
            'engine': '2.0 л бензин',
            'transmission': 'Автомат',
            'drive': 'Задний',
            'description': 'Премиальный седан в идеальном состоянии. Регулярное ТО у официального дилера.',
            'location': 'Санкт-Петербург',
            'price': 3200000,
            'old_price': None,
            'price_note': 'Цена окончательная',
            'seller_type': 'Автосалон',
            'seller_name': 'Премиум Авто',
            'seller_rating': 4,
            'is_new': False,
            'is_verified': True,
            'created_at': '2023-11-28'
        },
         {
            'id': 3,
            'name': 'Audi RS6',
            'main_image': 'main/img/audi.rs6.jpg',
            'thumbnails': ['main/img/audi.rs6.jpg', 'main/img/audi.rs6.jpg'],
            'images_count': 8,
            'year': 2019,
            'mileage': 67000,
            'engine': '2.0 л бензин',
            'transmission': 'Автомат',
            'drive': 'Полный',
            'description': 'Отличный автомобиль для деловых поездок. Все ТО пройдены вовремя.',
            'location': 'Екатеринбург',
            'price': 2800000,
            'old_price': None,
            'price_note': 'Без торга',
            'seller_type': 'Частное лицо',
            'seller_name': 'Михаил',
            'seller_rating': 4,
            'is_new': False,
            'is_verified': False,
            'created_at': '2023-11-25'
        }
        # Добавьте больше автомобилей...
    ]
    
    # Пагинация
    paginator = Paginator(cars, 10)  # 10 объявлений на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'cars': page_obj,
    }
    
    return render(request, 'main/catalog.html', context)

def car_detail(request, car_id):
    # Данные автомобилей (в реальном проекте это будет база данных)
    cars_data = {
        1: {
            'id': 1,
            'name': 'BMW X8',
            'main_image': 'img/cars/bmw_x5_main.jpg',
            'images': [
                'main/img/bmw.x8.webp'
            ],
            'year': 2021,
            'mileage': 45000,
            'engine': '3.0 л дизель',
            'transmission': 'Автомат',
            'drive': 'Полный',
            'body_type': 'Внедорожник',
            'color': 'Черный',
            'description': 'Автомобиль в отличном состоянии, один владелец, полная сервисная история, не битый, не крашеный. Регулярное обслуживание у официального дилера.',
            'location': 'Москва',
            'price': 4500000,
            'seller_type': 'Частное лицо',
            'seller_name': 'Александр',
            'seller_phone': '+7 (999) 123-45-67',
            'created_at': '2023-12-01'
        },
        2: {
            'id': 2,
            'name': 'Mercedes GLS',
            'main_image': 'img/cars/mercedes_e200_main.jpg',
            'images': [
                'main/img/mercedes.gls.jpg',
            ],
            'year': 2020,
            'mileage': 32000,
            'engine': '2.0 л бензин',
            'transmission': 'Автомат',
            'drive': 'Задний',
            'body_type': 'Седан',
            'color': 'Белый',
            'description': 'Премиальный седан в идеальном состоянии. Регулярное ТО у официального дилера.',
            'location': 'Санкт-Петербург',
            'price': 3200000,
            'seller_type': 'Автосалон',
            'seller_name': 'Премиум Авто',
            'seller_phone': '+7 (812) 555-66-77',
            'created_at': '2023-11-28'
        },
        3: {
            'id': 3,
            'name': 'Audi RS6',
            'main_image': 'main/img/audi.rs6.jpg',
            'images': [
                'main/img/audi.rs6.jpg',
                'main/img/audi.rs6.jpg',
                'main/img/audi.rs6.jpg'
            ],
            'year': 2019,
            'mileage': 67000,
            'engine': '2.0 л бензин',
            'transmission': 'Автомат',
            'drive': 'Полный',
            'body_type': 'Седан',
            'color': 'Серый',
            'description': 'Отличный автомобиль для деловых поездок. Все ТО пройдены вовремя.',
            'location': 'Екатеринбург',
            'price': 2800000,
            'seller_type': 'Частное лицо',
            'seller_name': 'Михаил',
            'seller_phone': '+7 (343) 777-88-99',
            'created_at': '2023-11-25'
        }
    }
    
    # Получаем данные автомобиля или возвращаем 404
    if car_id in cars_data:
        car = cars_data[car_id]
        context = {'car': car}
        return render(request, 'main/car_detail.html', context)
    else:
        from django.http import Http404
        raise Http404("Автомобиль не найден")