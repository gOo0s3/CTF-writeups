import bcrypt

hash = "$2a$10$M6ZEdhJDnMmqTyNm6E1tyuzpS7EYH6I.qxvWoxDpQPDWyxStR1p7u"
SALT = bcrypt.gensalt(10)

print(bcrypt.hashpw("b".encode(), SALT))
