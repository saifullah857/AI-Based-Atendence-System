from src.database.config import supabase
import bcrypt


# 🔐 Hash password
def has_pass(password):
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')


# 🔑 Check password
def check_pass(password, hashed):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed.encode('utf-8')
    )


# 🔍 Check if teacher exists
def check_teacher_exist(username):
    response = supabase.table("teachers") \
        .select("username") \
        .eq("username", username) \
        .execute()

    return len(response.data) > 0


# 👨‍🏫 Create teacher
def create_teacher(username, password, name):
    data = {
        "username": username,
        "password": has_pass(password),
        "name": name
    }

    response = supabase.table("teachers") \
        .insert(data) \
        .execute()

    return response.data


# 🔐 Teacher login (FIXED)
def teacher_login(username, password):
    response = supabase.table("teachers") \
        .select("*") \
        .eq("username", username) \
        .execute()

    if len(response.data) == 0:
        return None

    teacher = response.data[0]

    if check_pass(password, teacher["password"]):
        return teacher  
    else:
        return None