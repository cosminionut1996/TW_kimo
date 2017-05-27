# from django import template
#
# import redis
# import rediscoll
#
# from kimo.models import VMS
#
#
# # Tags
# register = template.Library()
#
#
# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)
#
#
# @register.simple_tag
# def get_num_jobs():
#     redis_queues = [_.name for _ in VMS.objects.all()]
#     host, port = 'ausserver01', '6379'
#     num_jobs = 0
#     try:
#         res = dict()
#         res['detailed'] = dict()
#         for queue in redis_queues:
#             q = rediscoll.PriorityRedisQueue(
#                 host=host, port=port, key=queue,
#                 reverse=True, seron=False, norm=False
#             )
#             res['detailed'][queue] = q.size()
#             num_jobs += q.size()
#         res['total'] = num_jobs
#         return res
#     except redis.exceptions.ConnectionError:
#         """ getaddrinfo failed. 'ausserver01' might be down. """
#         return {
#             'detailed': {
#                 'win7_x86': "?",
#                 'win7_x64': "?",
#                 'win8_x86': "?",
#                 'win8_x64': "?",
#                 'win10_x86': "?",
#                 'win10_x64': "?",
#             },
#             'total': "?",
#         }
