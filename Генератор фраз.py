import random


otvet=input("Хочешь узнать кто ты сегодня? (да/нет): ")
WORDS1 = ("задорный", "подозрительный", "вредный", "застенчивый", "рисковый")
WORDS2 = ("жиробас", "огурчик", "карапуз", "алкаш", "пятачок")
WORDS3 = ("в дурдоме", "в печали", "со справкой", "с бородой", "под мостом")

while otvet=='да':
    word1 = random.choice(WORDS1)
    word2 = random.choice(WORDS2)
    word3 = random.choice(WORDS3)
    print(word1, word2, word3, end='')
    print()
    otvet=input("Хочешь узнать кто ты сегодня? (да/нет): ")

    
