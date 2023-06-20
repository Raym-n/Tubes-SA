def greedy_move(pieces, table):
    count = [0] * 7  # Menghitung frekuensi setiap angka potongan domino
    for piece in pieces:
        count[piece[0]] += 1
        count[piece[1]] += 1    
    best_piece = None
    best_score = -1    
    for piece in pieces:
        score = count[piece[0]] + count[piece[1]]
        if score > best_score:
            best_score = score
            best_piece = piece    
    return best_piece

def play_domino(pieces):
    table = [(0, 0)]  # Meja dimulai dengan potongan (0, 0)    
    while len(pieces) > 0:
        piece = greedy_move(pieces, table)        
        if piece[0] == table[-1][1]:
            # Potongan domino cocok dengan angka terakhir di meja
            table.append(piece)
        else:
            # Potongan domino dirotasi dan cocok dengan angka terakhir di meja
            table.append((piece[1], piece[0]))        
        pieces.remove(piece)    
    print("Solusi ditemukan:")
    for piece in table:
        print(piece)

pieces = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]  # Contoh potongan domino
play_domino(pieces)


