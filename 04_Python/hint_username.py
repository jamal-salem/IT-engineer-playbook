def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
        return False  # إرجاع خطأ ليفهم النظام أن الاسم مرفوض
    else:
        print("Valid username!")
        return True   # إرجاع صحيح ليفهم النظام أن الاسم مقبول
