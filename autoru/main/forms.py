# main/forms.py
from django import forms
from django.core.exceptions import ValidationError
import re
from datetime import datetime

class CarListingForm(forms.Form):
    # Основная информация
    brand = forms.ChoiceField(
        choices=[
            ('', 'Выберите марку'),
            ('bmw', 'BMW'),
            ('mercedes', 'Mercedes-Benz'),
            ('audi', 'Audi'),
            ('toyota', 'Toyota'),
            ('volkswagen', 'Volkswagen'),
            ('hyundai', 'Hyundai'),
            ('kia', 'Kia'),
            ('ford', 'Ford'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_brand'
        }),
        error_messages={
            'required': 'Выберите марку автомобиля',
            'invalid_choice': 'Выберите марку из списка'
        }
    )
    
    model = forms.CharField(
        max_length=100,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_model',
            'disabled': True
        }),
        error_messages={
            'required': 'Выберите модель автомобиля',
            'max_length': 'Название модели не может быть длиннее 100 символов'
        }
    )
    
    year = forms.IntegerField(
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_year'
        }),
        error_messages={
            'required': 'Укажите год выпуска',
            'invalid': 'Введите корректный год'
        }
    )
    
    body_type = forms.ChoiceField(
        choices=[
            ('', 'Выберите тип кузова'),
            ('sedan', 'Седан'),
            ('hatchback', 'Хэтчбек'),
            ('suv', 'Внедорожник'),
            ('wagon', 'Универсал'),
            ('coupe', 'Купе'),
            ('convertible', 'Кабриолет'),
            ('minivan', 'Минивэн'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_body_type'
        }),
        error_messages={
            'required': 'Выберите тип кузова',
            'invalid_choice': 'Выберите тип кузова из списка'
        }
    )
    
    mileage = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: 50000'
        }),
        error_messages={
            'required': 'Укажите пробег автомобиля',
            'invalid': 'Введите корректное значение пробега'
        }
    )
    
    color = forms.ChoiceField(
        choices=[
            ('', 'Выберите цвет'),
            ('white', 'Белый'),
            ('black', 'Черный'),
            ('gray', 'Серый'),
            ('silver', 'Серебристый'),
            ('blue', 'Синий'),
            ('red', 'Красный'),
            ('green', 'Зеленый'),
            ('brown', 'Коричневый'),
            ('other', 'Другой'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_color'
        }),
        error_messages={
            'required': 'Выберите цвет автомобиля',
            'invalid_choice': 'Выберите цвет из списка'
        }
    )
    
    # Технические характеристики
    engine_type = forms.ChoiceField(
        choices=[
            ('', 'Выберите тип двигателя'),
            ('petrol', 'Бензин'),
            ('diesel', 'Дизель'),
            ('hybrid', 'Гибрид'),
            ('electric', 'Электро'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_engine_type'
        }),
        error_messages={
            'required': 'Выберите тип двигателя',
            'invalid_choice': 'Выберите тип двигателя из списка'
        }
    )
    
    engine_volume = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: 2.0'
        }),
        error_messages={
            'required': 'Укажите объем двигателя',
            'invalid': 'Введите корректное значение'
        }
    )
    
    transmission = forms.ChoiceField(
        choices=[
            ('', 'Выберите коробку передач'),
            ('manual', 'Механика'),
            ('automatic', 'Автомат'),
            ('cvt', 'Вариатор'),
            ('robot', 'Робот'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_transmission'
        }),
        error_messages={
            'required': 'Выберите коробку передач',
            'invalid_choice': 'Выберите коробку передач из списка'
        }
    )
    
    drive = forms.ChoiceField(
        choices=[
            ('', 'Выберите привод'),
            ('front', 'Передний'),
            ('rear', 'Задний'),
            ('all', 'Полный'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_drive'
        }),
        error_messages={
            'required': 'Выберите тип привода',
            'invalid_choice': 'Выберите тип привода из списка'
        }
    )
    
    power = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: 200'
        }),
        error_messages={
            'required': 'Укажите количество лошадиных сил',
            'invalid': 'Введите корректное значение'
        }
    )
    
    fuel_consumption = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: 12'
        }),
        error_messages={
            'required': 'Укажите расход топлива',
            'invalid': 'Введите корректное значение'
        }
    )
    
    # Состояние
    condition = forms.ChoiceField(
        choices=[
            ('', 'Выберите состояние'),
            ('excellent', 'Отличное'),
            ('good', 'Хорошее'),
            ('fair', 'Удовлетворительное'),
            ('poor', 'Требует ремонта'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_condition'
        }),
        error_messages={
            'required': 'Укажите состояние автомобиля',
            'invalid_choice': 'Выберите состояние из списка'
        }
    )
    
    owners_count = forms.ChoiceField(
        choices=[
            ('', 'Не указано'),
            ('1', '1 владелец'),
            ('2', '2 владельца'),
            ('3', '3 владельца'),
            ('4', '4+ владельцев'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_owners_count'
        }),
        required=False
    )
    
    accidents = forms.BooleanField(required=False)
    service_book = forms.BooleanField(required=False)
    warranty = forms.BooleanField(required=False)
    
    # Цена и контакты
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: 1000000'
        }),
        error_messages={
            'required': 'Укажите пробег цену',
            'invalid': 'Введите корректное значение'
        }
    )
    
    price_negotiable = forms.BooleanField(required=False)
    
    seller_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: Иван'
        }),
        error_messages={
            'required': 'Укажите Ваше имя',
            'invalid': 'Введите корректное имя'
        }
    )
    
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '+7 (999) 123-45-67',
            'id': 'id_phone'
        }),
        error_messages={
            'required': 'Укажите номер телефона',
            'invalid': 'Введите корректный номер телефона'
        }
    )
    
    email = forms.EmailField(
       widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: ivanov@mail.ru'
        }),
        error_messages={
            'required': 'Укажите ваш Email',
            'invalid': 'Введите корректный Email'
        }
    )
    
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Например: Москва'
        }),
        error_messages={
            'required': 'Укажите город',
            'invalid': 'Введите корректный город'
        }
    )
    
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Добавьте описание'
        }),
        error_messages={
            'required': 'Добавьте описание',
            'invalid': 'Введите корректное описание'
        }
    )
    
    
   
    
    # Кастомная валидация
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Убираем все символы кроме цифр
            phone_digits = re.sub(r'\D', '', phone)
            
            # Проверяем российский номер
            if not re.match(r'^7\d{10}$', phone_digits):
                raise ValidationError('Введите корректный российский номер телефона')
            
            return phone
        return phone
    
    def clean_seller_name(self):
        name = self.cleaned_data.get('seller_name')
        if name:
            # Проверяем, что имя содержит только буквы и пробелы
            if not re.match(r'^[а-яА-Яa-zA-Z\s]+$', name):
                raise ValidationError('Имя должно содержать только буквы')
            return name.strip()
        return name
    
    def clean_mileage(self):
        mileage = self.cleaned_data.get('mileage')
        year = self.cleaned_data.get('year')
        
        if mileage and year:
            # Проверяем реалистичность пробега
            current_year = datetime.now().year
            car_age = current_year - year
            max_realistic_mileage = car_age * 30000  # 30,000 км в год максимум
            
            if mileage > max_realistic_mileage:
                raise ValidationError(
                    f'Пробег слишком большой для автомобиля {year} года. '
                    f'Максимальный реалистичный пробег: {max_realistic_mileage:,} км'
                )
        
        return mileage
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        year = self.cleaned_data.get('year')
        
        if price and year:
            current_year = datetime.now().year
            car_age = current_year - year
            
            # Минимальная цена в зависимости от возраста
            if car_age > 20 and price < 50000:
                raise ValidationError('Цена слишком низкая для данного автомобиля')
            
            if car_age < 2 and price < 500000:
                raise ValidationError('Цена слишком низкая для нового автомобиля')
        
        return price
    
    def clean_photos(self):
        photos = self.files.getlist('photos')
        
        if photos:
            # Проверяем количество фотографий
            if len(photos) > 20:
                raise ValidationError('Можно загрузить максимум 20 фотографий')
            
            # Проверяем каждую фотографию
            for photo in photos:
                # Проверяем размер файла (максимум 5MB)
                if photo.size > 5 * 1024 * 1024:
                    raise ValidationError(f'Файл {photo.name} слишком большой. Максимальный размер: 5MB')
                
                # Проверяем тип файла
                allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
                if photo.content_type not in allowed_types:
                    raise ValidationError(f'Файл {photo.name} имеет неподдерживаемый формат. Разрешены: JPEG, PNG, WebP')
        
        return photos