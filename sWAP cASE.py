def swap_case(s):
    edited_str = ""
    for i in s:
        if i == i.upper():
            lowered = i.lower()
            edited_str += lowered
        else:
            uppered = i.upper()
            edited_str += uppered
            
    return edited_str
