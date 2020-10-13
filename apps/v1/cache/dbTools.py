from apps.v1.models import User


def mongoInsertMany(dataList: list):
    """
    mongoDB批量插入数据，加入某一条记录错误则忽略继续插入（如唯一索引触发错误）
    :return:
    """
    User._get_collection().insert_many(dataList, ordered=False, bypass_document_validation=True)


def mongoInsertOrUpdate(oneData: dict):
    """
    mongoDB新增一个新记录，加入有则更新，没有则直接创建
    :param oneData:
    :return:
    """
    # 首先查看是否有name相同的对象，有则更新，无则新增
    User.objects(name=oneData["name"]).update_one(**oneData, upsert=True)