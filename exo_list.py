########## EXO 1 ##########
def somme_cumulative(liste):
    new_list = []
    for i in range(len(liste)):
        if i == 0:
            new_list.append(liste[i])
        else:
            new_list.append(liste[i] + new_list[i - 1])
    return new_list


################# EXO 2 ##############
def palindrome(liste):
    n = len(liste) // 2
    print(n)
    for i in range(n + 1):
        if liste[i] != liste[-(i + 1)]:
            return False
        else:
            if i == n:
                return True


def trier(liste, reverse=False):
    for i in range(len(liste)):
        for j in range(i, len(liste)):
            if reverse:
                if liste[i] < liste[j]:
                    temp = liste[i]
                    liste[i] = liste[j]
                    liste[j] = temp
            else:
                if liste[i] > liste[j]:
                    temp = liste[i]
                    liste[i] = liste[j]
                    liste[j] = temp

    return liste


def fusion_list_trier(liste1, liste2):
    if liste1[0] > liste2[0]:
        liste2.extend(liste1)
        return liste2
    else:
        liste1.extend(liste2)
        return liste1


def suppression_des_doublons(liste):
    s_list = []
    for elt in liste:
        if elt not in s_list:
            s_list.append(elt)
    return s_list


def produit_cumulatif(liste):
    sc_list = []
    for i in range(len(liste)):
        if i == 0:
            sc_list.append(liste[i])
        else:
            sc_list.append(liste[i]*sc_list[i-1])
    return sc_list


def sous_list_max_som():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if '__main__' == __name__:
    # list_ = [4, 20, 3, -2]
    # print(somme_cumulative(list_))
    # liste = [1, 2, 4, 4, 2, 1]
    # print(palindrome(liste))
    # liste = [4, 20, 3, -2]
    # print(trier(liste))
    # print(trier(liste, reverse=True))
    # liste1 = [1, 2, 3, 4, 5]
    # liste2 = [6, 7]
    # print(fusion_list_trier(liste1, liste2))
    # liste = [1, 2, 3, 4, 5, 3, 1, 6, 7, 8, 7, 0]
    # print(suppression_des_doublons(liste))
    liste = [1, 2, 3, 4]
    print(produit_cumulatif(liste))

