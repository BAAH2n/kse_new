import area as a
import utils as u
import temperature as t
import password_generator as p
import text_stats as s
import finance_tracker as f

print (a.rectangle_area(20, 40))
print (a.circle_area(24))
print (u.is_prime(12))
print (t.c_to_f (21))
print (t.f_to_c(80))
print (p.generate_password(19, False))
print (p.generate_password(11, True))
print (s.count_words('Тестове речення, яке дуже цікаве'))
print (s.average_word_length('Тестове речення, яке дуже цікаве'))
transactions = {}
f.add_transaction(transactions, 5000, "дохід", "житло")
print (transactions)
print (f.get_balance(transactions))