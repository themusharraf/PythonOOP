## Python ob'ektga yo'naltirilgan dasturlash
---

- Xulosa : ushbu qo'llanmada siz Python-da ob'ektga yo'naltirilgan dasturlashni o'rganasiz, jumladan objects, classes,
  attributes, methods, inheritances, overriding methods va boshqalar kabi muhim tushunchalar bor.

1. ### Python ob'ektga yo'naltirilgan dasturlashga kirish

   `Python-da hamma narsa ob'ektdir`. Ob'ektning holati va xatti-harakatlari mavjud. Ob'ektni yaratish uchun avval siz
   classni aniqlaysiz. Va keyin, classdan siz bir yoki bir nechta ob'ektlarni yaratishingiz mumkin. Ob'ektlar classning
   namunalari.

---

2. ### Classni aniqlang
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

3. ### Namuna atributlarini aniqlang.

   Python dinamik. Bu shuni anglatadiki, siz ish vaqtida dinamik ravishda class namunasiga atribut qo'shishingiz mumkin.

   Masalan, quyidagilar `name` ob'ektga atributni qo'shadi person:

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
   chaqiradi. Usulda `__init__` bu self class ning namunasi dir `Person`.

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

4. ### Namuna methodlarini aniqlang.

---

5. ### Class atributlarini aniqlang.

---

6. ### Class methodini aniqlang

---

7. ### Statik methodni aniqlang

---

8. ### Yagona `inheritance`meros