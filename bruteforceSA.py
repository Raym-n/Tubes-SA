pieces = []
for i in range(7):
    for j in range(i, 7):
        pieces.append((i, j))

def solve_domino(pieces, table):
    if len(pieces) == 0:
        # Semua potongan domino telah ditempatkan di meja
        return True    
    for i, piece in enumerate(pieces):
        if piece[0] == table[-1][1]:
            # Potongan domino cocok dengan angka terakhir di meja
            table.append(piece)
            if solve_domino(pieces[:i] + pieces[i+1:], table):
                return True
            table.pop()            
        elif piece[1] == table[-1][1]:
            # Potongan domino cocok dengan angka terakhir di meja setelah dirotasi
            table.append((piece[1], piece[0]))
            if solve_domino(pieces[:i] + pieces[i+1:], table):
                return True
            table.pop()    
    return False

def play_domino():
    table = [(0, 0)]  # Permainan dimulai dengan potongan (0, 0)
    if solve_domino(pieces, table):
        print("Solusi ditemukan:")
        for piece in table:
            print(piece)
    else:
        print("Tidak ada solusi yang ditemukan.")

play_domino()




