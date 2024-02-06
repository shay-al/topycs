def gimatria(heb_str=''):
    letters=['אבגדהוזחט','יכלמנסעפצ','קרשת']
    valids=[chr(i) for i in range(ord('א'), ord('ת')+1)]
    heb_str="".join([ch for ch in heb_str if ch in valids])
    wheights={}
    for level in range(len(letters)):
        set_of_chars=letters[level]
        for ind in range(len(set_of_chars)):
            wheights[set_of_chars[ind]]=(10**level)*(ind+1)
    end_letters={'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}
    end_L_keys=end_letters.keys()
    value=0
    for L in heb_str:
        if L in end_L_keys:
            L=end_letters[L]
        value+=wheights[L]
    return (value)
