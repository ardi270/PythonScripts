def paga_bruto_neto(pagaBruto:float):
    pagaMinimale = 34_000
    pagaMaxKonShoq = 149_954   # Paga Maksimale per kontributet shoqerore
    sigShoqPerqind = 9.5 / 100  # Sigurimet Shoqerore te punemarresit
    sigShenPerqind = 1.7 / 100  # Sigurimet shendetesore te punedhenesit
    tapKufiri40_000 = 40_000  # Kufiri prej 40_000 lekesh per TAP
    tapKufiri30_000 = 30_000  # Kufiri prej 30_000 lekesh per TAP
    tapKufiri20mil = 200_000  # Kufiri prej 200_000  lekesh per TAP
    tapKufiri50_000 = 50_000  # Kufiri prej 50_000  lekesh per TAP
    tap13Perqind = 13 / 100  # Tatimi prej 13% per TAP
    tap23Perqind = 23 / 100  # Tatimi prej 23% per TAP
    tap6Pike5Perqind = 6.5 / 100  # Tatimi pre 6.5% per TAP
    if pagaBruto < pagaMinimale:
        return None
    else:
        # LLogaritja e sigurimeve shendetesore dhe shoqerore
        pagaNeto = pagaBruto
        if pagaBruto > pagaMaxKonShoq:
            pagaNeto -= pagaMaxKonShoq * sigShoqPerqind
        else:
            pagaNeto -= pagaBruto * sigShoqPerqind
        pagaNeto -= pagaBruto * sigShenPerqind
        # Llogaritja e TAP
        if pagaBruto <= tapKufiri40_000:
            tap = 0.0  # per kufirin 40_000 nuk paguhet tap
        elif pagaBruto <= tapKufiri50_000:
            tap = (pagaBruto - tapKufiri30_000) * tap6Pike5Perqind
        elif pagaBruto <= tapKufiri20mil:
            tap = (pagaBruto - tapKufiri30_000) * tap13Perqind
        else:
            tap = (tapKufiri20mil - tapKufiri30_000) * tap13Perqind
            tap += (pagaBruto - tapKufiri20mil) * tap23Perqind
        pagaNeto -= tap
        return round(pagaNeto,2)

l = [97_073,100_000, 45_000, 52_000,210_000, 28_000,34_000,150000]
for paga in l:
    print("Paga Bruto", paga, ", Paga neto", paga_bruto_neto(paga))
