## Python ob'ektga yo'naltirilgan dasturlash
---

- Xulosa : ushbu qo'llanmada siz Python-da ob'ektga yo'naltirilgan dasturlashni o'rganasiz, jumladan objects, classes,
  attributes, methods, inheritances, overriding methods va boshqalar kabi muhim tushunchalar bor.

1. Python ob'ektga yo'naltirilgan dasturlashga kirish

   `Python-da hamma narsa ob'ektdir`. Ob'ektning holati va xatti-harakatlari mavjud. Ob'ektni yaratish uchun avval siz
   sinfni aniqlaysiz. Va keyin, sinfdan siz bir yoki bir nechta ob'ektlarni yaratishingiz mumkin. Ob'ektlar sinfning
   namunalari.

---

2. Classni aniqlang
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