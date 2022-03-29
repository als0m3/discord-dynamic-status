
def spaceInvader(index_):
    step_1 = 7
    step_2 = 14

    cursor = "👾"
    space = "⠀"

    if index_ < step_1:
        return index_+1, index_*space + cursor + (step_1-index_)*space
    elif index_ < step_2:
        return index_+1, (step_2-index_)*space + cursor + (index_-step_1)*space
    else:
        return 1, cursor + (step_1)*space


def loading1(index_):
    if index_ == 10:
        return 1, "[----------]"
    else:
        return index_+1, "[" + index_*"=" + (10-index_)*"-" + "]"
