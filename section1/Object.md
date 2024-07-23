## Python ob'ektga yo'naltirilgan dasturlash
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

   Python dinamik. Bu shuni anglatadiki, siz ish vaqtida dinamik ravishda class instance siga atribut qo'shishingiz
   mumkin.

   Masalan, quyidagilar `name` ob'ektga atributni qo'shadi `person`:

   ```python
   person.name = 'John'
   ```
   Biroq, agar siz boshqa ob'ekt yaratsangiz `Person`, yangi ob'ekt atributga ega bo'lmaydi `name`.

   Sinfning barcha misollari uchun atributni aniqlash va ishga tushirish uchun siz `__init__`usuldan foydalanasiz.
   Quyidagi Person ikkita misol atributlari bilan class ni belgilaydi `name` va `age`:

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   ```
   Ob'ektni yaratganingizda `Person` , Python avtomatik ravishda `__init__` misol atributlarini ishga tushirish usulini
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
   Masalan, `counter` sinfdagi sinf atributini quyidagilar belgilaydi `Person` :

```python
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."
```

`counter` Siz atributga sinfdan kirishingiz mumkin `Person` :

```python
Person.counter
```

Yoki class ning har qanday misollaridan `Person` :

```python
person = Person('John', 25)
person.counter
```

O'zgaruvchini foydaliroq qilish uchun `counter` ob'ekt yaratilgandan so'ng uning qiymatini bittaga oshirishingiz mumkin.
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
p1 = Person('John', 25)
p2 = Person('Jane', 22)
print(Person.counter)
```

natija:

```shell
2
```

---

6. ### Class methodini aniqlang

---

7. ### Statik methodni aniqlang

---

8. ### Yagona `inheritance`meros