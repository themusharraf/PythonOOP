## Pythonda ob'ektga yo'naltirilgan dasturlash
---

- Xulosa : ushbu qo'llanmada siz Python-da ob'ektga yo'naltirilgan dasturlashni o'rganasiz, jumladan objects, classes,
  attributes, methods, inheritances, overriding methods va boshqalar kabi muhim tushunchalar bor.

1. ### Python ob'ektga yo'naltirilgan dasturlashga kirish.

   `Python-da hamma narsa ob'ektdir`. Ob'ektning holati va xatti-harakatlari mavjud. Ob'ektni yaratish uchun avval siz
   classni aniqlaysiz. Va keyin, classdan siz bir yoki bir nechta ob'ektlarni yaratishingiz mumkin. Ob'ektlar classning
   namunalari.

---

2. ### Classni aniqlang.
   Classni aniqlash uchun siz classkalit so'zdan keyin class nomidan foydalanasiz . Masalan, quyidagilar Person classni
   belgilaydi:

   ```python
   class Person:
        pass
   ```

   Classdan ob'ekt yaratish uchun Person siz class nomidan keyin qavslardan foydalanasiz (), masalan, funktsiyani
   chaqirish:
   ```python
    person = Person()
   ```
   Ushbu misolda, bu person classning namunasidir Person. Class lar chaqirilishi mumkin .

---

3. ### instance atributlarini aniqlang.
 ```python
   # class ClassName:
#     ...
#     # statement-1>
#     # .
#     # .
#     # statement-n>

# class object
# class Myclass:
#     """A simple example class"""
#     num = 2024  # instance attribute
#
#     def foo(self):
#         return self.num
#
#
# obj = Myclass()
# print(obj.foo())

# __init__
"""
__init__ Ob'ektni yaratganingizda Person
Python avtomatik ravishda __init__ misol
atributlarini ishga tushirish methodini chaqiradi.
Methodda __init__ bu self class ning namunasi dir 
"""  # noqa


class Person:

    def __init__(self, name, age):
        """
           Shaxsni yaratishda "Musharraf" and 24 argument sifatida uzatiladi,
           bu argument ob'ektni ishga tushirish uchun __init__ usuliga
           o'tkaziladi.
           """  # noqa
        self.name = name
        self.age = age

    def display(self):
        """class method display"""
        return f"name: {self.name}\nage: {self.age}"


person1 = Person("Musharraf", 24)  # object one
# print(person1) # <__main__.Person object at 0x104556fd0>
# print(person1.age)
# print(person1.name)
print(person1.display())  # get class attributes
print(person1.display.__doc__)  # get class method docstring
print(person1.__init__.__doc__)  # get class __init__ method docstring
```

   Python dinamik. Bu shuni anglatadiki, siz ish vaqtida dinamik ravishda class instance siga atribut qo'shishingiz
   mumkin.

   Masalan, quyidagilar `name` ob'ektga atributni qo'shadi `person`:

   ```python
   person.name = 'John'
   ```
   Biroq, agar siz boshqa ob'ekt yaratsangiz `Person`, yangi ob'ekt atributga ega bo'lmaydi `name`.

   Classning barcha misollari uchun atributni aniqlash va ishga tushirish uchun siz `__init__`methoddan foydalanasiz.
   Quyidagi Person ikkita misol atributlari bilan class ni belgilaydi `name` va `age`:

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   ```
   Ob'ektni yaratganingizda `Person` , Python avtomatik ravishda `__init__` misol atributlarini ishga tushirish
   methodini
   chaqiradi. Methodda `__init__` bu self class ning namunasi dir `Person`.

   Quyidagilar Person nomli ob'ektni yaratadi `person`:

   ```python
   person = Person('John', 25)
   ```
   Ob'ekt `person` endi `name` va ageatributlariga ega. Misol atributiga kirish uchun siz nuqta belgisidan foydalanasiz.
   Masalan, quyidagi ob'ektning nom atributining qiymatini qaytaradi `person`:

   ```python
   person.name
   ```

---

4. ### `instance`namuna methodlarini aniqlang.

   Quyida Classga chaqirilgan misol methodi greet()qo'shiladi Person:

   ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hi, it's {self.name}."
   ```
   instance methodni chaqirish uchun siz nuqta belgilaridan ham foydalanasiz. Masalan:

   ```python
   person = Person('John', 25)
   print(person.greet())
   ```
   natija:

   ```shell
   Hi, it's John
   ```

---

5. ### Class atributlarini aniqlang.
   Misol atributlaridan farqli o'laroq, class atributlari classning barcha misollari tomonidan baham ko'riladi. Agar siz
   class konstantalarini yoki class misollari sonini kuzatib boruvchi o'zgaruvchilarni aniqlamoqchi bo'lsangiz, ular
   foydali bo'ladi.
   Masalan, `counter` classdagi class atributini quyidagilar belgilaydi `Person` :

   ```python
   class Person:
        counter = 0
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hi, it's {self.name}."
   ```
   `counter` Siz atributga classdan kirishingiz mumkin `Person` :

   ```python
   Person.counter   
   ```

   Yoki class ning har qanday misollaridan `Person` :

   ```python
   person = Person('John', 25)
   person.counter
   ```

   O'zgaruvchini foydaliroq qilish uchun `counter` ob'ekt yaratilgandan so'ng uning qiymatini bittaga oshirishingiz
   mumkin.
   Buni amalga oshirish uchun siz `counter` methodda class atributini oshirasiz `__init__` :

   ```python
    class Person:
        counter = 0

        def __init__(self, name, age):
            self.name = name
            self.age = age
            Person.counter += 1

        def greet(self):
            return f"Hi, it's {self.name}."
   ```

   Quyidagilar classning ikkita nusxasini yaratadi `Person` va qiymatini ko'rsatadi `counter` :

   ```python
   p1 = Person('Musharraf', 25)
   p2 = Person('Musharraf', 22)
   print(Person.counter)
   ```
   natija:

   ```shell
   2
   ```

---

6. ### Class methodini aniqlang
   Class atributi singari, class methodi ham classning barcha misollari tomonidan baham ko'riladi. Class methodining
   birinchi argumenti bu classning o'zi. An'anaga ko'ra, uning nomi `cls`. Python avtomatik ravishda bu argumentni class
   methodiga uzatadi. Bundan tashqari, siz class methodini bezash uchun `@classmethod` dekoratoridan foydalanasiz.

   Quyidagi misol anonim ob'ektni qaytaradigan class methodini belgilaydi `Person`:
   ```python
   class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)
   ```
   Quyida `create_anonymous()` class methodini qanday chaqirish ko'rsatilgan:
   ```python
   anonymous = Person.create_anonymous()
   print(anonymous.name)  # Anonymous
   ```

---

7. ### Static methodni aniqlang
   Python dasturlash tilida static methodlar (statik metodlar) class metodlari bo'lib, ular class (klass) darajasida chaqiriladi va class obyektlarining holatiga (state) bog'liq emas. Statik metodlar classga tegishli umumiy funksiyalarni amalga oshirish uchun foydalaniladi. Ular `@staticmethod` dekoratori yordamida yaratiladi.
   ```python
   class MathOperations:
        @staticmethod
        def add(a, b):
            return a + b

   # Statik metodni classning obyekti orqali chaqirish mumkin:
   result = MathOperations()
   print(result.add(5, 10))  # 15

   # Yoki to'g'ridan-to'g'ri class nomi orqali chaqirish mumkin:
   result = MathOperations.add(15, 25)
   print(result)  # 40
   ```
   Ushbu misolda MathOperations classi bor va unda add statik metodi mavjud. add metodi ikkita argumentni qabul qiladi va ularning yig'indisini qaytaradi. Statik metodlar class yoki obyekt holatiga bog'liq emasligi sababli, ular class nomi orqali to'g'ridan-to'g'ri chaqirilishi mumkin.

   `Statik metodlar qachon foydali bo'lishi mumkin`:

   Agar metod classning holatiga yoki obyektining holatiga bog'liq bo'lmasa.
   Classning umumiy funksiyalarini aniqlashda (matematika amallar, utility functions va hokazo).
---

8. ### Yagona `inheritance`meros
   Class boshqa classni meros qilib olish orqali uni qayta ishlatishi mumkin. Agar bolalar classi ota-classdan meros bo'lsa, bolalar class ota-classning atributlari va methodlariga kirishi mumkin.

   Masalan, siz `Employee` classdan meros bo'lgan classni belgilashingiz mumkin `Person`:
   ```python
   class Employee(Person):
        def __init__(self, name, age, job_title):
            super().__init__(name, age)
            self.job_title = job_title
   ```
   `__init__` Class methodi ichida va atributlarini ishga tushirish uchun class methodini `Employee` chaqiradi . Bu bolalar classiga ota-class methodiga kirish imkonini beradi.`__init__Person name age super()`

   Class yana bitta atributni qo'shish orqali classni `Employee` kengaytiradi .`Person job_title`

   Bu Person ota-ona class, esa `Employee` bolalar classi. `greet()` Classdagi methodni bekor qilish uchun siz classdagi methodni quyidagicha `Person` belgilashingiz mumkin :`greet() Employee`
   ```python
   class Employee(Person):
        def __init__(self, name, age, job_title):
            super().__init__(name, age)
            self.job_title = job_title

        def greet(self):
            return super().greet() + f" I'm a {self.job_title}."
   ```
   greet()` dagi method class methodi `Employee` deb ham ataladi . Boshqacha qilib aytganda, u ota-ona classining methodiga vakil qiladi.`greet()` Person

   Quyidagilar classning yangi namunasini yaratadi `Employee` va methodni chaqiradi greet()`:
   ```python
   employee = Employee('Musharraf', 25, 'Python Developer')
   print(employee.greet())
   ```
   natija:
   ```shell
   Hi, it's Musharraf. I'm a Python Developer.
   ```
Ushbu qo'llanmada siz Python-da ob'ektga yo'naltirilgan dasturlashning qisqacha ko'rinishini o'rgandingiz.

