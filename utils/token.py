import jwt
import datetime

from app_user.models import User


def generate_token(data, expire=3, secret='SECRET'):
    """
    生成token
    :data 自定义用户信息
    :expire 过期时间(天)
    :secret 密钥
    :return: str
    """
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=expire),  # 过期时间
        'iat': int(datetime.datetime.now().timestamp() - 120),  # 签发时间
        'iss': 'LIN0309',  # 签名
        'data': data,
    }
    return jwt.encode(dic, secret, algorithm='HS256')


def auth_token(token, secret='SECRET'):
    """
    验证token
    :token token
    :secret 密钥
    :return: dict
    """
    try:
        result = jwt.decode(token, secret, iss='LIN0309', algorithms=['HS256'])
        if result['iss']:
            return {"status": "success", "result": result}
    except jwt.exceptions.DecodeError as err:
        return {"status": "fail", "result": str(err)}

def student_token(token, secret='SECRET'):
    """
    验证token
    :token token
    :secret 密钥
    :return: dict
    """
    try:
        result = jwt.decode(token, secret, iss='LIN0309', algorithms=['HS256'])
        user=User.objects.get(username=result['data']['username'])
        if result['iss'] and user.authority=='1':
            return {"status": "success", "result": result}
        else:
            return {"status": "fail", "result": "权限不足"}
    except jwt.exceptions.DecodeError as err:
        return {"status": "fail", "result": str(err)}

def teacher_token(token, secret='SECRET'):
    """
    验证token
    :token token
    :secret 密钥
    :return: dict
    """
    try:
        result = jwt.decode(token, secret, iss='LIN0309', algorithms=['HS256'])
        user=User.objects.get(username=result['data']['username'])
        if result['iss'] and user.authority=='2':
            return {"status": "success", "result": result}
        else:
            return {"status": "fail", "result": "权限不足"}
    except jwt.exceptions.DecodeError as err:
        return {"status": "fail", "result": str(err)}