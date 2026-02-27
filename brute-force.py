alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

krypterat = "Äya, mux ÅTi xl öXuå!?"
ordlista = ["hej","jag", "du", "ni", "de", "dem", "dom", "han", "hon", "den", "det", "har", "ska", "inte", "att", "och", "är", "på"]

for nyckel in range(0, len(alfabet)):
    dekrypterat = ""
    for bokstav in krypterat:
        if bokstav.isalpha():
            b = alfabet[(alfabet.index(bokstav.lower()) - nyckel) % 29]
            if bokstav.isupper():
                b = b.upper()
                dekrypterat += b
            else:
                dekrypterat += b
    
        else:
            dekrypterat += bokstav

    print(f"Nyckel: {nyckel} | {dekrypterat}")
