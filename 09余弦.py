import math


def get_dot(vec_a, vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量必须维度相同")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b
    return dot_sum


def get_norm(vec):
    return math.sqrt(sum(v * v for v in vec))


def get_cosine_similarity(vec_a, vec_b):
    """计算两个向量的余弦相似度"""
    dot_product = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0  

    return dot_product / (norm_a * norm_b)


# 测试一下
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(f"点积: {get_dot(v1, v2)}")
print(f"v1 的模长: {get_norm(v1):.2f}")
print(f"余弦相似度: {get_cosine_similarity(v1, v2):.4f}")