## Python class

- Xulosa : ushbu qo'llanmada siz Python classlari va ob'ektlari va yangi classni qanday aniqlash haqida bilib olasiz.

## Ob'ektlar

- Ob'ekt - bu ma'lumotlar va funksionallikni o'z ichiga olgan konteyner .

- Ma'lumotlar ob'ektni ma'lum bir vaqtning o'zida aks ettiradi. Shuning uchun ob'ektning ma'lumotlari holat deb
  ataladi . Python ob'ekt holatini modellashtirish uchun atributlardan foydalanadi .

- Funktsionallik ob'ektning xatti-harakatlarini ifodalaydi. Python xatti-harakatlarni modellashtirish uchun
  funktsiyalardan foydalanadi. Agar funktsiya ob'ekt bilan bog'langan bo'lsa, u ob'ektning usuliga aylanadi.

- Boshqacha qilib aytganda, ob'ekt holati va usullarini o'z ichiga olgan konteynerdir .

- Ob'ektlarni yaratishdan oldin siz avval classni aniqlaysiz. Va classdan siz bir yoki bir nechta ob'ektlarni
  yaratishingiz mumkin. Class ob'ektlari class misollari deb ham ataladi.

## class ni aniqlang

- Python-da classni aniqlash uchun siz `class` kalit so'zdan keyin class nomi va ikki nuqtadan foydalanasiz. Quyidagi
  misol `Person` classni belgilaydi:
  ```python
  class Person:
    pass
  ```
- An'anaga ko'ra, siz Pythondagi classlar uchun bosh harflar bilan yozilgan nomlardan foydalanasiz. Agar class nomi bir
  nechta so'zlardan iborat bo'lsa, siz `CamelCase` formatdan foydalanasiz, masalan `SalesEmployee`.
- `Person` Class to'liq bo'lmaganligi sababli ; `pass` keyinroq unga qo'shimcha kod qo'shishingizni bildirish uchun
  bayonotdan foydalanishingiz kerak .
  Class namunasini yaratish uchun siz class nomidan quyidagi kabi qavslar bilan foydalanasiz:
  ```python
  person = Person()
  ```
  Ob'ektni chop etishda personsiz uning nomi va xotira manzilini ko'rasiz:
  ```python
  class Person:
    pass


  print(person)
  ```
  Chiqish:
  ```python
  <__main__.Person object at 0x000001C46D1C47F0>
  ```
  Ob'ektning identifikatorini olish uchun siz `id()` funksiyasidan foydalanasiz. Masalan:

  ```python
  print(id(person))
  ```
  Chiqish:
  ```python
  1943155787760
  ```
  Ob'ektning identifikatori noyobdir. `CPython` da `id()` ob'ektning xotira manzilini qaytaradi. `hex()`
  funksiyasi `id()` funksiyasi tomonidan qaytarilgan butun sonni 0x prefiksli kichik o‘n oltilik qatorga o‘zgartiradi:

  ```python
  print(hex(id(person)))
  ```

  Chiqish:
  ```python
  0x1c46d1c47f0
  ```

  Shaxs ob'ekti classning namunasidir `Person`. Agar ob'ekt classning namunasi bo'lsa, funktsiya `isinstance()`
  qaytariladi :`True`
  ```python
  print(isinstance(person, Person))  # True
  ```

## Class ham Pythonda ob'ekt hisoblanadi

- Python-da hamma narsa ob'ekt, shu jumladan classlar.

  Classni aniqlaganingizda `Person`, Python nomi bilan ob'ekt yaratadi `Person`. Ob'ekt `Person` atributlarga ega. Masalan, `__name__` atribut yordamida uning nomini topishingiz mumkin:

  ```python
  print(Person.__name__)
  ```
  Chiqish:
  ```python
  Person
  ```


- Ob'ekt `Person` quyidagi turga ega `type`:
  ```python
  print(type(Person))
  ```


  Chiqish:
  ```python
  <class 'type'>
  ```


Classning Person xulq-atvori ham bor. Masalan, u yangi misol yaratishi mumkin:
  ```python
  person = Person()
  ```

Xulosa
- Ob'ekt - bu holat va xatti-harakatni o'z ichiga olgan konteyner.
- Class - bu ob'ektlarni yaratish rejasi.
- Pythonda class ham ob'ekt bo'lib, u `type`.
  




