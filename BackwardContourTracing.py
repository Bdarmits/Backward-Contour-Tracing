from PIL import Image

def BCT(img, starting_pix,run = 10):

    lst_pix = img.load()
    background_pix = []
    current_pix = starting_pix
    conts = [current_pix]
    position = 0

    def next_cont_finder(n, m,run=10):

        def find_dif(c):
            return lst_pix[current_pix[0], current_pix[-1]][c] -run <= \
                   lst_pix[current_pix[0] + n, current_pix[-1] + m][c] <= lst_pix[current_pix[0], current_pix[-1]][
                       c] +run

        if find_dif(0) and find_dif(1) and find_dif(2) and [current_pix[0] + n, current_pix[-1] + m] not in background_pix:
            return list([current_pix[0] + n, current_pix[-1] + m])

    def search_nearest(pos,run = 10, side = False):

        def give_cords(p, c):
            return [[-1, -1],[0, -1],[1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]][p][c]
        counter = 0
        for p in range(pos, pos + 8):
            temp = pos
            p %= 8
            if side == True:
                p = temp - counter
                if p < 0:
                    p += 8
            neighbour_pix = next_cont_finder(give_cords(p, 0), give_cords(p, 1),run)
            if neighbour_pix is not None:
                return neighbour_pix, p
            counter += 1
        return None, None

    def compare():
        return neighbour_pix != None and neighbour_pix != ending_pix

    def make_img():
        width, height = img.size
        new_img = Image.new("RGB", list([width, height]), 'white')
        new_lst_pix = new_img.load()
        for (i, j) in conts:
            new_lst_pix[i, j] = (0, 140, 0)
        new_img.show()
        return conts

    neighbour_pix_l, position_l = search_nearest(position,run)
    if position_l is None:
        return conts
    neighbour_pix_r, position_r = search_nearest(position,run, True)
    while neighbour_pix_l == neighbour_pix_r:
        ind = conts.index(current_pix)
        conts.pop(ind)
        background_pix.append(current_pix)
        current_pix = neighbour_pix_l
        conts.append(current_pix)
        neighbour_pix_l, position_l = search_nearest(position,run)
        if position_l is None:
            return conts
        neighbour_pix_r, position_r = search_nearest(position,run, True)
    ending_pix = current_pix
    position = position_l
    current_pix = neighbour_pix_l
    conts.append(current_pix)

    while 1:
        position = (position + 6) % 8
        old_pos = position
        neighbour_pix, position = search_nearest(position,run)
        if compare() and not(neighbour_pix in conts):
            current_pix = neighbour_pix
            conts.append(current_pix)
        elif compare() and neighbour_pix in conts:
            background_pix.append(neighbour_pix)
            position = old_pos
        elif neighbour_pix == ending_pix or len(conts) == 0:
            return make_img()
        elif neighbour_pix == None:
            conts.remove(current_pix)
            background_pix.append(current_pix)
            current_pix = conts[-1]
            position = old_pos

