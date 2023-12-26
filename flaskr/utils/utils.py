
import hashlib

def calculate_signature(token, timestamp, nonce, msg_encrypt):
    # 对参数进行排序
    sorted_params = sorted([token, timestamp, nonce, msg_encrypt])

    # 拼接排序后的参数
    joined_params = ''.join(sorted_params)

    # 计算SHA-1哈希
    sha1 = hashlib.sha1()
    sha1.update(joined_params.encode('utf-8'))
    signature = sha1.hexdigest()

    return signature
