
#before_month = 0
def month_change(date, before = "0000-13-00"):
    ##global before_month
    before = before.split("-")
    date = date.split("-")
    #print(date, "date", before)
    if(before[1] != date[1]):
        return False
    return True


# print(month_change("2020-04-06"))
# print(month_change("2020-04-07"))