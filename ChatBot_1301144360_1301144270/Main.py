import random
import re

kumpulanpattern = [
    # 0
    ["end",
     ["Terima kasih sudah menggunakan aplikasi ini :)"]],

    #1
    [r'(.*) (K|k)has (\w+)',
     ["Wah, Saya belum pernah coba makanan khas {2}",
      "Coba ceritakan bagaimana rasa dari makanan khas {2} ?"]],

    #2
    [r'(S|s)aya suka (\w+)(.*)',
     ["Makanan seperti apa itu ?",
      "Saya tertarik untuk mencobanya"]],

    #3
    [r'(.*) (R|r)asanya (\w+)',
     ["Pasti enak ya :9",
      "Saya lebih suka makanan dengan rasa yang {2} sedikit",
      "Perut saya tidak baik ketika mencoba memakan {0}"]],

    #4
    [r'(M|m)akanan (\b[kesukaan])(.*)',
     ["Saya suka mencoba semua jenis makanan, bagaimana denganmu ?",
      "Saya tertarik untuk mencoba makanan khas dari berbagai daerah",
      "Sebenarnya Saya rindu dengan jajanan Bandung :("]],

    #5
    [r'(K|k)enapa (([^\?]*)\?) ?',
     ["Mungkin bisa ditanyakan kepada google kenapa {1}",
      "Saya kurang tahu mengapa bisa seperti itu",
      "Karena mungkin ada makanan yang membuat {1}"]],

    #6
    [r'(.*) (B|b)erapa banyak (([^\?]*)\?) ?',
     ["Menurutmu ada berapa banyak {2} ?",
      "Berapa banyakpun yang penting adalah sesuai dengan porsi dan rasanya enak :9"]],

    #7
    [r'(.*) (R|r)ekomendasi(.*)',
     ["Saya merekomendasikan mencicipi makanan tradisional dahulu",
      "Saya rasa makanan khas luar negri juga harus dicicipi"]],

    #8
    [r'(.*) (M|m)enu (.*)',
     ["Coba jelaskan menu dari {2}",
      "Menu yang paling murah disana apas saja ?"]],

    #9
    [r'(.*) (M|m)urah (.*)',
     ["Apakah rasanya enak ?",
      "Coba makanan yang lebih mahal, mungkin rasanya akan berbeda",
      "Sepertinya banyak makanan yang lebih murah di pinggir jalan"]],

    #10
    [r'(.*) (H|h)arganya (\d*)',
     ["Apa ada makanan yang lebih murah ?",
      "Bagaimana dengan rasanya apabila harganya {2} ?"]],

    #11
    [r'(.*) (H|h)arga (\d*) (.*) ?',
     ["Dengan harga {2}, menurut saya sudah terbilang murah",
      "Dengan harga {2}, menurut saya sudah terbilang mahal"]],

    #12
    [r'(.*) (I|i)bu (.*)',
     ["Apakah Ayahmu juga bisa memasak ?",
      "Bagaimana dengan rasa dari racikan orangtuamu ?",
      "Makanan akan lebih enak apabila diracik oleh orangtua :)"]],

    #13
    [r'(.*) (R|r)esep (.*)',
     ["Coba jelaskan resep apa itu ?",
      "Bagaimana cara membuatnya ?",
      "Saya tertarik untuk mencoba resep {2}"]],

    #14
    [r'(.*) (T|t)ahun (\d*)',
     ["Makanan yang sedang tren di tahun ini apa ?",
      "Sepertinya akan ada kuliner baru pada tahun mendatang",
       "Menurutmu makanan apa yang akan ada di tahun 2020 ?"]],

    #15
    [r'(M|m)inuman (\b[kesukaan])(.*)',
     ["Bagaimana dengan minuman kesukaanmu ?",
      "Minuman kesukaanku adalah squash orange"]],

    #16
    [r'(.*) tradisional (.*)',
     ["Saya menyukai makanan tradisional",
      "Sebenarnya saya menyukai makanan luar negri juga :D",
      "Makanan tradisional yang kamu suka apa?"]],

    #17
    [r'(.*) dimana ?',
     ["Coba gunakan google maps untuk menemukan {0} dimana",
      "Saya pernah melihatnya, namun saya lupa dimana"]],

    #18
    [r'(.*) (I|i)nternet (.*)',
     ["Banyak sekali makanan yang dapat dilihat di internet",
      "Makanan apa yang direkomendasikan dari google search dengan keyword 'makanan enak di Bandung' ?",
      "Saya pernah melihat rendang adalah makanan enak No.1 di dunia. Bagaimana menurutmu rasa dari rendang ?"]],

    #19
    [r'(.*) (P|p)ernah (.*)',
     ["Saya belum pernah kesana, apakah disana adalah tempat kuliner yang menarik ?",
      "Saya ingin berjalan-jalan kesana :(",
      "Pasti tempat tersebut sangatlah terkenal"]],

    #20
    [r'(.*) (R|r)estaurant (.*)',
     ["Restaurant {2} punya menu apa saja ?",
      "Berapa kisaran harga di restaurant {2} ?",
      "Makanan apa yang paling rekomendasikan di sana ?"]],

    #21
    [r'(.*)',
     ["{0}",
      "Oooh...",
      "Oh, {0}",
      "Apa yang Anda bicarakan ?",
      "Saya tidak mengerti :(",
      "Mungkin lebih baik kita berdiskusi tentang makanan saja :D"]]
]

katadiubah = {
    "saya" : "anda",
    "aku" : "kamu",
    "kita" : "kalian",
    "kamu" : "aku",
    "anda" : "saya"
}

def ubah(kata):
    splitkata = kata.lower().split()
    for indeks, indekskata in enumerate(splitkata):
        if indekskata in katadiubah:
            splitkata[indeks] = katadiubah[indekskata]
    return ' '.join(splitkata)


def proses(inputan):
    for pattern, pilihanjawaban in kumpulanpattern:
        patternsama = re.match(pattern, inputan.rstrip(".!"))
        if patternsama:
            jawaban = random.choice(pilihanjawaban)
            return jawaban.format(*[ubah(kata) for kata in patternsama.groups()])

def main():
    print "Bot  : Apa yang ingin Anda bicarakan tentang kuliner?"
    inputan = ""
    while (inputan != "end"):
        inputan = raw_input("Anda : ")
        print "Bot  : " + proses(inputan)

if __name__ == "__main__":
    main()