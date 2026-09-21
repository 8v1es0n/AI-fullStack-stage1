# ============================================================================
# 练习1：智能数据筛选器
# ============================================================================
#
# 题目描述：
#   请设计一个通用数据筛选函数 filter_data，要求功能如下：
#   1. 通过 *args 接收任意数量的数值数据
#   2. 通过 **kwargs 接收筛选配置，支持的配置项包括：
#      - threshold：阈值，只保留大于等于该值的数据（默认：无阈值）
#      - top_n：只保留前N个（默认：全部保留）
#      - unique：是否去重（默认 False）
#      - sort_order：排序方式，"asc" 升序 / "desc" 降序（默认 "asc"）
#   3. 为所有函数添加完整的类型注解
#
#   测试：
#     filter_data(5,2,9,1,7,3,8,2,9,4, threshold=5, unique=True, sort_order="desc")
#       → [9, 8, 7, 5]
#     filter_data(3,5,1,8,6, top_n=3)
#       → [1, 3, 5]
# ============================================================================


def filter_data(*args, **kwargs: int | str | bool) -> list[int]:
    threshold = kwargs.get("threshold")
    top_n = kwargs.get("top_n")
    unique = kwargs.get("unique", False)
    sort_order = kwargs.get("sort_order", "asc")

    # 2. 数据处理 -- 元组 -> 列表
    data_list = list(args)

    # 3. 阈值处理
    if threshold is not None:  # threshold 不是None值
        data_list = [i for i in data_list if i >= threshold]

    # 4. 去重
    if unique:
        data_list = list(set(data_list))

    # 5. 排序
    data_list.sort(reverse=(sort_order == "desc"))  # sort_order --> "desc" ; sort_order --> "asc"

    # 6. 保留前N个
    if top_n is not None:
        data_list = data_list[:top_n]

    return data_list


result = filter_data(5, 2, 9, 1, 7, 3, 8, 2, 9, 4,
                     threshold=5, unique=True, sort_order="asc", top_n=3)
print(result)